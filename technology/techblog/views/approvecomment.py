from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView

from techblog.models.comments import Comments


class ApproveComment(TemplateView):
    @login_required
    def comment_approve(request, pk):
        comment = get_object_or_404(Comments, pk=pk)
        comment.approve()
        return redirect('blog_post_detail', pk=comment.post.pk)
