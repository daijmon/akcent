from django.shortcuts import render
from django.views import generic


# Create your views here.
class HomeView(generic.TemplateView):
    template_name = 'store/home.html'
    # context_object_name = 'latest_question_list'
