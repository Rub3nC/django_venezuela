# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Municipio'
        db.create_table(u'venezuela_municipio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('estado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['venezuela.Estado'])),
            ('municipio', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'venezuela', ['Municipio'])


    def backwards(self, orm):
        # Deleting model 'Municipio'
        db.delete_table(u'venezuela_municipio')


    models = {
        u'venezuela.ciudad': {
            'Meta': {'object_name': 'Ciudad'},
            'capital': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ciudad': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['venezuela.Estado']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'venezuela.estado': {
            'Meta': {'object_name': 'Estado'},
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'venezuela.municipio': {
            'Meta': {'object_name': 'Municipio'},
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['venezuela.Estado']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['venezuela']