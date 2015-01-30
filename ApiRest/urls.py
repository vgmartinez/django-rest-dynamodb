from django.conf.urls import url, include
from ApiDataLab.views import SnippetViewSet, UserViewSet, api_root
from rest_framework import renderers
from ApiDataLab.dynamoViewSet import dynamo_viewset

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})
thread = dynamo_viewset.as_view({
    'get': 'list',
    'post':'create'
})
thread_detail = dynamo_viewset.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns = [
    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', api_root),
    url(r'^snippets/$', snippet_list, name='snippet-list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', snippet_detail, name='snippet-detail'),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', snippet_highlight, name='snippet-highlight'),
    url(r'^users/$', user_list, name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail'),
    url(r'^thread/', thread, name='thread'),
    url(r'^thread/(?P<pk>[0-9]+)/$', thread_detail, name='thread_detail'),
]
