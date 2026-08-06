from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Choice, Question


def index(request):
    latest_question_list = Question.objects.order_by("-publish_date")[:5]
    #template = loader.get_template("polls/index.html")
    context = {"latest_question_list": latest_question_list}
    #output = ", ".join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)
    return render(request, "polls/index.html", context)

def about(request):
    return HttpResponse("this is the about page of our")

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
              "polls/detail.html",
              {
                  "question": question,
                  "error_message": "you didn't select a choice yet",
              },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))