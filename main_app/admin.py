from django.contrib import admin
from .models import Categoria,Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('titulo','autor','published_date','categoria')
    list_filter=('titulo','categoria','autor','published_date')
    list_editable=('categoria',)
    search_fields=('titulo',)
    list_per_page=10
    date_hierarchy = "published_date"

