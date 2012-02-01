from django.conf.urls.defaults import patterns, include

urlpatterns = patterns('',
    (r'^tags/', include('ella_tagging.urls')),
    (r'^', include('ella.core.urls')),
)
