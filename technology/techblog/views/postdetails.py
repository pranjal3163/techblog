from django.views.generic import DetailView
from techblog.models.post import Post


class PostDetails(DetailView):
    model = Post
