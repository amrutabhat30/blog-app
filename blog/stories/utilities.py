from django.core.exceptions import ObjectDoesNotExist

from django.shortcuts import render
import logging

from stories.models import Story, Comment
logger = logging.getLogger(__name__)


def get_comment_object(request, comment_id):
    """
    returns comment object
    :param request:
    :param story_id:
    :param comment_id:
    :return:
    """
    try:
        comment = Comment.objects.get(id=comment_id)
        return comment
    except ObjectDoesNotExist:
        logger.error("Comment does not exist")
        return render(request, 'stories/error.html')


def get_story_object(request, story_id):
    """
    returns story object
    :param request:
    :param story_id:
    :return:
    """
    try:
        story = Story.objects.get(id=story_id)
        return story
    except Story.DoesNotExist:
        logger.error("Story does not exist")
        return render(request, 'stories/error.html')


