# -*- coding: utf-8 -*-
from django.db import models


class Estado(models.Model):
    estado = models.CharField(max_length=50)

    def __unicode__(self):
        return self.estado

    class Meta:
        verbose_name = u'Estado'
        verbose_name_plural = u'Estados'


class Ciudad(models.Model):
    estado = models.ForeignKey('Estado')
    ciudad = models.CharField(max_length=100)
    capital = models.CharField(max_length=100)

    def __unicode__(self):
        return self.ciudad

    class Meta:
        verbose_name = u'Ciudad'
        verbose_name_plural = u'Ciudades'