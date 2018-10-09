from django.urls import path
from . import views
app_name = 'resume'
urlpatterns = [
    #path('',views.my_profile,name='my_profile'),
    path('',views.index, name='about'),
    path('experience',views.experience, name='experience'),
    path('portfolio',views.portfolio, name='portfolio'),
    path('skills',views.skills, name='skills'),
    path('awards',views.awards, name='awards'),
    path('contact',views.emailView, name='contact'),

]
