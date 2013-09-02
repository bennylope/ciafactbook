# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field members on 'InternationalOrganization'
        m2m_table_name = db.shorten_name(u'intl_orgs_internationalorganization_members')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('internationalorganization', models.ForeignKey(orm[u'intl_orgs.internationalorganization'], null=False)),
            ('country', models.ForeignKey(orm[u'countries.country'], null=False))
        ))
        db.create_unique(m2m_table_name, ['internationalorganization_id', 'country_id'])


    def backwards(self, orm):
        # Removing M2M table for field members on 'InternationalOrganization'
        db.delete_table(db.shorten_name(u'intl_orgs_internationalorganization_members'))


    models = {
        u'countries.country': {
            'Meta': {'object_name': 'Country'},
            'background': ('django.db.models.fields.TextField', [], {}),
            'government_type': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '13', 'decimal_places': '10', 'blank': 'True'}),
            'lng': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '13', 'decimal_places': '10', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'population': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'})
        },
        u'intl_orgs.internationalorganization': {
            'Meta': {'object_name': 'InternationalOrganization'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '13', 'decimal_places': '10', 'blank': 'True'}),
            'lng': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '13', 'decimal_places': '10', 'blank': 'True'}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'orgs'", 'symmetrical': 'False', 'to': u"orm['countries.Country']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        }
    }

    complete_apps = ['intl_orgs']