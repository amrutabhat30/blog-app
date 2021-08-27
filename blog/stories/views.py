from django.views import View
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import F
from datetime import datetime, timedelta

import logging

from stories.forms import CreateStoryForm, CreateCommentForm
from stories.models import Story, Comment
from stories.utilities import get_story_object, get_comment_object

logger = logging.getLogger(__name__)


# Class based views
class StoriesView(View):
    def get(self, request):
        """
        home page displaying recent 5 stories
        :param request: Django request object
        :return: renders template displaying recent 5 stories that are not archived
        """
        duration = request.GET.get('duration', 0)
        if duration:
            time_threshold = datetime.now() - timedelta(hours=int(duration))
            stories = Story.objects.filter(archive=False, created_on__gt=time_threshold)[:5]
        else:
            stories = Story.objects.filter(archive=False).order_by('-created_on')[:5]
        message = ''
        if not stories:
            message = "No stories to show"
        return render(request, 'stories/home.html', {'stories': stories, 'param': 'home', 'message': message})


class CreateStoryView(View):
    def post(self, request):
        """
        create and save a story with title and link
        :param request: Django request object
        :return: redirects to home page
        """
        try:
            story_form = CreateStoryForm(request.POST)
            if story_form.is_valid():
                story_form.save()
                return HttpResponseRedirect(reverse('stories_view'))
            return render(request, 'stories/create_story.html', {'form': story_form, 'param': 'create'})
        except Exception as e:
            logger.error(e)
            return render(request, 'stories/error.html')

    def get(self, request):
        """
        :param request: Django request object
        :return: renders a template to create a story
        """
        story_form = CreateStoryForm()
        return render(request, 'stories/create_story.html', {'form': story_form, 'param': 'create'})


class EditStoryView(View):
    def post(self, request, story_id):
        """
        edit the title and link of a story
        :param request: Django request object
        :param story_id: id of the story to be edited
        :return: redirects to home page
        """
        story = get_story_object(request=request, story_id=story_id)
        story_form = CreateStoryForm(request.POST, instance=story)
        if story_form.is_valid():
            story_form.save()
            return HttpResponseRedirect(reverse('stories_view'))
        return render(request, 'stories/create_story.html', {'form': story_form, 'param': 'edit'})

    def get(self, request, story_id):
        """
        :param request: Django request object
        :param story_id: id of the story to be edited
        :return: renders a template to submit edited title and link
        """
        story = get_story_object(request=request, story_id=story_id)
        story_form = CreateStoryForm(instance=story)
        return render(request, 'stories/create_story.html', {'form': story_form, 'param': 'edit'})


def get_story(request, story_id):
    """
    :param request: Django request object
    :param story_id: id of the story
    :return: renders a template to display story and post comments on the story
    """
    story = get_story_object(request, story_id)
    comment_form = CreateCommentForm()
    return render(request, 'stories/display_story.html', {'story': story, 'form': comment_form})


def delete_story(request,story_id):
    """
    :param request: Django request object
    :param story_id: id of the story to delete
    :return: redirects to home page
    """
    story = get_story_object(request=request, story_id=story_id)
    story.delete()
    return HttpResponseRedirect(reverse('stories_view'))


def up_vote_story(request, story_id):
    """
    :param request: Django request object
    :param story_id: id of the story to be up voted
    :return:redirects to home page
    """
    story = get_story_object(request=request, story_id=story_id)
    story.up_vote = F('up_vote') + 1
    story.save()
    return HttpResponseRedirect(reverse('stories_view'))


def down_vote_story(request,story_id):
    """
    :param request: Django request object
    :param story_id: id of the story to be down voted
    :return: redirects to home page
    """
    story = get_story_object(request=request, story_id=story_id)
    story.down_vote = F('down_vote') + 1
    story.save()
    return HttpResponseRedirect(reverse('stories_view'))


# Comment views
class GetCommentsView(View):
    def get(self, request, story_id):
        """
        return top 25 comments on a story
        :param request: Django request object
        :param story_id: id of the story whose comments are to displayed
        :return: renders to template to display top 25 comments on the story
        """
        story = get_story_object(request, story_id)
        comments = Comment.objects.filter(story=story_id).order_by('-posted_on')[:25]
        message = ''
        if not comments:
            message = "No comments to show"
        return render(request, 'stories/display_comments.html', {'comments': comments, 'story': story,
                                                                 'message': message})


class EditCommentView(View):
    def get(self, request, story_id, comment_id):
        """
        :param request: Django request object
        :param story_id: id of the story whose comment is to be edited
        :param comment_id: id of the comment to be edited
        :return:  renders a template to edit a comment
        """
        comment = get_comment_object(request, comment_id)
        comment_form = CreateCommentForm(instance=comment)
        return render(request, 'stories/edit_comment.html', {'form': comment_form, 'param': 'edit'})

    def post(self, request, story_id, comment_id):
        """
        :param request: Django request object
        :param story_id: id of the story whose comment is to be edited
        :param comment_id: id of the comment to be edited
        :return: redirects to single story view page
        """
        comment = get_comment_object(request, comment_id)
        comment_form = CreateCommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            comment_form.save()
            return HttpResponseRedirect(reverse('get_story_view', args=[story_id]))
        return render(request, 'stories/edit_comment.html', {'form': comment_form, 'param': 'edit'})


def create_comment(request, story_id):
    """
    :param request: Django request object
    :param story_id: id of the story on which comment is posted
    :return: redirects to single story view page
    """
    story = get_story_object(request=request, story_id=story_id)
    comment_form = CreateCommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.story = story
        comment.save()
        return HttpResponseRedirect(reverse('get_story_view', args=[story_id]))
    return render(request, 'stories/display_story.html',{'form': comment_form, 'param': 'create', 'story': story})


def delete_comment(request, story_id, comment_id):
    """
    :param request: Django request object
    :param story_id: id of the story whose comment is to be deleted
    :param comment_id: id of comment to be deleted
    :return: redirects to single story view page
    """
    comment = get_comment_object(request, comment_id)
    comment.delete()
    return HttpResponseRedirect(reverse('get_story_view', args=[story_id]))


class AdminView(View):
    def get(self, request):
        """
        :param request: Django Request object
        :return renders a template for an admin to archive a story
        """
        stories = Story.objects.all().order_by('-created_on')
        return render(request, 'stories/home.html', {'stories': stories, 'param': 'admin', 'form': CreateStoryForm()})

    def post(self, request):
        """
        archive a story so that it does not show up in the home page
        :param request: Django request object
        :return redirects to home page
        """
        archive_list = request.POST.getlist('archives')
        Story.objects.filter(id__in=archive_list).update(archive=True)
        Story.objects.exclude(id__in=archive_list).update(archive=False)
        return HttpResponseRedirect(reverse('stories_view'))






