from django.test import TestCase
from .models import Todo

class AnimalTestCase(TestCase):
    def setUp(self):
        Todo.objects.create(title="Todo1", isCompleted=True)

    def test1(self):
        todo1 = Todo.objects.get(title="Todo1")
        self.assertEqual(todo1.isCompleted, True)
