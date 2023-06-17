from django.views.generic import ListView, CreateView,View
from .models import Block
import uuid
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Block2 as Block , Article
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
import json


class LongFormEditorView(LoginRequiredMixin,CreateView):
    template_name = 'long form editor/Long-form-editor.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    
class SaveArticleTitleView(View):
    def post(self, request, *args, **kwargs):
        title = request.POST.get('article_title')
        
        # Create a new article with the provided title
        article = Article(title=title)
        article.save()

        self.request.session['article_id'] = article.id
        return JsonResponse({'success': True})

    def get(self, request, *args, **kwargs):
        return JsonResponse({'success': False, 'error': 'Invalid request method'})


class CreateBlockView(View):
    def post(self, request, *args, **kwargs):
        content = request.POST.get('content')
        block_type = request.POST.get('block_type')
        position = int(request.POST.get('position'))

        # Get the current article ID from the request
        article_id = self.request.session.get('article_id')

        try:
            # Fetch the article based on the provided ID
            article = Article.objects.get(id=article_id)

            # Create a new block associated with the article
            block = Block(article=article, content=content, block_type=block_type, position=position)
            block.save()

            return JsonResponse({'success': True})
        except ObjectDoesNotExist:
            return JsonResponse({'success': False, 'error': 'Article does not exist'}, status=404)

    def get(self, request, *args, **kwargs):
        return JsonResponse({'success': False, 'error': 'Invalid request method'})
    
class AskFeatherView(View):
    def post(self, request, *args, **kwargs):
        try:
            payload = json.loads(request.body)
            question = payload.get('question')

            response = {
                'question': question,
                'answer': 'This is the answer to your question.',
            }

            return JsonResponse(response)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON payload'})

    def get(self, request, *args, **kwargs):
        return JsonResponse({'error': 'Invalid request method'})