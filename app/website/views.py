from decimal import Decimal

from django.contrib import messages
from django.shortcuts import render, get_object_or_404, reverse, HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _

from app.company.models import Quotation
from app.lawyer.models import Lawyer, Proposal
from utils.decorators import user_lawyer_required
from utils.paginator import listing


def index(request):
    ctx = {
        'total_lawyers': Lawyer.objects.all().count(),
        'quotations': Quotation.objects.filter(state='created').order_by('-created_date')[:4],
    }
    return render(
        request,
        'website/index.html',
        ctx
    )


def quotations(request):
    ctx = {
        'quotations': listing(request, Quotation.objects.filter(state='created'), 12),
        'title': _('Quotations')
    }
    return render(
        request,
        'website/quotations.html',
        ctx
    )


@user_lawyer_required
def quotation(request, pk):
    o_quotation = get_object_or_404(Quotation, pk=pk)
    # get logged lawyer
    lawyer = request.user.lawyer
    # get lawyer proposal or false
    try:
        lawyer_proposal = Proposal.objects.get(quotation=o_quotation, lawyer=lawyer)
    except Proposal.DoesNotExist:
        lawyer_proposal = False
    if request.method == 'POST':
        proposal_value = Decimal(request.POST.get('proposal_value'))
        if proposal_value > 0:
            Proposal.objects.create(
                quotation=o_quotation,
                lawyer=lawyer,
                price=proposal_value
            )
            messages.success(request, _('Thanks for send your proposal.'))
            return HttpResponseRedirect(
                reverse('website:quotation', kwargs={'pk': o_quotation.pk})
            )
        else:
            messages.error(request, _('Invalid value.'))
    ctx = {
        'quotation': o_quotation,
        'lawyer_proposal': lawyer_proposal,
        'title': _('Quotation')
    }
    return render(
        request,
        'website/quotation.html',
        ctx
    )
