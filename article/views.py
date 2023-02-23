import datetime
from django.db.models import Count, Avg, Max, Min
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from article.models import Topic, User
from article.forms import TopicForm
from django.views.generic.list import ListView
from django.views.generic.edit import FormView


# def index(request):
#     return HttpResponse("Hello, world. Greetings from Beetroot Academy!")


def get_topic_list(request):
    topic_type = request.GET.get('type', None)
    if topic_type:
        queryset = Topic.objects.filter(type=topic_type)
    else:
        queryset = Topic.objects.all()
    context = {'topic_list': queryset}
    return render(request, 'test.html', context)


# Create - 2 variants
# Update - 2 variants
# Delete

def create_topic(request):
    # I
    # topic = Topic(title='Django ORM', text='We are learning Django', type=4)
    # topic.subtitle = 'My subtitle'
    # topic.save()
    # II
    topic = Topic.objects.create(title='Django ORM', text='We are learning Django', type=4)
    return render(request, 'courses.html', {'topic_list': [topic]})


def update_topic(request):
    # I
    # topic = Topic.objects.get(id=4)
    # topic.author = User.objects.get(username='Sofia')
    # topic.save()
    data = {'text': 'Django ORM', 'subtitle': 'My subtitle',
            'url': 'https://docs.djangoproject.com/en/4.1/topics/db/queries/'}
    # for key, value in data.items():
    #     setattr(topic, key, value)
    # topic.save()
    # II
    topic = Topic.objects.filter(id=4)
    topic.update(**data)
    return render(request, 'courses.html', {'topic_list': topic})


def delete_topic(request):
    # I
    topic = Topic.objects.get(id=4)
    topic.delete()
    # II
    # Topic.objects.filter(id=4).delete()
    return render(request, 'courses.html', {'topic_list': Topic.objects.all()})


"""Filter"""
def filter_topic(request):
    # Get all records in table
    all_topic = Topic.objects.all()
    # Get record with conditions
    topics = Topic.objects.filter(type=5)
    topics = Topic.objects.filter(type__range=(1, 5))
    topics = Topic.objects.filter(type=5, title__contains='Django')
    topics = Topic.objects.filter(author__username__contains='Sofia')
    topics = Topic.objects.filter(author__username__contains='Sofia').count()
    topics = Topic.objects.filter(author__username__contains='Sofia').first()
    topics = Topic.objects.filter(author__username__contains='Sofia').last()
    topics = Topic.objects.filter(author__username__contains='Sofia').exists()
    topics = Topic.objects.filter(author__username__contains='Sofia').distinct('type')
    topics = Topic.objects.filter(author__username__contains='Sofia').order_by('creation_date').distinct('type')
    topics = Topic.objects.filter(author__username__contains='Sofia').order_by('-creation_date').distinct('type')
    topics = Topic.objects.exclude(url__isnull=True)
    topics = Topic.objects.filter(type=5).exclude(author_id=3)
    now_ = datetime.datetime.now()
    topics = Topic.objects.filter(type=4).union(
        Topic.objects.filter(creation_date__range=(now_ - datetime.timedelta(days=7), now_ - datetime.timedelta(days=2))))
    # topics = Topic.objects.annotate('type')
    # topics = Topic.objects.annotate(Count('author'))
    # topics = Topic.objects.aggregate(Max('text__len'))
    return render(request, 'courses.html', {'topic_list': topics})


def create_topic_form(request):
    if request.method == 'POST':
        print(request.POST.get("title"))
        form = TopicForm(request.POST)
        if form.is_valid():
            # Topic.objects.create(**form.cleaned_data)
            return redirect('topic_list')
    else:
        form = TopicForm()
        return render(request, 'contact.html', {'form': form})


class TopicListView(ListView):
    # model = Topic
    template_name = 'test.html'

    def get_queryset(self):
        topic_type = self.request.GET.get('type', None)
        if topic_type:
            self.queryset = Topic.objects.filter(type=topic_type)
        else:
            self.queryset = Topic.objects.all()
        return self.queryset


class TopicFormView(FormView):
    template_name = 'contact.html'
    form_class = TopicForm
    success_url = '/articles/topics/'

    def form_valid(self, form):
        Topic.objects.create(**form.cleaned_data)
        return HttpResponseRedirect(self.get_success_url())
