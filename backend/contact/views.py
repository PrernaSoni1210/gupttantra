from django.shortcuts import render
from .models import ContactMessage


def contact_page(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        consultation_type = request.POST.get("consultation_type")
        message = request.POST.get("message")

        ContactMessage.objects.create(
            name=name,
            email=email,
            phone=phone,
            consultation_type=consultation_type,
            message=message
        )

        return render(request, "contact/contact.html", {
            "success": True
        })

    return render(request, "contact/contact.html")