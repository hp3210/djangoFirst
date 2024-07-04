from django.urls import path
from. views import *

# urlpatterns = [
#     path('',views.home,name='home'),
# ]
urlpatterns =[
    path('test/',test,name='test'),
    path('testpg/',testPage,name='testPage'),
]
