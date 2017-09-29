from django.conf.urls import url
import views

__author__ = 'dipap'


urlpatterns = [
    # home page of the tool
    url(r'^$', views.home),

    # connection urls
    url(r'^connection/create/$', views.create_configuration),

    # different connection types
    url(r'^connection/update-info/(?P<pk>\d+)/sqlite3/$', views.sqlite3_info),
    url(r'^connection/update-info/(?P<pk>\d+)/mysql/$', views.mysql_info),
    url(r'^connection/update-info/(?P<pk>\d+)/postgres/$', views.postgres_info),

    # pick user table & columns
    url(r'^connection/(?P<pk>\d+)/suggest-user-table/$', views.suggest_users_table),
    url(r'^connection/(?P<pk>\d+)/select-columns/$', views.select_columns),

    # change active configuration
    url(r'^connection/(?P<pk>\d+)/set-active/$', views.set_active),
    url(r'^connection/(?P<pk>\d+)/set-inactive/$', views.set_inactive),

    # access keys
    url(r'^connection/(?P<pk>\d+)/access-keys/$', views.access_keys),
    url(r'^connection/(?P<pk>\d+)/access-keys/(?P<key_id>\d+)/revoke/$', views.revoke_access_key),

    # api access
    url(r'^api/(?P<key>[a-zA-Z0-9]+)/', views.connnection_api_view),
    url(r'^api/(?P<key>[a-zA-Z0-9]+)/(?P<action>\s+/', views.connnection_api_view),

    # query & console to run them
    url(r'^connection/(?P<pk>\d+)/query/$', views.query_connection),
    url(r'^connection/(?P<pk>\d+)/console/$', views.console),

    # delete configuration
    url(r'^connection/(?P<pk>\d+)/delete/$', views.delete_view),
]
