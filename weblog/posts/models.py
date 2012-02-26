#coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from tagging.fields import TagField


class Post(models.Model):
    title = models.CharField(_('title'), max_length=200)
    content = models.TextField(_('cotent'))

    create_time = models.DateTimeField(_('create time'), auto_now_add=True)
    update_time = models.DateTimeField(_('update time'), auto_now=True)
    author = models.ForeignKey(User, verbose_name=_('author'), related_name='posts')

    tags = TagField()

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')

    def __unicode__(self):
        return self.title
