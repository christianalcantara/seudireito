from django.shortcuts import render
from . forms import LawyerCreationForm
from django.utils.translation import ugettext_lazy as _


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
