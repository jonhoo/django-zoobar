#!/usr/bin/python

import sys
import os
import urllib
import hashlib
import socket
import traceback
from io import StringIO
import zapp.views

## Cache packages that the sandboxed code might want to import
import time
import errno

class ProfileAPI():
    def __init__(self, user, visitor):
        self.user = user
        self.visitor = visitor

    def get_self(self):
        return self.user

    def get_visitor(self):
        return self.visitor

    def get_xfers(self, username):
        xfers = []

        try:
            user = User.objects.get(username = username)
            transfers = Transfer.objects.filter(Q(sender = user) | Q(recipient = user))

            for xfer in transfers:
                xfers.append({
                    'sender': xfer.sender,
                    'recipient': xfer.recipient,
                    'amount': xfer.amount,
                    'time': xfer.time
                })

        except User.DoesNotExist:
            print("User not found")

        return xfers

    def get_user_info(self, username):
        try:
            user = User.objects.get(username = username)

            return {
                'username': user.person.user.username,
                'profile': user.person.profile,
                'zoobars': user.person.zoobars
            }
        except User.DoesNotExist:
            print("User not found")

        return {}

    def xfer(self, target, zoobars):
        views.transfer_impl(self.user, target, zoobars)

def run_profile(user, visitor):
    try:
        pcode = user.person.profile.encode('ascii', 'ignore')
        pcode = pcode.replace('\r\n', '\n')

        uid = 0
        profile_api_client = ProfileAPI(user, visitor)
        stdout = sys.stdout
        result = StringIO.StringIO()
        sys.stdout = result
        exec(pcode) in {'api': profile_api_client}
        sys.stdout = stdout
        return result.getvalue()

    except e:
        traceback.print_exc()
        return 'Exception: ' + str(e)


