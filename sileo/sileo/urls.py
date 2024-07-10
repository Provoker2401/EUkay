# from django.conf.urls import url
# from .views import (
#     ResourceDetailView, ResourceListView, ResourceCreateView,
#     ResourceUpdateView, ResourceDeleteView, ResourceFormInfoView)

# urlpatterns = (
#     url(r'(?P<version>[\w-]+)/(?P<namespace>[\w-]+)/(?P<resource>[\w-]+)/get/(?P<pk>\d+)/$',
#         ResourceDetailView.as_view(), name='api-detail-version'),
#     url(r'(?P<namespace>[\w-]+)/(?P<resource>[\w-]+)/get/(?P<pk>\d+)/$',
#         ResourceDetailView.as_view(), name='api-detail'),

#     url(r'(?P<version>[\w-]+)/(?P<namespace>[\w-]+)/(?P<resource>[\w-]+)/filter/$',
#         ResourceListView.as_view(), name='api-list-version'),
#     url(r'(?P<namespace>[\w-]+)/(?P<resource>[\w-]+)/filter/$',
#         ResourceListView.as_view(), name='api-list'),

#     url(r'(?P<version>[\w-]+)/(?P<namespace>[\w-]+)/(?P<resource>[\w-]+)/create/$',
#         ResourceCreateView.as_view(), name='api-create-version'),
#     url(r'(?P<namespace>[\w-]+)/(?P<resource>[\w-]+)/create/$',
#         ResourceCreateView.as_view(), name='api-create'),

#     url(r'(?P<version>[\w-]+)/(?P<namespace>[\w-]+)/(?P<resource>[\w-]+)/update/$',
#         ResourceUpdateView.as_view(), name='api-update-version'),
#     url(r'(?P<namespace>[\w-]+)/(?P<resource>[\w-]+)/update/$',
#         ResourceUpdateView.as_view(), name='api-update'),

#     url(r'(?P<version>[\w-]+)/(?P<namespace>[\w-]+)/(?P<resource>[\w-]+)/delete/$',
#         ResourceDeleteView.as_view(), name='api-delete-version'),
#     url(r'(?P<namespace>[\w-]+)/(?P<resource>[\w-]+)/delete/$',
#         ResourceDeleteView.as_view(), name='api-delete'),

#     url(r'(?P<version>[\w-]+)/(?P<namespace>[\w-]+)/(?P<resource>[\w-]+)/form-info/$',
#         ResourceFormInfoView.as_view(), name='api-form-info-version'),
#     url(r'(?P<namespace>[\w-]+)/(?P<resource>[\w-]+)/form-info/$',
#         ResourceFormInfoView.as_view(), name='api-form-info'),
# )

from django.urls import path
from .views import (
    ResourceDetailView, ResourceListView, ResourceCreateView,
    ResourceUpdateView, ResourceDeleteView, ResourceFormInfoView)

urlpatterns = [
    path('<str:version>/<str:namespace>/<str:resource>/get/<int:pk>/',
         ResourceDetailView.as_view(), name='api-detail-version'),
    path('<str:namespace>/<str:resource>/get/<int:pk>/',
         ResourceDetailView.as_view(), name='api-detail'),

    path('<str:version>/<str:namespace>/<str:resource>/filter/',
         ResourceListView.as_view(), name='api-list-version'),
    path('<str:namespace>/<str:resource>/filter/',
         ResourceListView.as_view(), name='api-list'),

    path('<str:version>/<str:namespace>/<str:resource>/create/',
         ResourceCreateView.as_view(), name='api-create-version'),
    path('<str:namespace>/<str:resource>/create/',
         ResourceCreateView.as_view(), name='api-create'),

    path('<str:version>/<str:namespace>/<str:resource>/update/',
         ResourceUpdateView.as_view(), name='api-update-version'),
    path('<str:namespace>/<str:resource>/update/',
         ResourceUpdateView.as_view(), name='api-update'),

    path('<str:version>/<str:namespace>/<str:resource>/delete/',
         ResourceDeleteView.as_view(), name='api-delete-version'),
    path('<str:namespace>/<str:resource>/delete/',
         ResourceDeleteView.as_view(), name='api-delete'),

    path('<str:version>/<str:namespace>/<str:resource>/form-info/',
         ResourceFormInfoView.as_view(), name='api-form-info-version'),
    path('<str:namespace>/<str:resource>/form-info/',
         ResourceFormInfoView.as_view(), name='api-form-info'),
]