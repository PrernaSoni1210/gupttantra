from django.shortcuts import render
from .models import Service


def services_list(request):

    services = Service.objects.all().order_by('-created_at')

    return render(
        request,
        'services/services.html',
        {
            'services': services
        }
    )