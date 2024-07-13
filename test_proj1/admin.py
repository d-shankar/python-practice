from django.contrib import admin
from test_proj1.model.practice import Topic, AccessRecord, Webpage

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)