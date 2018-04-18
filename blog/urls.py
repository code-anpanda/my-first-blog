from django.conf.urls import url # django 메소드
from . import views # 우리가 만들 view들

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]


# post_list라는 이름의 view가 ‘^$’ URL에 할당됨
# 누군가 ‘http://127.0.0.1:8000/’ 주소로 들어왔을 때 views.post_list를 보여줌
# 마지막 name=‘post_list’는 URL에 이름을 붙인 것
