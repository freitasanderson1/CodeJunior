from django.contrib import admin
from django.urls import include, path

import problemasProgramacao

urlpatterns = [
    path("codejunior/admin/", admin.site.urls),
    path("codejunior/", include('problemasProgramacao.urls'))
]
