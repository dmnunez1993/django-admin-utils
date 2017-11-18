# django-admin-utils

Set of tools I commonly use in the admin interface on django projects

## How to use

#### Hidden Admin

To hide a particular model from the admin (but keeping the models registered):

    from app.models import MyModel

    from admin_utils import HiddenAdmin

    admin.site.register(MyModel, HiddenAdmin)

Additionaly, if it is necessary to modify admin behaviour from that model (i. e. Remove fields, add custom methods), there is a mixin called HiddenAdminMixin which can be used alongside admin.ModelAdmin:

    from app.models import MyModel

    from admin_utils import HiddenAdminMixin

    class MyModelAdmin(HiddenAdminMixin, admin.ModelAdmin):
        ...

#### Unique Related Form

To hide instances previously selected in related fields, you need to do the following:

    from admin_utils.models import AvailableModel

    class MyModel(AvailableModel):
        ...

Then, in admin.py:

    from app.models import MyModel

    from admin_utils.forms import UniqueRelatedForm

    class MyForm(UniqueRelatedForm):

        class Meta:
            model = MyModel
            fields = '__all__'


    class MyModelAdmin(admin.ModelAdmin):
        form = MyForm


    admin.site.register(MyModel, MyModelAdmin)
