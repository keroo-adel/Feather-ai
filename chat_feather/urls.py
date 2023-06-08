from django.urls import path
from . import views

urlpatterns = [
    path('', views.ChatFeatherView.as_view(), name='chat_feather'),
    path('delete_chat/<int:chat_id>/', views.DeleteChatView.as_view(), name='delete_chat'),
    path('update_chat_name/<int:chat_id>/', views.UpdateChatNameView.as_view(), name='update_chat_name'),
    path('update_active_chat/<int:chat_id>/', views.UpdateActiveChatView.as_view(), name='update_active_chat'),
    path('send_message/', views.SendMessageView.as_view(), name='send_message'),

]