from django.db import models

# TODO write all of your code here...

class Author(models.Model):
    name = models.CharField(max_length=50)


class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def copy(self):
        blg_post = BlogPost.objects.get(pk=self.pk)
        cmmnts = blg_post.comment_set.all()

        blg_post.pk = None
        blg_post.save()

        for cmnt in cmmnts:
            cmnt.pk = None
            cmnt.blog_post = blg_post
            cmnt.save()

        return blg_post.pk


class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)