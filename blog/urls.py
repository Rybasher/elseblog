from django.conf.urls import url
from .views import *
from django.urls import path

urlpatterns = [
    path('', posts_list),
    path('blog/', hello),

]