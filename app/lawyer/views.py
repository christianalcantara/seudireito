from django.shortcuts import render
from . forms import LawyerCreationForm
from django.utils.translation import ugettext_lazy as _
from utils.paginator import listing


def createaccount(request):
    if request.method == 'POST':
        form = LawyerCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = LawyerCreationForm()

    ctx = {
        'title': _("Create Account"),
        'form': form
    }
    return render(
        request,
        'lawyer/create-account.html',
        ctx
    )


def proposals(request):
    lawyer = request.user.lawyer
    ctx = {
        'proposals': listing(request, lawyer.proposals.all(), 10)
    }
    return render(
        request,
        'lawyer/proposals.html',
        ctx
    )
