# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#from django.template import loader
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.db.models import F
from django.views import generic
from django.utils import timezone

from .models import Question, Choice
import pdb

# This commented out index is a long version of rendering template using loader and http response
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     print latest_question_list
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))

# since loading and sending http response is common a shortcut (i.e. render) was made
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = { 'latest_question_list': latest_question_list }
#     return render(request, 'polls/index.html', context)

# converted to use generic views
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions (not including those set to be published in the future)."""
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

# initial version of detail using http response
# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)

# version of detail using render method. Uses try-except to check if record exists
# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404('Question does not exist.')   # raises a 404 exception if question with primary key (i.e. id) does not exist
#     return render(request, 'polls/detail.html', {'question': question})


# since checking record and returning 404 if no record found is common a shortcut (i.e. get_object_or_404 or get_list_or_404) is made
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})

# converted to use generic views
class DetailView(generic.DetailView):
    # model = Question
    # shorthand for queryset = Question.objects.all()
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

# initial version of results
# def results(request, question_id):
#     response = "You're looking at the results of the question %s."
#     return HttpResponse(response % question_id)

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

# converted to use generic views
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

# initial version of vote
# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)

def vote(request, pk):
    question = get_object_or_404(Question, pk=pk)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        # converted this from votes+=1 to avoid race condition
        # this way instead of python updating fields it will be the database updating the fields
        selected_choice.votes = F('votes')+1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the back button
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

# Create your views here.
