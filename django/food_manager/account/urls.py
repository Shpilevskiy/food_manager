from django.conf.urls import (
    url,
    include
)

from account.views import (
    UserRetrieveUpdateView,
)

urlpatterns = [
    url(r'profile/', UserRetrieveUpdateView.as_view(), name='profile')
]
