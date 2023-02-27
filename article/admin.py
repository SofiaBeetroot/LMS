from article.models import *


class CommentsInline(admin.StackedInline):
    model = Comments
    extra = 2


class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'creation_date', 'was_published_recently')
    fieldsets = [(None, {'fields': ['title', 'subtitle', 'text']}),
                 ('Additional info', {'fields': ['url', 'type']}),
                 ('Created by', {'fields': ['author']})]
    inlines = [CommentsInline]
    list_filter = ['type', 'creation_date', 'author']
    search_fields = ['title']


admin.site.register(Topic, TopicAdmin)
admin.site.register(Comments)
