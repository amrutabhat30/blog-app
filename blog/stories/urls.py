from django.urls import path, include
from stories.views import *

urlpatterns = [
    path('', StoriesView.as_view(), name='stories_view'),
    path('create/', CreateStoryView.as_view(), name='create_story_view'),
    path('<int:story_id>/', get_story, name="get_story_view"),
    path('<int:story_id>/edit/', EditStoryView.as_view(), name="edit_story_view"),
    path('<int:story_id>/delete/', delete_story, name="delete_story_view"),
    path('<int:story_id>/up-vote/', up_vote_story, name="up_vote_story_view"),
    path('<int:story_id>/down-vote/', down_vote_story, name="down_vote_story_view"),
    # path('story/<int:story_id>/comment/$', Comment.as_view(), name="comment_view"),
    # path('<int:story_id>/comments/', include('comments.urls')),
    path('<int:story_id>/comment/create', create_comment, name='create_comment_view'),
    path('<int:story_id>/comment/', GetCommentsView.as_view(), name='comments_view'),
    path('<int:story_id>/comment/<int:comment_id>/edit/', EditCommentView.as_view(), name='edit_comment_view'),
    path('<int:story_id>/comment/<int:comment_id>/delete/',delete_comment, name='delete_comment_view'),
    path('admin/', AdminView.as_view(), name="admin_view")

]




    # url(r'^story/(?P<story_id>[\d]+)/$', 'views.view_story', name='view_story'),
    # url(r'^story/(?P<story_id>[\d]+)/edit/$', 'views.edit_story', name='edit_story'),
    # url(r'^story/(?P<story_id>[\d]+)/delete/$', 'views.delete_story', name='delete_story'),
    # url(r'^story/(?P<story_id>[\d]+)/up_vote/$', 'views.up_vote', name='up_vote'),
    # url(r'^story/(?P<story_id>[\d]+)/down_vote/$', 'views.down_vote', name='down_vote'),

    # url(r'^story/(?P<story_id>[\d]+)/comment/$', 'views.create_comment', name='create_comment'),
    # url(r'^story/(?P<story_id>[\d]+)/comments/$', 'views.view_comments', name='view_comments'),
    # url(r'^story/(?P<story_id>[\d]+)/comment/(?P<comment_id>[\d]+)/edit/$', 'views.edit_comment',
    #     name='edit_comment'),
    # url(r'^story/(?P<story_id>[\d]+)/comment/(?P<comment_id>[\d]+)/delete/$',
    #     'views.delete_comment',name='delete_comment'),




