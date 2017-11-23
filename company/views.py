from django.contrib import messages
from django.shortcuts import render, reverse, HttpResponseRedirect, get_object_or_404
from django.utils.translation import ugettext_lazy as _

from lawyer.models import Proposal
from utils.decorators import user_company_required
from utils.paginator import listing
from .forms import CompanyCreationForm, QuotationCreateForm
from .models import Quotation


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


@user_company_required
def quotations(request):
    company = request.user.company
    ctx = {
        'title': _('Your quotations'),
        'quotations': listing(request, company.quotations.all(), 10)
    }
    return render(
        request,
        'company/quotations.html',
        ctx
    )


@user_company_required
def quotation_create(request):
    company = request.user.company
    if request.method == 'POST':
        form = QuotationCreateForm(request.POST)
        if form.is_valid():
            new_quotation = form.save(commit=False)
            new_quotation.company = company
            new_quotation.save()
            messages.success(request, _("Quotation '{}' created successfully").format(new_quotation.title))
            return HttpResponseRedirect(reverse('company:quotations'))
    else:
        form = QuotationCreateForm()

    ctx = {
        'title': _('Create quotation'),
        'form': form
    }
    return render(
        request,
        'company/quotation-create.html',
        ctx
    )


@user_company_required
def quotation_proposals(request, pk):
    o_quotation = get_object_or_404(Quotation, pk=pk)
    company = request.user.company

    if request.method == 'POST':
        action = request.POST.get('action')
        proposal_pk = request.POST.get('pk')
        proposal = Proposal.objects.get(pk=proposal_pk)
        if action == 'finish':
            o_quotation.state = 'finished'
            o_quotation.save()
            messages.success(request, _("Quotation '{}' finished").format(o_quotation))
        elif action == 'delegate':
            o_quotation.delegated_to = proposal
            o_quotation.state = 'delegate'
            o_quotation.save()
            messages.success(request, _("Proposal '{}' delegate").format(proposal))
        return HttpResponseRedirect(reverse('company:quotations'))

    ctx = {
        'title': _('Quotation proposals'),
        'quotation': o_quotation,
        'proposals': listing(request, o_quotation.proposals.all().order_by('price'))
    }
    return render(
        request,
        'company/quotation-proposal.html',
        ctx
    )
