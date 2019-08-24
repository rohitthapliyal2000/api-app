from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
	path('api/feed/', views.feed_data),
	path('api/bank/<int: ifsc>', views.bank_list.as_view(), name='bank_list'),
	path('api/branch/<slug: bank_name>/<slug: city>', views.branch_list.as_view(), name='branch_list'),
	path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
	path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
	