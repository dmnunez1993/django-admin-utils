from django.forms import ModelForm
from django.db.models import OneToOneField, ManyToManyField


class UniqueRelatedForm(ModelForm):
    """
    Prevents already selected objects from showing up in
    related field choices(i.e. OneToOneField, ManyToManyField)
    For this to work, it is necessary to implement
    available property (models.AvailableModel)
    in the related models, otherwise it will be handled
    as a regular form
    """

    def __init__(self, *args, **kwargs):
        super(UniqueRelatedForm, self).__init__(*args, **kwargs)

        opts = self._meta

        model = opts.model


        for field in model._meta.get_fields():
            try:
                if isinstance(field, ManyToManyField):
                    model = field.rel.to
                    field_name = field.name

                    qs = self.get_available_m2m_qs(model, field_name)

                    self.set_qs_for_field(field_name, qs)

                elif isinstance(field, OneToOneField):
                    model = field.rel.to
                    field_name = field.name

                    qs = self.get_available_o2o_qs(model, field_name)

                    self.set_qs_for_field(field_name, qs)

            except AttributeError:
                pass


    def get_available_m2m_qs(model, field_name):
        """
        Returns a QuerySet containing only available models
        (i.e. not selected previously) for a ManyToManyField
        """
        try:
            qs = model.objects.available(
                include_qs=getattr(self.instance, field_name)
            )
        except:
            qs = model.objects.available()

        return qs

    def get_available_o2o_qs(model, field):
        """
        Returns a QuerySet containing only available models
        (i.e. not selected previously) for a OneToOneField
        """
        try:
            qs = model.objects.available(
                include_obj=getattr(self.instance, field_name)
            )

        except:
            qs = model.objects.available()

        return qs

    def set_qs_for_field(field_name, qs)
        self.fields[field_name] = qs
