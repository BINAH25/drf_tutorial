from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_home, name='api_home'),
    path('advocate', views.advocate_list ),
    path('advocate/<str:username>', views.advocate_detail),
    path('company', views.company_list ),

]
