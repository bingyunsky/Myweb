from django.conf.urls import include, url
from django.contrib import admin
from DjangoUeditor import urls as DjangoUeditor_urls
from django.conf import settings

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^ueditor/', include(DjangoUeditor_urls))
]


if settings.DEBUG:
	form django.conf.urls.static import static
	urlpatterns +=static(
		settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)