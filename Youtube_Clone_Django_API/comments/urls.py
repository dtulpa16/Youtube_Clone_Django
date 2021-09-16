from django.urls import path
from . import views

urlpatterns = [
    path('comment/', views.CommentList.as_view()),
    path('comment/<int:pk>/', views.CommentDetail.as_view()),
    path('comment/<str:video_Id>/video/', views.CommentVideo.as_view()),
    path('reply/', views.ReplyList.as_view()),
    path('comment/<int:comment_Id>/reply/', views.ViewReply.as_view())
]