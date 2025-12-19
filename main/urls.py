from django.urls import path

from views import ArticleAPIView, PostAPIView, BookAPIView, AuthorAPIView

urlpatterns = [
    path('', AuthorAPIView.as_view)
    path()
]