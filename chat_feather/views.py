from django.views.generic import ListView,View
from django.shortcuts import render, redirect
from .models import Chat, Message, Response
# from .ai_model import load_ai_model  # Replace with the code to load your AI model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from urllib.parse import unquote
import json
    
class ChatFeatherView(LoginRequiredMixin,ListView):
    template_name = 'chat_feather/chat-feather.html'

    def get(self, request):

        chats = Chat.objects.filter(user=request.user).order_by('-timestamp')
        messages = Message.objects.filter(chat__in=Chat.objects.filter(user=request.user, active=True))
        responses = Response.objects.filter(message__in=messages)
        message_response_pairs = list(zip(messages, responses))
        active_chat_id  = Chat.objects.filter(user=request.user, active=True)
        has_message_response_pairs = len(message_response_pairs) > 0
        return render(request, self.template_name, {
            'chats': chats,
            'message_response_pairs': message_response_pairs, 
            'active_chat_id': active_chat_id,
            'has_message_response_pairs': has_message_response_pairs,
            })
        

    def post(self, request):
        if 'new_chat' in request.POST:
            chat_name = request.POST.get('chat_name')
            if chat_name == '':
                chat_name = 'chat_' + str(len(Chat.objects.filter(user=request.user)) + 1)
            chat = Chat.objects.create(user=request.user, name=chat_name)
            Chat.objects.all().update(active=False)
            Chat.objects.filter(user=request.user, name=chat_name).update(active=True)
           
            return redirect('chat_feather')
    
class DeleteChatView(View):
    def post(self, request, chat_id):
        chat = Chat.objects.get(pk=chat_id)
        chat.delete()
        return redirect('chat_feather')
    
class UpdateChatNameView(View):
    def post(self, request, chat_id):
        new_name = request.POST.get('new_name')
        chat = Chat.objects.get(pk=chat_id)
        chat.name = new_name
        chat.save()
        return redirect('chat_feather')

class UpdateActiveChatView(View):
    def post(self, request, chat_id):
        # Update the active state of the chats
        Chat.objects.all().update(active=False)
        chat = Chat.objects.get(id=chat_id)
        chat.active = True
        chat.save()
    
        return redirect('chat_feather')  
    
class SendMessageView(LoginRequiredMixin, View):
    def post(self, request):
        data = json.loads(request.body)
        chat_id = data.get('chat_id')
        message_content = data.get('message')

        try:
            chat = Chat.objects.get(pk=chat_id)
        except Chat.DoesNotExist:
            chat = Chat.objects.create(user=request.user, name='new_chat', active=True)

        message = Message.objects.create(chat=chat, content=message_content)

        # Ai model response
        ai_response = "Ai model say hello"

        response = Response.objects.create(message=message, content=ai_response)

        return HttpResponse(ai_response, content_type="text/plain")
    
