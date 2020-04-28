from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from common.models import SystemModel


class Post(SystemModel):
    slug = models.SlugField(_("slug"), unique=True, allow_unicode=True)
    title = models.CharField(_("title"), max_length=255)
    text = models.TextField(_("text"))
    published_at = models.DateTimeField(_("publication date"), null=True, blank=True)

    @property
    def is_published(self):
        return self.published_at is not None and self.published_at > timezone.now()

    @property
    def is_draft(self):
        return not self.is_published
