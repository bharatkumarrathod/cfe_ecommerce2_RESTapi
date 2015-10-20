from django.contrib import admin

from .forms import SignUpForm
from .models import SignUp


# Use this to add more info for each object in the admin site
class SignUpAdmin(admin.ModelAdmin):
    list_display = ["__str__", "created", "updated"]
    form = SignUpForm

    # class Meta:
    #     model = SignUp


# Usually would use this:
# admin.site.register(SignUp)

# now we add the new class here:
admin.site.register(SignUp, SignUpAdmin)
