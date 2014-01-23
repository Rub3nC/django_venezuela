# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Estado'
        db.create_table(u'venezuela_estado', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('estado', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'venezuela', ['Estado'])


    def backwards(self, orm):
        # Deleting model 'Estado'
        db.delete_table(u'venezuela_estado')


    models = {
        u'venezuela.estado': {
            'Meta': {'object_name': 'Estado'},
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['venezuela']