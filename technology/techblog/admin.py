from django.contrib import admin
from techblog.models.post import Post
from techblog.models.comments import Comments

admin.site.register(Post)
admin.site.register(Comments)
