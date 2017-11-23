from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.utils.translation import ugettext_lazy as _

from utils.decorators import user_lawyer_required
from utils.paginator import listing
from .forms import LawyerCreationForm


def createaccount(request):
    if request.method == 'POST':
        form = LawyerCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('Account created successfully'))
            return HttpResponseRedirect(reverse('website:index'))
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


@user_lawyer_required
def proposals(request):
    lawyer = request.user.lawyer
    ctx = {
        'proposals': listing(request, lawyer.proposals.all(), 10),
        'title': _('Proposals')
    }
    return render(
        request,
        'lawyer/proposals.html',
        ctx
    )
