from django.urls import path
from . import views

urlpatterns = [
    path('', views.LongFormEditorView.as_view(), name='long_form_editor'),

]