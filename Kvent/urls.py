from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:event_id>/', views.detail, name='event-detail')
    path('profile', views.profile, name='profile'),
    path('create',views.create_event, name='create-event'),
]

