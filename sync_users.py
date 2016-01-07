#!/usr/bin/env python3
import os
import sys
os.environ['DJANGO_SETTINGS_MODULE'] = "mobilager2.settings"

import django
from django.contrib.auth.models import User

from mobilager2.auth import *

def sync_users(pwfile):
    myusers = set(map(lambda x: x.username,
                      User.objects.filter(is_active = True).only('username')))
    print(myusers)
    for l in DokuwikiBackend.parse_file(pwfile, GROUP_FILTER):
        print(l[USERNAME])
        myusers.discard(l[USERNAME])
        DokuwikiBackend.get_update_user(l[USERNAME], l)

    # Mark users removed from dokuwiki inactive
    print(myusers)
    for u in myusers:
        user = User.objects.get(username = u)
        user.is_active = False
        user.save()


def main():
    if len(sys.argv) < 2:
        print("Usage: ./sync_users.py <dokuwiki password database>")
        sys.exit(1)

    pws = sys.argv[1]

    django.setup()
    auth = DokuwikiBackend()
    sync_users(pws)
    sys.exit(0)

if  __name__ == "__main__":
    main()
