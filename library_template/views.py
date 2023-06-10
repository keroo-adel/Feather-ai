from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse

class AiArticleWriterView(LoginRequiredMixin,ListView):
    template_name = 'ai_article_writer/aIArticleWriter.html'
    
    def get(self, request):
        # Render the keywords selection template
        return render(request, self.template_name)
    
    def post(self, request):
        message = request.POST.get('message') 
        
        keywords = {'keyword1', 'keyword2', 'keyword3'}
        keyword_list = list(keywords)
        
        if message:
            return render(request, 'ai_article_writer/keywords.html', 
                          {'keywordslist': keyword_list, 
                           'message': message
                                            })

        return render(request, self.template_name)
        

class EmailToolsView(LoginRequiredMixin,ListView):
    template_name = 'email_tools/emailTool.html'
    
    def get(self, request):
        return render(request, self.template_name)
    
class SocialMediaToolsView(LoginRequiredMixin,ListView):
    template_name = 'social_media_tools/socialMediaTool.html'
    
    def get(self, request):
        return render(request, self.template_name)