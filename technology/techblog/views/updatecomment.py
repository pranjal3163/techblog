from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView

from techblog.forms import CommentForm
from techblog.models.comments import Comments


class UpdateComment(TemplateView):
    def comment_update(request, pk, template_name='techblog/comments_form.html'):
        comment = get_object_or_404(Comments, pk=pk)
        form = CommentForm(request.POST or None, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('blog_post_detail', pk=comment.post.pk)
        return render(request, template_name, {'form': form})
