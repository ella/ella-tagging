'''
Created on 1.2.2012

@author: xaralis
'''
from datetime import datetime

from django.conf import settings
from django.contrib.contenttypes.models import ContentType

from tagging.models import TaggedItem

from ella.core.models import Publishable

def related_by_tags(obj, count, collected_so_far, mods=[], only_from_same_site=True):
    """
    Returns objects related to ``obj`` up to ``count`` by targets of 
    matching ``TaggedItem`` instances.
    """
    if isinstance(obj, Publishable):
        obj = obj.publishable_ptr

    qset = Publishable.objects.filter(
        publish_from__lte=datetime.now(),
        published=True,
    ).distinct()

    if mods:
        qset = qset.filter(content_type__in=[
            ContentType.objects.get_for_model(m).pk for m in mods])
    if only_from_same_site:
        qset = qset.filter(category__site__pk=settings.SITE_ID)

    to_add = TaggedItem.objects.get_related(obj, qset, num=count + len(collected_so_far))
    for rel in to_add:
        if rel != obj and rel not in collected_so_far:
            count -= 1
            collected_so_far.append(rel)
        if count <= 0:
            return collected_so_far
    return collected_so_far
