from django import template

from techblog.models.post import Post

register = template.Library()
@register.inclusion_tag('techblog/sidebars.html')
def sidebar_results():
    posts = Post.objects.all().order_by('-date')[:5]
    # context = {
    #     'new_post': post
    # }
    # return render(request, 'blogapp/sidebars.html', context)
    return {'posts': posts}
