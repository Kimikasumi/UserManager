from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('documents/', views.getdocumenttypelist, name='getdocumenttypelist'),
    path('city/', views.getcitylist, name='getcitylist'),
    path('users/', views.getuserslist, name='getuserslist'),
    path('users/create/', csrf_exempt(views.createuser), name='createuser'),
    path('<int:user_id>/users/edit/', csrf_exempt(views.updateuser), name='updateuser'),
    path('<int:user_id>/users/delete/', views.deleteuser, name='deleteuser'),
]