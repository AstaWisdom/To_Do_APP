"""Defines urls patterns for learning_logs"""

from django.urls import path
from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
    # Path that shows every topics
    path('topics/', views.topics, name='topics'),
    # Detail page for single topic
    path('topic/<int:topic_id>/', views.topic, name='topic'),
    # page for adding new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # page for adding new entries
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Page for editing the Entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    # delete the selected entry
    path('delete_entry/<int:entry_id>/', views.delete_entry, name='delete_entry'),
    # Delete the selected Topic
    path('delete_topic/<int:topic_id>', views.delete_topic, name='delete_topic'),
]
