from django.contrib import admin


class HiddenAdminMixin(object):

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class HiddenAdmin(HiddenAdminMixin, admin.ModelAdmin):
    pass
