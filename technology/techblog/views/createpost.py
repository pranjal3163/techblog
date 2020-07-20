# creating new posts
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

from techblog.models.post import Post


class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
