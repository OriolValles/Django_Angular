from django.contrib import admin
from django.urls import path
from backend.apirest import views

router = routers.DefaultRouter()
router.register(r'printers', views.PrinterViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
