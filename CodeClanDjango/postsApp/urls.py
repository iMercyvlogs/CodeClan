from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns=[
    path('',views.post_list,name="post_list_url"),
    path('<slug:my_slug>/',views.post_detail, name="post_detail_url"),
    #<slug:my_slug> is a path converter that captures a string consisting of ASCII letters, numbers, hyphens, or underscores and assigns it to the variable my_slug. 
    #path('<int:postObj_id>/',views.post_detail, name="post_detail_url"),
]
