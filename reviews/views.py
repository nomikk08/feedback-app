from typing import Any, Dict
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, CreateView
from django.views.generic import ListView, DetailView

from .forms import ReviewForm
from .models import Review

# Create your views here.

# Class based view
class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"
    
class ThankYouView(TemplateView):
    template_name = 'reviews/thank-you.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['message'] = 'Your feedback matters'
        return context
    
class ReviewListView(ListView):
    template_name = 'reviews/review_list.html'
    model = Review
    context_object_name = 'reviews'

    def get_queryset(self):
        base_query =  super().get_queryset()
        data = base_query.filter(rating__gte =3 )
        return data
    
    
class SingleReviewlView(DetailView):
    template_name = 'reviews/single_review.html'
    model = Review
    