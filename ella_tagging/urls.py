from django.conf.urls.defaults import patterns, url

from ella_tagging.views import TaggedPublishablesView


urlpatterns = patterns('',
    url(r'^(?P<tag>[\w\s]+)/', TaggedPublishablesView.as_view(), name="tag_list"),
)
