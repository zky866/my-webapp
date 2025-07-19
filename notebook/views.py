from django.shortcuts import render,redirect
from .models import Topic
from .forms import TopicForm,EntryForm


# Create your views here.
def topics(request):
    topics=Topic.objects.order_by("date_added")
    context={"topics":topics}
    return render(request,"notebook/topics.html",context)


def notebook(request):
    return render(request,"notebook/notebook.html")

def topic(request,topic_id):
    topic=Topic.objects.get(id=topic_id)
    entries=topic.entry_set.order_by("-date_added")
    context={"topic":topic,"entries":entries}
    return render(request,"notebook/topic.html",context)

def new_topic(request):

    if request.method != "POST":
        form=TopicForm()
    else:
        form=TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("notebook:topics")
    context = {"form":form}
    return render(request,"notebook/new_topic.html",context)

def new_entry(request,topic_id):
    topic=Topic.objects.get(id=topic_id)

    if request.method != "POST":
        form=EntryForm()
    else:
        form=EntryForm(data=request.POST)
        if form.is_valid():
            new_entry=form.save(commit=False)
            new_entry.topic=topic
            new_entry.save()
            return redirect("notebook:topic",topic_id=topic_id)

    context = {"form":form,"topic":topic}
    return render(request,"notebook/new_entry.html",context)



