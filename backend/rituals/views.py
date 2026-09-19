from django.shortcuts import render
from .models import Ritual


def rituals_list(request):

    rituals = Ritual.objects.all().order_by('-created_at')

    return render(
        request,
        'rituals/rituals.html',
        {
            'rituals': rituals
        }
    )