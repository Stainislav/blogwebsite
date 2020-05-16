from django.shortcuts import render
from .forms import ContactForm
from blog.models import BlogPost


def home_page(request):

    home = BlogPost.objects.get(slug="home_slug")
    context = {'me': home}
    template_name = "home.html"

    return render(request, template_name, context)


def projects_view(request):

    project = BlogPost.objects.get(slug="calc_slug")
    template_name = "projects.html"
    title = "My projects"
    context = {'title': title, "project": project}

    return render(request, template_name, context)

