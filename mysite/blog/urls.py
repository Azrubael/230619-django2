from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # host views
    # path('', views.post_list, name='post_list'),
    path('', views.PostListView.as_view(), name='post_list'),
    # exapmle of a simple router
    # path('<int:id>/', views.post_detail, name='post_detail'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name='post_detail'),
]