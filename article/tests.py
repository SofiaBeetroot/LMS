from django.test import TestCase
from django.urls import reverse
from article.views import *


class TopicTest(TestCase):
    def setUp(self) -> None:
        self.test_topic = Topic.objects.create(title='Test topic', text='My test text',
                                               url='http://localhost:8000/test', type=1)

    def test_get_topic(self):
        database_topic = Topic.objects.get(title='Test topic')
        self.assertEqual(database_topic, self.test_topic)

    def test_topic_creation(self):
        topic = Topic.objects.create(title='Test topic creation', text='My test text',
                                     url='http://localhost:8000/test', type=1)
        self.assertTrue(isinstance(topic, Topic))
        database_topic = Topic.objects.get(title='Test topic creation')
        self.assertEqual(topic, database_topic)

    def test_topic_update(self):
        topic = Topic.objects.filter(title='Test topic')
        topic.update(text='Updated text')
        new_topic = Topic.objects.get(title='Test topic')
        self.assertEqual(new_topic.text, 'Updated text')

    def test_topic_delete(self):
        self.test_topic.delete()
        self.assertFalse(Topic.objects.filter(title='Test topic').exists())


class ArticleViewTest(TestCase):

    def test_getting_topic_list(self):
        url = reverse('topic_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_getting_topic_list_func(self):
        url = reverse('function_topic_list')
        response = self.client.get(url)
        self.assertIn('text/html', response.headers.get('Content-Type'))


class TopicFormTest(TestCase):
    def setUp(self) -> None:
        self.topic = Topic.objects.create(title='Test topic', text='My test text',
                                          url='http://localhost:8000/test', type=1)

    def test_creation_topic_form__valid(self):
        data = {'title': self.topic.title, 'subtitle': 'My subtitle', 'text': self.topic.text,
                'url': self.topic.url, 'type': self.topic.type}
        form = TopicForm(data=data)
        self.assertTrue(form.is_valid())

    def test_creation_topic_form__invalid(self):
        data = {'title': self.topic.title, 'text': self.topic.text,
                'url': self.topic.url, 'type': self.topic.type}
        form = TopicForm(data=data)
        self.assertFalse(form.is_valid())
