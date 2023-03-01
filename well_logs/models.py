from datetime import datetime

from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils import FieldTracker
from model_utils.models import TimeStampedModel

from .querysets import QuerySetExtra


class Operator(TimeStampedModel):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("name",)


class Well(TimeStampedModel):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("name",)


class Log(TimeStampedModel):
    objects = QuerySetExtra.as_manager()

    well = models.ForeignKey(
        Well,
        verbose_name=_("well"),
        related_name="logs",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    operator = models.ForeignKey(
        Operator,
        verbose_name=_("well"),
        related_name="logs",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    start_time = models.DateTimeField(
        blank=True, null=True, validators=[MaxValueValidator(datetime.now)]
    )
    finish_time = models.DateTimeField(
        blank=True, null=True, validators=[MaxValueValidator(datetime.now)]
    )

    comment = models.TextField(_("comments"), blank=True, null=True)

    values = ArrayField(_("uncertainty"), base_field=models.FloatField)

    uncertainties = ArrayField(
        _("uncertainty"), base_field=models.FloatField, null=True, blank=True
    )

    depth = ArrayField(_("depth"), base_field=models.FloatField)
    depth_unit = models.CharField(_("depth unit"), default="m")

    class Meta:
        ordering = ("-start_time",)


class Data(models.Model):
    log = models.ForeignKey(
        Log,
        verbose_name=_("log"),
        related_name="data",
        on_delete=models.CASCADE,
        null=True,
    )

    value = models.FloatField(_("value"))
    uncertainty = models.FloatField(_("uncertainty"), null=True, blank=True)
    depth = models.FloatField(_("depth (m)"))

    class Meta:
        ordering = ["depth"]
        unique_together = ["value", "depth", "log"]
