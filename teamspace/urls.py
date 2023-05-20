from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from django.urls import path

from core import views as core_views
from evil import views as evil_views
from pages import views as pages_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Login/Logout
    path('login', core_views.login, name='login'),
    path('logout', core_views.logout, name='logout'),

    # Password Reset
    path('password_reset/complete', PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html',
    ), name='password_reset_complete'),
    path('password_reset/<uidb64>/<token>/confirm', PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html',
    ), name='password_reset_confirm'),
    path('password_reset/done', PasswordResetDoneView.as_view(
        template_name='password_reset_done.html',
    ), name='password_reset_done'),
    path('password_reset', PasswordResetView.as_view(
        template_name='password_reset.html',
        subject_template_name='password_reset_subject.txt',
        from_email=settings.DEFAULT_FROM_EMAIL,
        email_template_name='password_reset_email.html',
    ), name='password_reset'),

    # Dynamic static files :)
    path('static/base.css', core_views.base_css, name='base_css'),

    # Pages
    path('', pages_views.index, name='index'),
    path('pages/edit', pages_views.edit, name='edit'),
    path('pages/view/<username>', pages_views.view, name='view'),
    path('pages/css/<username>.css', pages_views.css, name='css'),
    path('pages/js/<username>.js', pages_views.js, name='js'),
    path('pages/pic/<username>', pages_views.pic, name='pic'),

    # Posts
    path('posts/add/<username>', pages_views.add, name='add'),
    path('posts/reply/<int:post_id>', pages_views.reply, name='reply'),
    path('posts/search', pages_views.search, name='search'),
]

if settings.EVIL:
    urlpatterns += [
        path('l0gin', evil_views.evil_login, name='evil_login'),
        path('haha', evil_views.haha, name="haha")
    ]
