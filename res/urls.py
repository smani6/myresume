from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from views import *

urlpatterns = [
 	url(r'^$', Resume.as_view(), name='login'),
 	url(r'^download/$', Download.as_view(), name='dashboard'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)