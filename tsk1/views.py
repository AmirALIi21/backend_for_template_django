from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Creator, Experience, Project, Contact, SocialLink, About

def index(request):
    creator = Creator.objects.get(is_active=True)
    experiences = Experience.objects.filter(is_active=True)
    projects = Project.objects.filter(is_active=True)
    contacts = Contact.objects.get()
    social_links = SocialLink.objects.all()
    about = About.objects.get()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone',)
        message = request.POST.get('message')

        # Validate the form data
        if name and email and message:
            send_mail(
                'New Contact Form Submission',
                f'Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}',
                email,  
                ['21amirali2112@gmail.com'],  # Replace with the recipient's email address
            )

            # Redirect after successful submission
            return HttpResponseRedirect(reverse('index'))
    context = {
        'creator': creator,
        'experiences': experiences,
        'projects': projects,
        'contacts': contacts,
        'social_links': social_links,
        'about': about,
    }

    return render(request, 'index.html', context)
