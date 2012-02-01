'''
Created on 1.2.2012

@author: xaralis
'''
from datetime import datetime

from django.conf import settings
from django.contrib.contenttypes.models import ContentType

from tagging.models import TaggedItem

from ella.core.models import Publishable
from ella.core.related_finders import related_only, fillup_from_category

def with_tagging(obj, count, mods=[], only_from_same_site=True):
    """
    Returns objects related to ``obj`` up to ``count`` by searching 
    ``Related`` instances for the ``obj``. If not enought records is found,
    finder tries to fill it up with matching ``TaggedItem`` instances. If 
    there is still not enought items after doing this, related object list
    is filled up by top objects listed in the same category as ``obj``.
    """
    related = related_only(obj, count, mods, only_from_same_site)

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

    to_add = TaggedItem.objects.get_related(obj, qset, num=count + len(related))
    for rel in to_add:
        if rel != obj and rel not in related:
            count -= 1
            related.append(rel)
        if count <= 0:
            return related

    return fillup_from_category(related, obj, count, mods, only_from_same_site)
