from django.db import models
from django.utils.functional import cached_property


class AvailableManager(models.Manager):

    def available(self, include_qs = None, include_obj = None):
        """
        Returns a QuerySet containing only available instances
        (i.e. not selected previously)
        """
        qs = self.all()
        available_qs = self.all()

        for obj in qs:
            if include_qs:
                if not obj.available and include_qs.filter(id=obj.id).count() == 0:
                    available_qs = available_qs.exclude(id=obj.id)
            elif include_obj:
                if not obj.available and obj.id != include_obj.id:
                    available_qs = available_qs.exclude(id=obj.id)
            else:
                if not obj.available:
                    available_qs = available_qs.exclude(id=obj.id)

        return available_qs


class AvailableModelMixin(object):
    """
    Mixin containing available property
    """
    @cached_property
    def available(self):
        """
        Determines whether the model instance has already been selected
        in a related field (ManyToManyField, OneToOneField).
        """
        fields = self._meta.get_fields()

        for field in fields:
            if isinstance(field, models.ManyToManyRel):
                attr = field.get_accessor_name()

                if getattr(self, attr).count() > 0:
                    return False

            elif isinstance(field, models.OneToOneRel):
                attr = field.get_accessor_name()
                if getattr(self, attr, None):
                    return False

        return True


class AvailableModel(AvailableModelMixin, models.Model):

    objects = AvailableManager()

    class Meta:
        abstract = True
