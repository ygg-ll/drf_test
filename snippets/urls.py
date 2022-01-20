### 使用原生view
from django.urls import path
from snippets.example_views import original_views
# urlpatterns = [
# path('snippets/', original_views.snippet_list),
# path('snippets/<int:pk>/', original_views.snippet_detail),

# ]


# 使用apiView
# from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
# from snippets.example_views import api_views
#
# urlpatterns = [
#     path('snippets/', api_views.SnippetList.as_view()),
#     path('snippets/<int:pk>/', api_views.SnippetDetail.as_view()),
# ]
# urlpatterns = format_suffix_patterns(urlpatterns)


# # 使用minxin
# from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
# from snippets.example_views import mixin_views
#
# urlpatterns = [
#     path('snippets/', mixin_views.SnippetList.as_view()),
#     path('snippets/<int:pk>/', mixin_views.SnippetDetail.as_view()),
# ]
# urlpatterns = format_suffix_patterns(urlpatterns)


# 使用 generics
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets.example_views import generics_views
from snippets import views

# urlpatterns = [
#     path('snippets/', generics_views.SnippetList.as_view()),
#     path('snippets/<int:pk>/', generics_views.SnippetDetail.as_view()),
#
#     path('users/', views.UserList.as_view()),
#     path('users/<int:pk>/', views.UserDetail.as_view()),
#
#     # 这个接口有问题https://www.django-rest-framework.org/tutorial/5-relationships-and-hyperlinked-apis/
#     # path('', generics_views.api_root),
#     path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view()),
#
# ]
# urlpatterns = format_suffix_patterns(urlpatterns)


# from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
# from snippets import views
#
# # API endpoints
# urlpatterns = format_suffix_patterns([
#     # path('', views.api_root),
#     path('snippets/', generics_views.SnippetList.as_view(), name='snippet-list'),
#     path('snippets/<int:pk>/', generics_views.SnippetDetail.as_view(), name='snippet-detail'),
#     path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'),
#     path('users/', views.UserList.as_view(), name='user-list'),
#     path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail')
# ])


### 简化路由
# from snippets.views import SnippetViewSet, UserViewSet, api_root
# from rest_framework import renderers
#
# snippet_list = SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# snippet_detail = SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# snippet_highlight = SnippetViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })
#
# urlpatterns = format_suffix_patterns([
#     path('', api_root),
#     path('snippets/', snippet_list, name='snippet-list'),
#     path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
#     path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
#     path('users/', user_list, name='user-list'),
#     path('users/<int:pk>/', user_detail, name='user-detail')
# ])

# 下面是简化写法
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]