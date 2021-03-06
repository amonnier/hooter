# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Message.utilisateur_initial'
        db.add_column(u'hooter_app_message', 'utilisateur_initial',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='utilisateur_initial+', null=True, to=orm['hooter_app.Utilisateur']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Message.utilisateur_initial'
        db.delete_column(u'hooter_app_message', 'utilisateur_initial_id')


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
            'utilisateur': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'utilisateur+'", 'to': u"orm['hooter_app.Utilisateur']"}),
            'utilisateur_initial': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'utilisateur_initial+'", 'null': 'True', 'to': u"orm['hooter_app.Utilisateur']"})
        },
        u'hooter_app.utilisateur': {
            'Meta': {'object_name': 'Utilisateur'},
            'abonnements': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'abonnements+'", 'blank': 'True', 'to': u"orm['hooter_app.Utilisateur']"}),
            'abonnes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'abonnes+'", 'blank': 'True', 'to': u"orm['hooter_app.Utilisateur']"}),
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