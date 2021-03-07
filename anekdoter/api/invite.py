import random
import string

from django.http.response import HttpResponse
from models.models import Invite


def generate_invite():
    invite = ''
    for _ in range (10):
        invite += random.choice(string.ascii_letters)
    return invite


def init_invites(request):
    for _ in range(10):
        t = Invite.objects.create(code=generate_invite())
        t.save()
    return HttpResponse('<h1>created</h1>', status=201)
