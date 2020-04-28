from django.test import TestCase

from common.models import SystemModel


class SM(SystemModel):
    class Meta:
        app_label = "common"


class PostTestCase(TestCase):
    def test_safe_deletion(self):
        sm = SM.objects.create()
        self.assertFalse(sm.is_deleted)

        sm.delete()
        self.assertTrue(sm.is_deleted)

        self.assertIsNone(SM.objects.filter(pk=sm.id).first())
        self.assertIsNotNone(SM.objects_unsafe.filter(pk=sm.id).first())

        sm.restore()
        self.assertIsNotNone(SM.objects.filter(pk=sm.id).first())
