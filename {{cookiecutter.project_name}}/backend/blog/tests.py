from django.test import TestCase
from blog.models import Post
from faker import Faker

Faker.seed(42)
fake_en = Faker("en_US")
fake_ru = Faker("ru_RU")


class PostTestCase(TestCase):
    def setUp(self):
        Post.objects.create(
            slug="fear-police",
            title="Build three east organization people information",
            text="""Upon very act perform none beyond. \
Defense enter value thing these hard citizen. \
Region particularly would pressure account stage federal.""",
        )
        Post.objects.create(
            slug="check-several-much",
            title="North first end prove fire enter capital population",
            text="List top somebody college be middle plan. \
Behavior weight dog financial southern challenge.\
\nWorker particularly shoulder lay though.",
        )

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        first = Post.objects.first()
        last = Post.objects.last()
        self.assertEqual(first.is_draft, True)
        self.assertEqual(last.is_draft, True)
