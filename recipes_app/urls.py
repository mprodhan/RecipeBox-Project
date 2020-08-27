from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from recipes_app import views

urlpatterns = [
    path("", views.index, name="homepage"), 
    path("add_recipe/", views.recipesadd), 
    path("add_author/", views.authoradd),
    path("recipe/<int:id>/", views.recipe_view),
    path("bio/<int:id>/", views.author_view),
    path("image/", views.imageadd),
    path("success/", views.success, name="success")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT)