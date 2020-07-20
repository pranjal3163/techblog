from django.urls import path, re_path
from django.views.generic import TemplateView
from techblog.views.homeview import HomeView
from techblog.views.about import About
from techblog.views.userpostview import UserPostView
from techblog.views.postdetails import PostDetails
from techblog.views.createpost import CreatePost
from techblog.views.postupdate import PostUpdate
from techblog.views.postdelete import PostDelete
from techblog.views.addcomment import AddComment
from techblog.views.approvecomment import ApproveComment
from techblog.views.removecomment import RemoveComment
from techblog.views.updatecomment import UpdateComment

# urlpatterns = [
#     #re_path(r'^$', TemplateView.as_view(template_name='techblog/index.html'), name='home'),
#     path('', Blog_List.post_list, name='post_list'),
#     path('post/<int:pk>/', Post_Details.post_detail, name='post_detail'),
# ]

urlpatterns = [
    path('', HomeView.as_view(), name='techblog-home'),
    path('about/', About, name='techblog-about'),
    path('<str:username>/', UserPostView.as_view(), name='users_blog'),
    path('post/<int:pk>/', PostDetails.as_view(), name='blog_post_detail'),
    path('post/create/', CreatePost.as_view(), name='blog-post-create'),
    path('post/<int:pk>/update', PostUpdate.as_view(), name='blog-post-update'),
    path('post/<int:pk>/delete', PostDelete.as_view(), name='blog-post-delete'),
    path('post/<int:pk>/comment/', AddComment.add_comment, name='add_comments'),
    path('comment/<int:pk>/approve/', ApproveComment.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', RemoveComment.comment_remove, name='comment_remove'),
    path('comment/<int:pk>/edit/', UpdateComment.comment_update, name='comment_edit'),
]

