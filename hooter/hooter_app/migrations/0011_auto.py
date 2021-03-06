# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field abonnes on 'Utilisateur'
        m2m_table_name = db.shorten_name(u'hooter_app_utilisateur_abonnes')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_utilisateur', models.ForeignKey(orm[u'hooter_app.utilisateur'], null=False)),
            ('to_utilisateur', models.ForeignKey(orm[u'hooter_app.utilisateur'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_utilisateur_id', 'to_utilisateur_id'])


    def backwards(self, orm):
        # Removing M2M table for field abonnes on 'Utilisateur'
        db.delete_table(db.shorten_name(u'hooter_app_utilisateur_abonnes'))


    models = {
        u'hooter_app.hashtag': {
            'Meta': {'object_name': 'Hashtag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'messages': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['hooter_app.Message']", 'symmetrical': 'False', 'blank': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'hooter_app.message': {
            'Meta': {'object_name': 'Message'},
            'contenu': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'hashtags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['hooter_app.Hashtag']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'utilisateur': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hooter_app.Utilisateur']"})
        },
        u'hooter_app.utilisateur': {
            'Meta': {'object_name': 'Utilisateur'},
            'abonnements': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'abonnements_rel_+'", 'blank': 'True', 'to': u"orm['hooter_app.Utilisateur']"}),
            'abonnes': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'abonnes_rel_+'", 'blank': 'True', 'to': u"orm['hooter_app.Utilisateur']"}),
            'date_naiss': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mot_passe': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'pays': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'default': "'photos/default.jpeg'", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pseudo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'ville': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['hooter_app']