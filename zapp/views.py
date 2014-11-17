from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseNotFound
from zapp.models import Person, Transfer
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from zapp.profile import run_profile

@login_required
def index(request):
    try:
        request.user.person.profile = request.POST['profile_update']
        request.user.person.save()
    except KeyError:
        pass
    return render(request, 'zapp/index.html', {'user': request.user})

@login_required
def transfer(request):
    try:
        recipient = request.POST['recipient']
        zoobars = symint(request.POST['zoobars'])

        transfer_impl(request.user, recipient, zoobars)

        return render(request, 'zapp/transfer.html', {
            'warning': 'Sent %d zoobars' % zoobars
        })

    except KeyError:
        return render(request, 'zapp/transfer.html')
    except (User.DoesNotExist, ValueError):
        return render(request, 'zapp/transfer.html', {
            'warning': 'Transfer to %s failed' % request.POST['recipient']
        })

def transfer_impl(sender, recipient, zoobars):
    try:
        recipientp = User.objects.get(username = recipient)

        sender_balance = sender.person.zoobars - zoobars
        recipient_balance = recipientp.person.zoobars + zoobars

        if sender_balance < 0 or recipient_balance < 0:
            raise ValueError()

        sender.person.zoobars = sender_balance
        recipientp.person.zoobars = recipient_balance
        sender.person.save()
        recipientp.person.save()

        transfer = Transfer()
        transfer.sender = sender.person
        transfer.recipient = recipientp.person
        transfer.amount = zoobars
        transfer.save()
    except User.DoesNotExist:
        raise User.DoesNotExist()


@login_required
def users(request):
    try:
        req_user = request.GET['user']
        try:
            user = User.objects.get(username = req_user)
            transfers = Transfer.objects.filter(Q(sender = user) | Q(recipient = user))

            if user.person.has_executable_profile():
                user.person.profile = run_profile(user, req_user)

            return render(request, 'zapp/users.html', {
                'req_user': req_user,
                'user': user,
                'transfers': transfers
            })
        except User.DoesNotExist:
            return render(request, 'zapp/users.html', {
                'req_user': req_user,
                'warning': 'Cannot find that user.'
            })
    except KeyError:
        return render(request, 'zapp/users.html', {'req_user':''})

@login_required
def zoobarjs(request):
    return render(request, 'zapp/zoobars.js', {'user': request.user})

