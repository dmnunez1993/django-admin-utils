# django-admin-utils

Set of tools I commonly use in the admin interface on django projects

## How to use

To hide a particular model from the admin (but keeping the models registered):

    from package.models import model

    from admin_utils import HiddenAdmin

    admin.site.register(model, HiddenAdmin)

Additionaly, if it is necessary to modify admin behaviour from that model (i. e. Remove fields, add custom methods), there is a mixin called HiddenAdminMixin which can be used alongside admin.ModelAdmin:

    from package.models import model

    from admin_utils import HiddenAdminMixin

    class ModelAdmin(HiddenAdminMixin, admin.ModelAdmin):
        ...
