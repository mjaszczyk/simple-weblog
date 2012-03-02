from __future__ import absolute_import
from django.contrib import admin
from django.test import TestCase, LiveServerTestCase
from django.core.urlresolvers import reverse
from selenium.webdriver.firefox.webdriver import WebDriver

from .models import Post


class EditorTest(LiveServerTestCase):

    fixtures = ('test_auth.json',)

    TEST_USERNAME = 'm'
    TEST_PASSWORD = 'm'

    TEST_POST_FIELDS = (
        ('title', u'Test title'),
        ('content', u"Test content with markdown markup\n\t\n\t> Quote\n\t\n\t* Test1\n\t* Test2\n\t"),
        ('tags', u'tag1,tag2'),
    )

    ADMIN_ROOT_URL = '/admin/'

    @classmethod
    def setUpClass(cls):
        cls.ADMIN_POST_CREATE_URL = reverse('admin:%s_%s_add' % (Post._meta.app_label,
            Post._meta.module_name), current_app=admin.site.name)
        cls.ADMIN_POST_LIST_URL = reverse('admin:%s_%s_changelist' % (Post._meta.app_label,
            Post._meta.module_name), current_app=admin.site.name)

        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)
        super(EditorTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(EditorTest, cls).tearDownClass()
        cls.selenium.quit()

    def test_post_creation(self):
        ''' Test post create proces and post display on homepage '''

        # login editor
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/'))
        self.selenium.find_element_by_id("id_username").send_keys(self.TEST_USERNAME)
        self.selenium.find_element_by_id("id_password").send_keys(self.TEST_PASSWORD)
        self.selenium.find_element_by_css_selector('#login-form .submit-row input').click()

        # count posts for future assertion
        before_posts_count = Post.objects.count()
        self.selenium.get('%s%s' % (self.live_server_url, self.ADMIN_POST_CREATE_URL))
        for key, value in self.TEST_POST_FIELDS:
            self.selenium.find_element_by_id("id_%s" % key).send_keys(value)
        self.selenium.find_element_by_css_selector('#post_form .submit-row input[name=_save]').click()
        self.assertTrue(self.selenium.current_url.endswith(self.ADMIN_POST_LIST_URL))
        # check if post was created
        self.assertEqual(before_posts_count + 1, Post.objects.count())
        self.new_post = Post.objects.latest()

        # go to homepage
        self.selenium.get('%s%s' % (self.live_server_url, '/'))

        first_post = self.selenium.find_elements_by_css_selector('.hero-unit.post')[0]
        # check if first post is the last added
        self.assertEqual(first_post.find_element_by_css_selector('h2 a').text,
                dict(self.TEST_POST_FIELDS)['title'])

        # go to detail
        first_post.find_element_by_css_selector('h2 a').click()
        # check if it is correct location
        self.assertTrue(self.selenium.current_url.endswith(self.new_post.get_absolute_url()))

    def test_post_markup(self):
        ''' Test post content markup '''

        post_content = self.selenium.find_element_by_css_selector('#post-content')
        # post content should have quote
        self.assertTrue(bool(post_content.find_elements_by_tag_name('blockquote')))
        # post content should have list
        self.assertTrue(bool(post_content.find_elements_by_css_selector('ul li')))

    def test_post_tags(self):
        ''' Test post tags '''

        # go to homepage
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        # take first post
        first_post = self.selenium.find_elements_by_css_selector('.hero-unit.post')[0]
        post_title = first_post.find_element_by_css_selector('h2 a').text
        # go to each tag list page
        for label in first_post.find_elements_by_css_selector('a.label'):
            self.selenium.get(label.get_attribute('href'))
            first_tagged_post = self.selenium.find_elements_by_css_selector('.hero-unit.post')[0]
            self.assertEqual(post_title, first_tagged_post.find_element_by_css_selector('h2 a').text)


class PostTest(TestCase):
    
    TEST_TAGS = ['tag 1', 'tag 2', 'tag 3']

    def test_tags_set(self):
        ''' Test Post model methods: set_tags and get_tags '''
        post = Post.objects.all()[0]
        post.set_tags(','.join(self.TEST_TAGS))
        self.assertSetEqual(set([t.name for t in post.get_tags()]).intersection(set(self.TEST_TAGS)),
                set(self.TEST_TAGS))

    def test_ordering(self):
        ''' Posts should be ordered chronologically by create_time, latest first'''
        posts = Post.objects.all()
        self.assertGreater(posts[0].create_time, posts[1].create_time)
