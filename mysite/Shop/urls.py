from django.urls import path
from .views import TaskViewSet, CategoryViewSet

urlpatterns = [
    path('', CategoryViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='category_list'),

    path('category/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='category_detail'),

    path('task/', TaskViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='task_list'),

    path('task/<int:pk>/', TaskViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='task_detail'),

    # path('account/signup/', CustomSignupView.as_view(), name='signup'),
]