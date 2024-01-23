from blogging.models import Post, Category
from django.contrib import admin


# and a new admin registration
admin.site.register(Post)
admin.site.register(Category) 