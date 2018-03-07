from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from inventory.models import Vendor, Product


class Command(BaseCommand):
    help = 'Merge two vendors. Second vendor will be kept'

    def add_arguments(self, parser):
        parser.add_argument("vendor1", type=str, help="vendor to merge")
        parser.add_argument("vendor2", type=str, help="vendor to merge into")

    def handle(self, *args, **options):
        try:
            vendor1 = Vendor.objects.get(pk=options["vendor1"])
        except ObjectDoesNotExist:
            raise CommandError("Make sure vendor1 is a valid Vendor")
        try:
            vendor2 = Vendor.objects.get(pk=options["vendor2"])
        except ObjectDoesNotExist:
            raise CommandError("Make sure vendor2 is a valid Vendor")

        products_of_vendor1 = Product.objects.filter(vendor=vendor1)
        for p in products_of_vendor1:
            p.vendor = vendor2
            p.save()

        vendor1.delete()
        self.stdout.write("Merge successful")
