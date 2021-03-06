from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:event_id>/', views.detail, name='event-detail'),
    path('accounts/profile/', views.profile, name='profile'),
    path('create/',views.create_event, name='create-event'),
    path('delete/<int:event_id>/', views.delete_event, name='delete-event'),
    path('signup/', views.signup, name='signup'),
    path('', include('django.contrib.auth.urls')),
    path('join/<int:event_id>/', views.join_event, name='join-event'),
    path('leave/<int:event_id>/', views.leave_event, name='leave-event'),
    path('', include('social_django.urls', namespace='social')),
    path('logout/',views.logout,name='logout'),
    path('<str:username>/history/', views.event_history, name='event-history')
] 

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

