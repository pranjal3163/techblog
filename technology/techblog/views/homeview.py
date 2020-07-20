from django.views.generic import (ListView)
from techblog.models.post import Post


class HomeView(ListView):
    model = Post
    context_object_name = 'posts'
    # to order the post from latest to oldest
    ordering = ['-date']
    paginate_by = 4

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            posts = self.model.objects.filter(title__icontains=query)
        else:
            posts = self.model.objects.all()
        return posts
