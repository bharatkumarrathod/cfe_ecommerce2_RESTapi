from django.db import models


class SignUp(models.Model):

    email = models.EmailField()
    full_name = models.CharField(blank=True, null=True, max_length=255)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    # DEBUG ONLY ## Use this when manually adding dates.
    # created = models.DateTimeField(auto_now_add=False, editable=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.email
