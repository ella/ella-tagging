# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

from django.core.urlresolvers import reverse
from django.test import TestCase

from tagging.models import TaggedItem, Tag

from nose import tools

from test_ella.test_core import create_basic_categories, create_and_place_a_publishable
from test_ella import template_loader

from ella_tagging import views

class TestTaggingViews(TestCase):
    def setUp(self):
        super(TestTaggingViews, self).setUp()
        create_basic_categories(self)
        create_and_place_a_publishable(self)

    def tearDown(self):
        super(TestTaggingViews, self).tearDown()
        template_loader.templates = {}

    def test_get_tagged_publishables_returns_tagged_publishable(self):
        Tag.objects.update_tags(self.only_publishable, 'tag1 tag2')
        tools.assert_equals(2, TaggedItem.objects.count())

        t = Tag.objects.get(name='tag1')
        tools.assert_equals([self.publishable], [p.target for p in views.get_tagged_publishables(t)])

    def test_get_tagged_publishables_doesnt_return_tagged_publishable_with_future_placement(self):
        Tag.objects.update_tags(self.only_publishable, 'tag1 tag2')
        tools.assert_equals(2, TaggedItem.objects.count())

        self.publishable.publish_from = datetime.now() + timedelta(days=2)
        self.publishable.save()

        t = Tag.objects.get(name='tag1')
        tools.assert_equals([], list(views.get_tagged_publishables(t)))

    def test_get_tagged_publishables_returns_no_objects_when_none_tagged(self):
        t = Tag.objects.create(name='tag1')
        tools.assert_equals([], list(views.get_tagged_publishables(t)))

    def test_tagged_publishables_view(self):
        Tag.objects.update_tags(self.only_publishable, 'tag1 tag2')
        tools.assert_equals(2, TaggedItem.objects.count())

        t = Tag.objects.get(name='tag1')
        url = reverse('tag_list', kwargs={'tag':'tag1'})
        template_loader.templates['page/tagging/listing.html'] = ''
        response = self.client.get(url)

        tools.assert_equals([self.publishable], [p.target for p in response.context['object_list']])
        tools.assert_equals(t, response.context['tag'])

