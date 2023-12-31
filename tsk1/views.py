from django.shortcuts import render
from .models import Creator, Experience, Project, Contact, SocialLink, About

def index(request):
    creator = Creator.objects.get(is_active=True)
    experiences = Experience.objects.filter(is_active=True)
    projects = Project.objects.filter(is_active=True)
    contacts = Contact.objects.get()
    social_links = SocialLink.objects.all()
    about = About.objects.get()

    context = {
        'creator': creator,
        'experiences': experiences,
        'projects': projects,
        'contacts': contacts,
        'social_links': social_links,
        'about': about,
    }

    return render(request, 'index.html', context)
