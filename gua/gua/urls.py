"""gua URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from blog.api import post as blog_post
from blog.api import category as blog_category
from blog.api import base as blog_base

from glaw.gateway import post as glaw_post
from glaw.gateway import base as glaw_base

from sepicat.api import analysis as sepi_analysis
from sepicat.api import base as sepi_base


urlpatterns = [
    path('admin/', admin.site.urls),
]

# Blog
blog_urlpatterns = [
    path(blog_base.url_prefix('posts'), blog_post.query_posts),
    path(blog_base.url_prefix('categories'), blog_category.query_categories),
]

urlpatterns += blog_urlpatterns

# Glaw
glaw_urlpatterns = [
    path(glaw_base.url_prefix('posts'), glaw_post.query_posts),
]

urlpatterns += glaw_urlpatterns

# Sepicat
sepicat_urlpatterns = [
    path(sepi_base.url_prefix_v1('analysis'), sepi_analysis.commit_analysis),
]
urlpatterns += sepicat_urlpatterns
