#coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _

from weblog.posts.models import Post


class Comment(models.Model):
    content = models.TextField(_('cotent'))
    signature = models.CharField(_('signature'), max_length=20)

    create_time = models.DateTimeField(_('create time'), auto_now_add=True)
    post = models.ForeignKey(Post, related_name='comments')

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')

    def __unicode__(self):
        return u'Comment for `%s`' % self.post
