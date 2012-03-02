#coding: utf-8
from __future__ import absolute_import
import autofixture
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

from tagging.fields import Tag, TagField

from .fixtures import PostFixture


class Post(models.Model):
    title = models.CharField(_('title'), max_length=200)
    content = models.TextField(_('content'),
            help_text=u'Markdown is available http://pl.wikipedia.org/wiki/Markdown')

    create_time = models.DateTimeField(_('create time'), auto_now_add=True, db_index=True)
    update_time = models.DateTimeField(_('update time'), auto_now=True)
    author = models.ForeignKey(User, verbose_name=_('author'), related_name='posts')

    tags = TagField()

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')
        get_latest_by = 'create_time'
        ordering = ('-create_time',)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts.detail', args=(slugify(self.title), self.id))

    def set_tags(self, tags):
        Tag.objects.update_tags(self, tags)

    def get_tags(self):
        return Tag.objects.get_for_object(self)

autofixture.register(Post, PostFixture)
