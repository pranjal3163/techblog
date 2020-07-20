from django.views.generic import (ListView)
from techblog.models.post import Post
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User


class UserPostView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'techblog/user_posts.html'
    paginate_by = 4

    def get_queryset(self):
        # v try to get the user when v click link on author name in post list
        # to get that user object v do self.kwargs.get('username')
        # self.kwargs is a dictionary of that user datas, and v use get method to fetch username of that user from that dictionary
        # here if user exists in User model v store it in user variable else, return 404 error
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        # now filter the post list based on author and order it by date.
        return Post.objects.filter(author=user).order_by('-date')
