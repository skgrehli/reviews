
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from accounts import urls
from django.conf import settings
from django.conf.urls.static import static
from blog import urls
import blog.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('blog/',include('blog.urls')),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
    path('', blog.views.IndexPageView, name='home'),
]

# urlpatterns += i18n_patterns()

# urlpatterns += staticfiles_urlpatterns() 

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# urlpatterns += format_suffix_patterns(urlpatterns)

# accounts/login/ [name='login']
# accounts/logout/ [name='logout']
# accounts/password_change/ [name='password_change']
# accounts/password_change/done/ [name='password_change_done']
# accounts/password_reset/ [name='password_reset']
# accounts/password_reset/done/ [name='password_reset_done']
# accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/reset/done/ [name='password_reset_complete']