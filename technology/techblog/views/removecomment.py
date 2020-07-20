from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView

from techblog.models.comments import Comments


class RemoveComment(TemplateView):
    @login_required
    def comment_remove(request, pk):
        comment = get_object_or_404(Comments, pk=pk)
        comment.delete()
        return redirect('blog_post_detail', pk=comment.post.pk)
