from django import template
from stories.models import Comment

register = template.Library()


@register.simple_tag
def get_verbose_field_name(instance, field_name):

    """
    Returns verbose_name for a field.
    """

    return instance._meta.get_field(field_name).verbose_name.title()


@register.simple_tag
def get_comments(story_id):
    """
    Returns latest 10 comments for a story
    """
    comments = Comment.objects.filter(story=story_id).order_by('-posted_on')[:10]
    return comments