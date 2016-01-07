from crypt import crypt
from hmac import compare_digest
import base64
import os

from django.conf import settings
from django.contrib.auth.models import User

NFIELDS = 5
USERNAME, CRYPT, REALNAME, EMAIL, GROUPS = list(range(NFIELDS))
GROUP_FILTER = lambda x: 'user' in x[GROUPS]

class DokuwikiBackend:
    @staticmethod
    def get_update_user(username, fields):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # Generate random password (we won't be using it anyway)
            pw = base64.b64encode(os.urandom(20))
            user = User(username=username, password=pw)

        # Get firstname, last name
        names = fields[REALNAME].split(' ')
        user.first_name = ''
        user.last_name = ''
        if len(names) == 1:
            user.first_name = names[0]
        elif len(names) > 1:
            user.first_name = ' '.join(names[0:-1])
            user.last_name = names[-1]

        user.email = fields[EMAIL]

        user.is_active = True
        user.is_staff = True

        user.save()
        return user

    @staticmethod
    def parse_file(pwfile, filter_pred = lambda x: x):
        with open(pwfile) as f:
            for l in f:
                if l.startswith('#'):
                    continue
                if len(l.strip()) == 0:
                    continue

                fields = l.strip().split(':')
                if len(fields) != NFIELDS and len(fields) > 0:
                    raise Exception('Invalid format')
                if filter_pred(fields):
                    yield fields

    def authenticate(self, username=None, password=None):
        # Look for username in the dokuwiki auth file
        for l in DokuwikiBackend.parse_file(settings.DOKUWIKI_AUTH_FILE,
                                            GROUP_FILTER):
            if username == l[USERNAME]:
                # Check password
                if not compare_digest(crypt(password, l[CRYPT]),
                                      l[CRYPT]):
                    return None
                return DokuwikiBackend.get_update_user(username, l)

        # User doesn't exists in dokuwiki password files
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
