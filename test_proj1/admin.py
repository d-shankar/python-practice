from django.contrib import admin
from test_proj1.model.practice import Topic, AccessRecord, Webpage
from test_proj1.model.user import User

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(User)