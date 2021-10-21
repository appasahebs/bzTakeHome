from articles.models import Article
from django.views import generic
from django.db.models import Q


class IndexView(generic.ListView):
    template_name = 'list.html'
    context_object_name = 'artilce_list'
    model = Article

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Article.objects.filter(
                Q(title__icontains=query) |
                Q(tags__icontains=query))
        else:
            return Article.objects.all()
