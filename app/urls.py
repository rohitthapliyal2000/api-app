from django.urls import path, include
from django.conf.urls import url
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
	path('api/feed/', views.feed_data),
	path('api/bank/<slug:ifsc>', views.bank_list.as_view(), name='bank_list'),
	url(r'^api/branch/(?P<bank_name>[\w|\W]+)/(?P<city>[\w]+)/$', views.branch_list.as_view(), name='branch_list'),
	path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
	path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
