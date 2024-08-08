from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from OrcaBlogs import settings
from django.conf.urls import handler400, handler403, handler404, handler500
from django.views.generic.base import RedirectView

urlpatterns = [
    path('orcablogsAdminDBforHarA', admin.site.urls),
    path('', include("OrcaBlogsWebsite.urls")),
    path('', RedirectView.as_view(url='/home', permanent=False)),
    re_path(r'^MediaFiles/(?P<path>.*)$', serve, {'document_root' : settings.MEDIA_ROOT})
]

handler404 = "OrcaBlogsWebsite.views.ErrorPage"
handler500 = "OrcaBlogsWebsite.views.ErrorOccured"
handler403 = "OrcaBlogsWebsite.views.ErrorPage"
handler400 = "OrcaBlogsWebsite.views.ErrorPage"
admin.site.site_title = "OrcaBlogs"
admin.site.site_header = "OrcaBlogs"
admin.site.index_title = "Welcome to OrcaBlogs's Admin panel..."