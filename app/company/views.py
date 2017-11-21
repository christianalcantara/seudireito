from django.shortcuts import render
from . forms import CompanyCreationForm
from django.utils.translation import ugettext_lazy as _


def createaccount(request):
    if request.method == 'POST':
        form = CompanyCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CompanyCreationForm()

    ctx = {
        'title': _("Create Account"),
        'form': form
    }
    return render(
        request,
        'company/create-account.html',
        ctx
    )
