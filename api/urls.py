from django.urls import path, include

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('about/', include('api.about.urls')),
    path('blog/', include('api.blog.urls')),
    path('chat-bot/', include('api.chatbot.urls')),
    path('contact/', include('api.contact.urls')),
    path('health-check/', include('api.healthCheck.urls')),
    path('home/', include('api.home.urls')),
    path('portfolio/', include('api.portfolio.urls')),
    path('services/', include('api.services.urls')),
    path('testimonials/', include('api.testimonials.urls')),
]
