from django.contrib import admin

from admin_utils.mixins import HiddenAdminMixin


class HiddenAdmin(HiddenAdminMixin, admin.ModelAdmin):
    pass
