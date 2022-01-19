### 使用原生view
from django.urls import path
from snippets.views import original_views
# urlpatterns = [
    # path('snippets/', original_views.snippet_list),
    # path('snippets/<int:pk>/', original_views.snippet_detail),

# ]


# 使用apiView
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets.views import api_views

urlpatterns = [
    path('snippets/', api_views.SnippetList.as_view()),
    path('snippets/<int:pk>/', api_views.SnippetDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
