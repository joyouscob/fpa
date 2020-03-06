from django.db import models
# import the timezone module for date and time
from django.utils import timezone
#import the user model from django
from django.contrib.auth.models import User

class HomeSettings(models.Model):
    mini_header_right = models.TextField(default=None)
    phone = models.CharField(max_length=100, null=True, default=None)
    email = models.EmailField(max_length=100, null=True, default=None)
    video = models.FileField(null=True, default="wavy.mp4", upload_to='media/')
    title = models.CharField(max_length=100)
    content = models.TextField(default=None)
    link = models.URLField(default=None)
    section1 = models.TextField(default=None)
    section2 = models.TextField(default=None)
    footer = models.TextField(default=None)
    copyright_text = models.TextField(default=None)
    # The default site name e.g NIHSA - Nigeria Metrological Agency...
    site_name = models.CharField(max_length=100, null=True, default=None)
    # Top of Page Notification
    toppage_notification = models.CharField(max_length=500, null=True, default=None)
    edited_by = models.ForeignKey(User, default=None, null=True, on_delete=models.PROTECT)
    date_posted = models.DateTimeField(default=timezone.now)
    website = models.CharField(max_length=100, null=True, default=None)
    active = models.BooleanField(null=True, default=0)

    def __str__(self):
        return self.title


# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=100)
    menu_title = models.CharField(max_length=20, null=True)
    content = models.TextField(default=None)
    # This captures when the post was originally posted and cannot be edited
    date_original_posted = models.DateTimeField(auto_now_add=True)
    publish = models.IntegerField(default=0)
    #Menu Order
    order = models.IntegerField(unique=True, null=True)
    # We importeed the timezone to capture the original date and time, this way we can modify it
    date_posted = models.DateTimeField(default=timezone.now)
    # author and editors of page from users table (We imported user)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    slug = models.SlugField(null=False, unique=True)
    header_img = models.ImageField(null=True, upload_to='images/')

    #whenever we query the database, it returns by default with the slug field
    def __str__(self):
        return self.title

    #We need to change the default id/pk that over to a keyword argument,
    #kwargs, for our slug
    def get_absolute_url(self):
        return reverse('page-detail', kwargs={'slug': self.slug})
        # we override the default django save method so we
        # can auto generate our slug
    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     return super().save(*args, **kwargs)

    #we are overriding the default django for images save method in our models
    def save(self):
        #run the main save
        super().save()
        #open the current saved image
        img = Image.open(self.header_img.path)
        #check the size and resize
        if img.height >800 or img.width > 800:
            output_size = (800, 800)
            img.thumbnail(output_size)
            img.save(self.header_img.path)




#Menu
class Menu(models.Model):
    # menu_title: Menu Title, page_id = The Page that will load,
    # date_created: The Day this was created
    title = models.CharField(max_length=20)
    page = models.ForeignKey(Page, on_delete=models.SET_NULL, null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)

    #whenever we query the database, it returns by default with the title field
    def __str__(self):
        return self.title



# Submenu
class Submenu(models.Model):
    # title: Menu Title, page_id = The Page that will load,
    # date_created: The Day this was created
    title = models.CharField(max_length=20)
    #Nested under which menu
    menuid = models.ForeignKey(Menu, on_delete=models.PROTECT)
    #Attached to which page
    page = models.ForeignKey(Page, on_delete=models.PROTECT)
    date_created = models.DateTimeField(default=timezone.now)

    #whenever we query the database, it returns by default with the title field
    def __str__(self):
        return self.title



# Blog Post
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # This captures when the post was originally posted and cannot be edited
    date_original_posted = models.DateTimeField(auto_now_add=True)
    # We importeed the timezone to capture the original date and time, this way we can modify it
    date_posted = models.DateTimeField(default=timezone.now)
    # author of posts from author table (We imported user) and delete if user is delete
    author = models.ForeignKey(User, on_delete=models.PROTECT, default=None)
    slug = models.SlugField(null=False, unique=True)
    featured_image = models.ImageField(null=True, default="post.jpg", upload_to='images/')

    #whenever we query the database, it returns by default with the title field
    def __str__(self):
        return self.title

    #We need to change the default id/pk that over to a keyword argument,
    #kwargs, for our slug
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug': self.slug})
        # we override the default django save method so we
        # can auto generate our slug
    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     return super().save(*args, **kwargs)


# Stories From The General Public
class Stories(models.Model):
    title = models.CharField(null=True, max_length=100, default="Story")
    #User can write on their experiences and share youtube links
    content = models.TextField()
    #User can upload pictures to box, or dropbox and share link
    video_link = models.URLField(null=True, default=None)
    # We importeed the timezone to capture the original date and time, this way we can modify it
    date_posted = models.DateTimeField(default=timezone.now)
    # author of story details
    name = models.CharField(null=True, max_length=100)
    email = models.EmailField(null=True, max_length=100, default=None)
    phone = models.CharField(null=True, max_length=11, default=None)

    slug = models.SlugField(null=True, unique=True)

    #whenever we query the database, it returns by default with the title field
    def __str__(self):
        return str(self.title)


class Setting(models.Model):
    # The default site name e.g NIHSA - Nigeria Metrological Agency...
    site_name = models.CharField(max_length=100)
    # Top of Page Notification
    toppage_notification = models.CharField(max_length=500)
    edited_by = models.ForeignKey(User, default=None, null=True, on_delete=models.PROTECT)
    website = models.CharField(max_length=100)

    def __str__(self):
        return self.site_name
