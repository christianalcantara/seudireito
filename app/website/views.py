from django.shortcuts import render
from app.lawyer.models import Lawyer


def index(request):
    ctx = {
        'total_lawyers': Lawyer.objects.all().count()
    }
    return render(
        request,
        'website/index.html',
        ctx
    )
