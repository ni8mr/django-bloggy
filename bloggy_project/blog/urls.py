from django.conf.urls import url
from blog import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^(?P<post_url>\w+)/$', views.post, name='post'),
]

# Explaining "(?P<post_id>d+)" expression
# (?P<Y>...) capturing group named post_id
# \d means catching 1 digit
# + means 1 or more
# in a word, we are extracting 1 digit post_id from the url 

# Explaining "(?P<post_url>\w+)" expression
# we are extracting 1 word charactered post_url from the url


