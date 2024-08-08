from django.urls import path
from . import views

urlpatterns = [
    path("home", views.index, name = "HomePage"),
    path("blogs", views.Blogs, name = "Blogs"),
    path("<str:bslug>", views.ReadBlogs, name = "ReadBlogs"),
    path("comment/<str:comsl>", views.Comment, name = "Comment"),
    path("cat/<str:catl>", views.Category, name = "Category"),
]