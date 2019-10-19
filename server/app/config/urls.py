from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls import url

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path("api/", include("app.api.urls")),
    url(r'^.*$', TemplateView.as_view(template_name="index.html"), name="home"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
