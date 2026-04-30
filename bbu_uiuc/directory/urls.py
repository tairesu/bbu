from django.conf import settings
from django.conf.urls.static import static

"""
URL configuration for directory app.

Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from directory.views import (
    LandingPageView,
    AboutView,
    BusinessCreateView,
)
urlpatterns = [
    path('', LandingPageView.as_view(), name="home_urlpattern"),
    path('business/new', BusinessCreateView.as_view(), name="new_business_urlpattern"),
    path('about/', AboutView.as_view(), name="about_urlpattern")
]


