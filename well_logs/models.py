from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
from .querysets import QuerySetExtra
from datetime import datetime

def current_year():
    return datetime.now().year

class Operator(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)


class Well(models.Model):
    name = models.CharField(max_length=255)
    class Meta:
        ordering = ('name',)

class Log(models.Model):
    objects = QuerySetExtra.as_manager()
    
    well = models.ForeignKey(Well, 
        verbose_name=_("well"), 
        related_name='logs',
        on_delete=models.CASCADE,
        )

    operator = models.ForeignKey(Operator, 
        verbose_name=_("well"), 
        related_name='logs',
        on_delete=models.SET_NULL,
        blank=True, null=True
        )

    start_time = models.DateTimeField(blank=True, null=True, validators=[MaxValueValidator(datetime.now)])
    finish_time = models.DateTimeField(blank=True, null=True, validators=[MaxValueValidator(datetime.now)])

    comment = models.TextField(_("comments"), blank=True,null=True)
    added = models.DateTimeField(_('date added'), auto_now_add=True)
    modified = models.DateTimeField(_('last modified'), auto_now=True)
        
    class Meta:
        ordering = ("-start_time",)


class Data(models.Model):
    log = models.ForeignKey(Log, 
        verbose_name=_("log"), 
        related_name='data',
        on_delete=models.CASCADE,
        null=True)

    value = models.FloatField(_("value")) 
    uncertainty = models.FloatField(_("uncertainty"), null=True, blank=True)   
    depth = models.FloatField(_("depth (m)"))

    class Meta:
        ordering = ['depth']
        unique_together = ['value', 'depth', 'log']
