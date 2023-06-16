from django.shortcuts import render
from django.views.generic import ListView,View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from .models import *
import json
from django.http import HttpResponse
from django.shortcuts import redirect,get_object_or_404
from .utils import *
from django.contrib.auth.models import User
from recent_activity.models import RecentActivity
from django.contrib import messages
from django.urls import reverse



############################### 
# AiArticleWriter template
############################### 
class AiArticleWriterView(LoginRequiredMixin,ListView):
    template_name = 'ai_article_writer/aIArticleWriter.html'
    
    def get(self, request):
        # Render the keywords selection template
        return render(request, self.template_name)
    
    def post(self, request):
        message = request.POST.get('message') 
        #replace ai this with ai model answer 
        # send this message to the model:
        
        # keywords = ai_model("""genreate only {} keywords with this format 
        # {"keyword1","keryword2",......tec}""".
        # format(message))

        keywords = {"Lionel Messi", "football", "Barcelona"}
        keyword_list = list(keywords)
        
        if message:
            return render(request, self.template_name, 
                          {'keywordslist': keyword_list, 
                           'message': message})

        return render(request, self.template_name)
class SaveTopicKeywordsView(View):
    template_name = 'ai_article_writer/aIArticleWriter-step-2.html'
    def post(self, request):
        data = json.loads(request.body)
        keywords = data.get('keywords', [])
        topic_name = data.get('topicName', None)
        
        keywords_string = ', '.join(keywords)
        # Save the topic name and keywords to the Topic model
        topic = Topic.objects.create(name=topic_name, keywords=keywords_string)

        # Set session data
        request.session['topic_id'] = topic.id
        request.session['topic_name'] = topic_name
        request.session['keywords'] = keywords

        return JsonResponse({'success': True, 'topic_id': topic.id})

    def get(self, request):
        topic_id = request.session.get('topic_id')
        keywords = request.session.get('keywords', [])
        if topic_id:
            try:
                topic = Topic.objects.get(id=topic_id)
                topic_name = topic.name
                topic_keywords = topic.keywords.split(',') if topic.keywords else []

                context = {
                    'topic_name': topic_name,
                    'keywords': topic_keywords,
                }
                return render(request, self.template_name, context)
            except Topic.DoesNotExist:
                # Handle the case where the stored topic ID does not correspond to a valid topic
                del request.session['topic_id']
                del request.session['topic_name']
                del request.session['keywords']

        # Handle the case where the topic ID is not found in the session or the topic does not exist
        return render(request, 'ai_article_writer/topic_not_found.html')

class IdeasGenratorView(LoginRequiredMixin, ListView):
    template_name = 'ai_article_writer/aIArticleWriter-step-2.html'

    def get(self, request):
        topic_id = request.session.get('topic_id')
        if topic_id:
            try:
                topic = Topic.objects.get(id=topic_id)
                topic_name = topic.name
                topic_keywords = topic.keywords.split(',') if topic.keywords else []

                # Check if topic name or keywords in session differ from the database
                session_topic_name = request.session.get('topic_name')
                session_keywords = request.session.get('keywords')

                if session_topic_name and topic_name != session_topic_name:
                    topic.name = session_topic_name
                    topic.save()

                if session_keywords and topic_keywords != session_keywords:
                    topic.keywords = ','.join(session_keywords)
                    topic.save()

                context = {
                    'topic_name': topic.name,
                    'keywords': topic.keywords.split(',') if topic.keywords else [],
                    # Include any other data you want to pass to the template
                }
                return render(request, self.template_name, context)
            except Topic.DoesNotExist:
                # Handle the case where the stored topic ID does not correspond to a valid topic
                del request.session['topic_id']
                del request.session['topic_name']
                del request.session['keywords']

        # Handle the case where the topic ID is not found in the session or the topic does not exist
        return render(request, 'ai_article_writer/topic_not_found.html')
    
    def post(self, request):
        topic_name = request.session.get('topic_name')
        keywords = request.session.get('keywords', [])
        tone_of_voice = request.POST.get('tone_of_voice', None)
        language = request.POST.get('language', None)
        
        # replace this with ai resopnce model 
        
        # ideas = airesponse("""genrate ideas for article to {} and this keywords {} 
        # without any message by this form [idea1, idea2 , ....etc] with {} tone of 
        # voice and {} language""".format(topic_name, keywords, tone_of_voice, language))
        
        ideas = [
            "Lionel Messi's Unforgettable Moments at Barcelona: A Retrospective",
            "The Barcelona Legacy of Lionel Messi: An Era of Greatness",
            "The Journey of Lionel Messi: From Argentina to Barcelona",
            "Football Mastery: Analyzing Lionel Messi's Skills at Barcelona",
            
        ]

        context = {
            "generated_ideas": ideas,
            "tone_of_voice": tone_of_voice,
            "language": language,
            "topic_name": topic_name,
            "keywords": keywords,
        }
        return render(request, self.template_name, context)    
