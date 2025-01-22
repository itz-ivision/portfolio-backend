from django.urls import path, include
# from . import github, resume, skills


urlpatterns = [
    path('certificates/', include('api.portfolio.certificates.urls')),
    path('github/', include('api.portfolio.github.urls')),
    path('resume/', include('api.portfolio.resume.urls')),
    path('skills/', include('api.portfolio.skills.urls')),
]
