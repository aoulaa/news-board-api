from blog.models import Upvote


def delete():
    Upvote.objects.all().delete()
