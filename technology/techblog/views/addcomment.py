from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView

from techblog.forms import CommentForm
from techblog.models.post import Post


class AddComment(TemplateView):
# create a message form
    def add_comment(request, pk):
        post = get_object_or_404(Post, pk=pk)
        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.save()
                return redirect('blog_post_detail', pk=post.pk)
            else:
                form = CommentForm()
        return render(request, 'techblog/comments_form.html', {'form': form})
