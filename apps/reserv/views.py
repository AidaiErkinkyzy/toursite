from django.db.transaction import commit
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView, TemplateView
from .models import Reserv
from .forms import ResetForm

class ResetView(TemplateView):
    template_name = 'pages/reservation.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ResetForm
        return context


    def post(self, request, *args, **kwargs):
        form = ResetForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('/')
        return self.render_to_response(self.get_context_data(form=form))