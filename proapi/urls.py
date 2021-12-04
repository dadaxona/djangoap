from django.urls import path
from .views import IndexPageView, HomePageView, CreatePageView, EditPageView, DeletePageView, ApiPageView, PostList,\
    PostDetail

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('home/',HomePageView.as_view(),name='home'),
    path('create/', CreatePageView.as_view(), name='create'),
    path('post/<int:pk>/edit', EditPageView.as_view(), name='edit'),
    path('post/<int:pk>/delete', DeletePageView.as_view(), name='delete'),
    path('api/', ApiPageView.as_view(), name='api'),
    path('', PostList.as_view()),
    path('<int:pk>/', PostDetail.as_view()),

]