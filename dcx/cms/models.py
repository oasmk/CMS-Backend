from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.FileField(upload_to='projects/')
    on_display = models.BooleanField(default=True)


class Inquiry(models.Model):
    name = models.CharField(max_length=150)
    contact_no = models.CharField(max_length=14, null=True, blank=True)
    email_id = models.EmailField(null=True, blank=True)
    message = models.TextField(blank=True)


class Testimonial(models.Model):
    name = models.CharField(max_length=150)
    designation = models.CharField(max_length=150)
    testimonial = models.TextField()
    image = models.FileField(upload_to='testimonials/')
    on_display = models.BooleanField(default=True)
