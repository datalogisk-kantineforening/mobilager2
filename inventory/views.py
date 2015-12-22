from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db.models import Q

from .models import *


def _update_stock(request, change_type):
    products = Product.objects.all().filter(discontinued=False)
    if request.method == 'GET':
        users = User.objects.all().filter(active=True).order_by('name')
        context = {'sellables': products.filter(category=0), #FIXME: Magic numbers
                   'refundables': products.filter(category=1),
                   'names': users}
        return render(request, change_type + ".html", context)
    elif request.method == 'POST':

        updated = []
        for p in products:
            req_qty = int(request.POST[str(p.pk) + "_qty"])
            changed = req_qty != p.quantity
            # FIXME: Do log handling here
            old_qty = p.quantity
            p.quantity = req_qty
            updated.append((p, old_qty, changed))
            #p.save()
        if any(map(lambda t: t[2], updated)):
            # TODO: Do something better with EventType handling
            event = Event(description = request.POST['what'],
                          event_type = EventType.objects.get(tag = change_type))
            event.save()
            for u in request.POST.getlist("who"):
                event.eventname_set.add(EventName(
                    name = User.objects.get(pk = u)))

            for p, old_qty, _ in updated:
                event.change_set.add(Change(product = p,
                                            quantity = p.quantity,
                                            delta = p.quantity - old_qty))

            return HttpResponseRedirect("/"+ change_type)
        else:
            # TODO: no changes were made. Show error message
            return HttpResponseRedirect("/"+ change_type)

def stock(request):
    products = Product.objects.all().filter(discontinued=False)
    context = {'products': products}
    return render(request, "stock.html", context)

def replenish(request):
    return _update_stock(request, "replenish")

def restock(request):
    return _update_stock(request, "restock")

def correction(request):
    return _update_stock(request, "correction")

def history(request):
    events = Event.objects.order_by("-date").order_by("-time")
    e = list(map(lambda x: {'event': x,
                            'changes': x.change_set.filter(~Q(delta = 0))},
             events))

    return render(request, "history.html", {'events': e})
