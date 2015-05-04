from .models import log


class EventLogMixin(object):

    @property
    def action(self):
        return "{}_{}".format(
            self.action_kind,
            self.model._meta.verbose_name.upper().replace(" ", "_")
        )

    @property
    def extra_data(self):
        return {}

    @property
    def user(self):
        if self.request.user.is_authenticated():
            return self.request.user
        return None

    def log_action(self):
        log(
            user=self.user,
            action=self.action,
            extra=self.extra_data,
            obj=self.object
        )

    def form_valid(self, form):
        response = super(EventLogMixin, self).form_valid(form)
        self.log_action()
        return response
