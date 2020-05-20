from .models import log


class EventLogMixin:

    @property
    def action(self):
        return f"{self.action_kind}_{self.model._meta.verbose_name.upper().replace(' ', '_')}"

    @property
    def extra_data(self):
        return {}

    @property
    def user(self):
        if self.request.user.is_authenticated:
            return self.request.user
        return None

    def log_action(self):
        log(
            user=self.user,
            action=self.action,
            extra=self.extra_data,
            obj=getattr(self, "object", None)
        )

    def form_valid(self, form):
        response = super().form_valid(form)
        self.log_action()
        return response
