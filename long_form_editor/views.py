from django.views.generic import ListView, CreateView
from .models import Block
from .forms import BlockForm
import uuid
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class LongFormEditorView(LoginRequiredMixin,CreateView):
    model = Block
    form_class = BlockForm
    template_name = 'long form editor/Long-form-editor.html'
    form_class = BlockForm
    success_url = reverse_lazy('long_form_editor')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blocks'] = Block.objects.all()
        return context
    