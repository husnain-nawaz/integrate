from django.contrib import admin
from . models import Project,project_formal,project_casual,project_reviews,footer
# Register your models here.

admin.site.register(Project)
admin.site.register(project_formal)
admin.site.register(project_casual)
admin.site.register(project_reviews)

# can remove
admin.site.register(footer)

