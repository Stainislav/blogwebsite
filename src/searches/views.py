from django.shortcuts import render
from .models import SearchQuery
from blog.models import BlogPost


def search_view(request):

    query = request.GET.get('q', None)
    user = None

    if request.user.is_authenticated:
        user = request.user

    context = {"query": query}
    template_name = 'searches/view.html'

    if query is not None:
        SearchQuery.objects.create(user=user, query=query)
        blog_list = BlogPost.objects.search(query=query)
        context['blog_list'] = blog_list

    return render(request, template_name, context)
