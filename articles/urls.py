from django.urls import path
from articles import views

urlpatterns = [
    path('', views.ArticleView.as_view(), name='Article_View'),
    path('feeds/',views.FeedView.as_view(), name='feed_view'),
    path('<int:article_id>/', views.ArticleDetailView.as_view(), name="Article_DetailView"),
    path('<int:article_id>/comment/', views.CommentView.as_view(), name='Comment_View'),
    path('<int:comment_id>/', views.CommentDetailView.as_view(), name="Comment_DetailView"),
    path('<int:article_id>/like/', views.LikeView.as_view(), name='Like_View'),
]