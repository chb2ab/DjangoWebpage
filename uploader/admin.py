from django.contrib import admin
from uploader.models import Document, Report, Folder, Group2
# Register your models here.
admin.site.register(Folder)
admin.site.register(Document)
admin.site.register(Report)
admin.site.register(Group2)
