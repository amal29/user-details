
from django.urls import path
from user import views
urlpatterns = [
    path('show',views.show,name='show'),
    path('',views.home,name="home"),
    path('view',views.view,name='view'),
    path('paginationapi',views.paginationapi,name="paginationapi")


]

