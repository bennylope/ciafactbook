# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'InternationalOrganization'
        db.create_table(u'intl_orgs_internationalorganization', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('lat', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=13, decimal_places=10, blank=True)),
            ('lng', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=13, decimal_places=10, blank=True)),
        ))
        db.send_create_signal(u'intl_orgs', ['InternationalOrganization'])


    def backwards(self, orm):
        # Deleting model 'InternationalOrganization'
        db.delete_table(u'intl_orgs_internationalorganization')


    models = {
        u'intl_orgs.internationalorganization': {
            'Meta': {'object_name': 'InternationalOrganization'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '13', 'decimal_places': '10', 'blank': 'True'}),
            'lng': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '13', 'decimal_places': '10', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        }
    }

    complete_apps = ['intl_orgs']