from django.contrib import admin

from eventlog.models import Log


class LogAdmin(admin.ModelAdmin):
    
    def queryset(self, request):
        qs = super(LogAdmin, self).queryset(request)
        return qs.select_related("user")
    
    def get_queryset(self, request):
        return self.queryset(request)
    
    raw_id_fields = ["user"]
    list_filter = ["action", "timestamp"]
    list_display = ["timestamp", "user", "action", "extra"]
    search_fields = ["user__username", "user__email", "extra"]


admin.site.register(Log, LogAdmin)
