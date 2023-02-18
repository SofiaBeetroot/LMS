import datetime
from django.db.models import Count, Avg, Max, Min
from django.shortcuts import render
from django.http import HttpResponse
from article.models import Topic, User


# def index(request):
#     return HttpResponse("Hello, world. Greetings from Beetroot Academy!")


def get_topic_list(request):
    context = {'topic_list': Topic.objects.all()}
    return render(request, 'courses.html', context)


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