class SaveIdeasView(View):
    template_name = 'ai_article_writer/aIArticleWriter-step-3.html'
    def get(self, request):
        return render(request, self.template_name)
    def post(self, request):
        data = json.loads(request.body)
        selectedTone = data.get('selectedTone', None)
        selectedLanguage = data.get('selectedLanguage', None)
        selectedIdea = data.get('selectedIdea', None)
        

        
        # Save the topic name and keywords to the Topic model
        idea = Idea.objects.create(
            topic=Topic.objects.get(id=request.session['topic_id']),
            tone_of_voice=selectedTone,
            language=selectedLanguage,
            idea_text=selectedIdea
        )
        
        request.session['tone'] = selectedTone
        request.session['language'] = selectedLanguage
        request.session['idea'] = selectedIdea
        request.session['idea_id'] = idea.id

        return JsonResponse({'success': True,"tone": selectedTone, "language": selectedLanguage, "idea": selectedIdea})


class OutlinesGenratorView(LoginRequiredMixin,ListView):
    template_name = 'ai_article_writer/aIArticleWriter-step-3.html'

    def get(self, request):
        topic_name = request.session.get('topic_name')
        topic_keywords = request.session.get('keywords')
        selected_tone = request.session.get('tone')
        selected_language = request.session.get('language')
        selected_idea = request.session.get('idea')
        
            
        context = {
            "topic_name": topic_name,
            "topic_keywords": topic_keywords,
            "selected_tone": selected_tone,
            "selected_language": selected_language,
            "selected_idea": selected_idea,
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        topic_name = request.session.get('topic_name')
        topic_keywords = request.session.get('keywords')
        selected_tone = request.session.get('tone')
        selected_language = request.session.get('language')
        selected_idea = request.session.get('idea')
        select_individual_outlines = request.POST.get('select_individual', False)
        
        genrated_outlines_list = [

                    [
                    "Introduction",
                    "Messi's arrival at Barcelona",
                    "Early years and breakthrough",
                    "Messi's partnership with Ronaldinho",
                    "The Pep Guardiola era",
                    "Champions League triumphs",
                    "Record-breaking seasons",
                    "Individual accolades",
                    "Messi's iconic goals",
                    "Clásico dominance",
                    "Special performances",
                    "Departure from Barcelona"
                    ],
                    [
                    "Introduction",
                    "Messi's arrival at Barcelona",
                    "Early years and breakthrough",
                    "Messi's partnership with Ronaldinho",
                    "The Pep Guardiola era",
                    "Champions League triumphs",
                    "Record-breaking seasons",
                    "Individual accolades",
                    "Messi's iconic goals",
                    "Clásico dominance",
                    "Special performances",
                    "Departure from Barcelona"
                    ],
                    [
                    "Introduction",
                    "Messi's arrival at Barcelona",
                    "Early years and breakthrough",
                    "Messi's partnership with Ronaldinho",
                    "The Pep Guardiola era",
                    "Champions League triumphs",
                    "Record-breaking seasons",
                    "Individual accolades",
                    "Messi's iconic goals",
                    "Clásico dominance",
                    "Special performances",
                    "keroo"
                    ]
        ]
          
        context = {
            "topic_name": topic_name,
            "topic_keywords": topic_keywords,
            "selected_tone": selected_tone,
            "selected_language": selected_language,
            "selected_idea": selected_idea,
            "genrated_outlines_list": genrated_outlines_list,
            "select_individual_outlines": select_individual_outlines,
        }
        
        return render(request, self.template_name, context)
class SaveOutlinesView(View):
    template_name = 'ai_article_writer/aIArticleWriter-step-4.html'
    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        data = json.loads(request.body)
        selected_outlines = data.get('selected_outlines', [])
        slecet_individual_outlines = data.get('select_individual_outlines', False)
        outlines_string = ', '.join(selected_outlines)
        
        boolean_selected = False
        if slecet_individual_outlines =="on":
            boolean_selected = True
        
        genrated_sub_outlines_list = [
            [
            "1.1 Background and context",
            "1.2 Messi's journey to Barcelona",
            "1.3 Significance of Messi's arrival at Barcelona"
            ],
            [
            "2.1 Transfer to Barcelona",
            "2.2 Early impressions and adaptation",
            "2.3 Messi's impact on the team"
            ]
        ]
        
        outlines_id_list = []
        # Save the topic name and keywords to the Topic model 
        for otline in selected_outlines:
            outline = Outline.objects.create(
                idea = Idea.objects.get(id=request.session['idea_id']),
                Outlines = otline,
                select_individual_outlines = boolean_selected,
            )
            outlines_id_list.append(outline.id)
        
        if len (genrated_sub_outlines_list)< len(outlines_id_list):
            genrated_sub_outlines_list.append([""]*(len(outlines_id_list)-len(genrated_sub_outlines_list)))

        suboutlines_id_list = []
        
        for i in range(len(outlines_id_list)):
            suboutlines_id_list.append([])
            for j in range(len(genrated_sub_outlines_list[i])):
                subOutline = Suboutline.objects.create(
                    outline = Outline.objects.get(id=outlines_id_list[i]), 
                    suboutlines = genrated_sub_outlines_list[i][j],
                )
                suboutlines_id_list[i].append(subOutline.id)
                
                
        request.session['outlines'] = selected_outlines
        request.session['sub_outlines'] = genrated_sub_outlines_list
        request.session['outlines_id_list'] = outlines_id_list
        request.session['suboutlines_id_list'] = suboutlines_id_list
        return JsonResponse({'success': True,"outlines": outlines_string, "select_individual_outlines": slecet_individual_outlines})
        
class ArticleGenratorView(LoginRequiredMixin,ListView):
    template_name = 'ai_article_writer/aIArticleWriter-step-4.html'

    def get(self, request):
        selected_idea = request.session.get('idea')
        outlines_list = request.session.get('outlines')
        sub_outlines_list = request.session.get('sub_outlines')
        keywrods_list = request.session.get('keywords')
        selected_tone = request.session.get('tone')
        selected_language = request.session.get('language')
        
        combined_outlines = zip(outlines_list, sub_outlines_list)
        
            
        context = {
            "selected_idea": selected_idea,
            "combined_outlines": combined_outlines,
            "keywrods_list": keywrods_list,
            "selected_tone": selected_tone,
            "selected_language": selected_language
        }
        
        return render(request, self.template_name, context)
    
    def post(self, request):
        selected_idea = request.session.get('idea')
        outlines_list = request.session.get('outlines')
        sub_outlines_list = request.session.get('sub_outlines')
        keywrods_list = request.session.get('keywords')
        selected_tone = request.session.get('tone')
        selected_language = request.session.get('language')
        outlines_id_list = request.session.get('outlines_id_list')
        suboutlines_id_list = request.session.get('suboutlines_id_list')
        combined_outlines = zip(outlines_list, sub_outlines_list)

        SuboutlineBody = [
            [
                """The game of football has witnessed many extraordinary talents over the years, but few have left as indelible a mark on a single club as Lionel Messi did during his time at Barcelona. As one of the greatest footballers of all time, Messi's arrival at Barcelona marked the beginning of an era of greatness, setting in motion a series of accomplishments and records that will forever be associated with his name.""",
                """Lionel Messi's journey to Barcelona is a captivating tale of talent, determination, and destiny. Born on June 24, 1987, in Rosario, Argentina, Messi showcased extraordinary football skills from a young age. His innate ability to control the ball and navigate the field with exceptional agility caught the attention of numerous football scouts. At the age of 13, Messi seized the opportunity to join FC Barcelona's esteemed youth academy, La Masia, where he would undergo his transformation from a promising talent to a global superstar.""",
                
                """Messi's arrival at Barcelona marked a turning point for both the player and the club. With his unique skill set, Messi injected a new dimension of creativity, flair, and goal-scoring prowess into Barcelona's playing style. His mesmerizing dribbles, extraordinary vision, and deadly precision in front of goal revolutionized the team's approach to the game. Messi's ability to effortlessly weave through defenses and create opportunities for his teammates raised the overall level of play and propelled Barcelona to new heights of success.
                Furthermore, Messi's impact extended beyond the field. 
                \n
                His humble demeanor, dedication to the sport, and unwavering loyalty to the Barcelona badge endeared him to fans around the world. He became a symbol of excellence and inspiration, showcasing the values and ethos that Barcelona stood for. The arrival of Messi not only brought immense sporting success to the club but also helped shape its identity and create a lasting legacy.
                
                In the following sections, we will delve deeper into the Barcelona legacy of Lionel Messi, exploring the unparalleled accomplishments, the trophies won, the records broken, and the unforgettable moments that defined this remarkable era of greatness.""",
            ],
                [
                """keroo""",
                """adel""",
                
                """azmy""",
            ]
        ]
        
        if len(SuboutlineBody) < len(outlines_list):
            remaining = len(outlines_list) - len(SuboutlineBody)
            SuboutlineBody.extend([[""]] * remaining)
            
        for i in range(len(sub_outlines_list)):
            for j in range(len(SuboutlineBody[i])):
                suboutline = Suboutline.objects.get(id=suboutlines_id_list[i][j])
                suboutline.body = SuboutlineBody[i][j]
                suboutline.save()
                
        random_image_path = fetch_random_image(selected_idea)

        keywrod_string = ', '.join(keywrods_list)
        if random_image_path :
            article = Article.objects.create(
                title=Idea.objects.get(id=request.session['idea_id']).idea_text,
                tags=keywrod_string,
                user= request.user,
            )
            article.image = random_image_path
            article.save()
            for outline in outlines_id_list:
                article.outlines.add(Outline.objects.get(id=outline))
                
            activity = RecentActivity(
            user=User.objects.get(id=request.user.id),  
            activity_type='Article Created',
            details=selected_idea,
            idOfActivity = article.id
            )
            activity.save()
            
            outlines=article.outlines.all()
            for outline in outlines:
                print(outline.Outlines)
                suboutlines = outline.suboutline_set.all()
                for suboutline in suboutlines:
                    print(suboutline.suboutlines)
                    print(suboutline.body)

        articleSections = zip(outlines_list, sub_outlines_list,SuboutlineBody)
        article_sections = []
        for outline, sub_outline, body in articleSections:
            section = {
                'outline': outline,
                'sub_outline_body': zip(sub_outline, body)
            }   
            article_sections.append(section)
            
        context = {
            "selected_idea": selected_idea,
            "combined_outlines": combined_outlines,
            "keywrods_list": keywrods_list,
            "selected_tone": selected_tone,
            "selected_language": selected_language,
            "articleSections": article_sections,
            "article": article      
        }

        return render(request, self.template_name, context)

############################### 
# Email Tools template
############################### 
class EmailToolsView(LoginRequiredMixin, ListView):
    template_name = 'email_tools/emailTool.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)

    def post(self, request):
        project_name = request.POST.get('project-name', '')
        Email_for = request.POST.get('Email_for', '')
        Tone_Of_Voice = request.POST.get('Tone_Of_Voice', '')
        selected_Language = request.POST.get('selected_Language', '')
        Number_of_generated = request.POST.get('Number_of_generated', '')
        # Create the Project
        
        project_name_step2 = request.POST.get('project_name_step2', '')
        Email_for_step2 = request.POST.get('Email_for_step2', '')
        Tone_Of_Voice_step2 = request.POST.get('Tone_Of_Voice_step2', '')
        selected_Language_step2 = request.POST.get('selected_Language_step2', '')
        Number_of_generated_step2 = request.POST.get('Number_of_generated_step2', '')
        
        list_generated_emails_subject = [
            "Introducing Feathe.ai: Unleash the power of AI content generation!",
            "Discover Feathe.ai: Your secret weapon for AI-powered content creation.",
            "Create captivating content effortlessly with Feathe.ai.",
            "Revolutionize your content strategy with Feathe.ai's AI generator.",
            "Unleash the writer within: Feathe.ai is here!",
            "Say hello to smarter content creation with Feathe.ai.",
            "Boost your productivity with Feathe.ai's AI content generator.",
            "Welcome to Feathe.ai: Your AI writing companion.",
            "Transform your content creation process with Feathe.ai.",
            "Experience the future of content generation with Feathe.ai.",
        ]
        
        if project_name_step2 and Email_for_step2 and Tone_Of_Voice_step2 and selected_Language_step2 and Number_of_generated_step2 :
            project_name = project_name_step2
            Email_for = Email_for_step2
            Tone_Of_Voice = Tone_Of_Voice_step2
            selected_Language = selected_Language_step2
            Number_of_generated = Number_of_generated_step2
            list_generated_emails_subject = [
            "Introducing Feathe.ai: Unleash the power of AI content generation! 2",
            "Discover Feathe.ai: Your secret weapon for AI-powered content creation. 2",
            "Create captivating content effortlessly with Feathe.ai. 2",
            ]

        project = Project.objects.create(name=project_name, user=request.user)

        for i in range(len(list_generated_emails_subject)):
            emailsubject = EmailSubject.objects.create(
                project=project,
                email_purpose=Email_for,
                tone_of_voice=Tone_Of_Voice,
                language=selected_Language,
                num_generated_emails=Number_of_generated,
                generated_subject=list_generated_emails_subject[i]
            )
            
        activity = RecentActivity(
            user=User.objects.get(id=request.user.id),  
            activity_type='Email Subject Lines Created',
            details= project_name,
            idOfActivity = project.id
            )
        activity.save()
            
        context = {
            'projects': self.get_queryset(),
            'selected_project': project,
        }
        
        return render(request, 'email_tools/emailToolStep2.html', context)

class EmailSubjectView(LoginRequiredMixin, View):
    template_name = 'email_tools/emailToolStep2.html'
    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)
    
    def get(self, request, project_id):
        project = get_object_or_404(Project, id=project_id, user=request.user)
        email_subjects = project.emailsubject_set.all()
        context = {
            'projects': self.get_queryset(),
            'selected_project': project,
        }
        
        return render(request, self.template_name, context)        


class DeleteEmailSubjectView(LoginRequiredMixin, View):
    def get(self, request, email_subject_id):
        email_subject = get_object_or_404(EmailSubject, id=email_subject_id)
        project_id = email_subject.project_id
        email_subject.delete()
        url = reverse('email_subjects', args=(project_id,))
        return redirect(url)
############################### 
# Social Media Tools template
############################### 
class SocialMediaToolsView(LoginRequiredMixin,ListView):
    template_name = 'social_media_tools/socialMediaTool.html'
    
    def get(self, request):
        return render(request, self.template_name)