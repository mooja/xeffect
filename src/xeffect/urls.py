from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import profiles.urls
import accounts.urls
import habits.urls
from . import views


from rest_framework.routers import DefaultRouter

from habits.views import HabitViewSet


router = DefaultRouter()
router.register('habits', HabitViewSet)


urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^habits/', include(habits.urls, namespace='habits')),
    url(r'^about/$', views.AboutPage.as_view(), name='about'),
    url(r'^users/', include(profiles.urls, namespace='profiles')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^', include(accounts.urls, namespace='accounts')),
]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
