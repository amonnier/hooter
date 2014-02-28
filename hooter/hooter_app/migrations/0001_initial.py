# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Utilisateur'
        db.create_table(u'hooter_app_utilisateur', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pseudo', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('mot_passe', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('pays', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('ville', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('date_naiss', self.gf('django.db.models.fields.DateField')()),
            ('photo', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'hooter_app', ['Utilisateur'])

        # Adding M2M table for field abonnements on 'Utilisateur'
        m2m_table_name = db.shorten_name(u'hooter_app_utilisateur_abonnements')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_utilisateur', models.ForeignKey(orm[u'hooter_app.utilisateur'], null=False)),
            ('to_utilisateur', models.ForeignKey(orm[u'hooter_app.utilisateur'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_utilisateur_id', 'to_utilisateur_id'])

        # Adding model 'Message'
        db.create_table(u'hooter_app_message', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contenu', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('utilisateur', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hooter_app.Utilisateur'])),
        ))
        db.send_create_signal(u'hooter_app', ['Message'])

        # Adding M2M table for field hashtags on 'Message'
        m2m_table_name = db.shorten_name(u'hooter_app_message_hashtags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('message', models.ForeignKey(orm[u'hooter_app.message'], null=False)),
            ('hashtag', models.ForeignKey(orm[u'hooter_app.hashtag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['message_id', 'hashtag_id'])

        # Adding model 'Hashtag'
        db.create_table(u'hooter_app_hashtag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'hooter_app', ['Hashtag'])

        # Adding M2M table for field messages on 'Hashtag'
        m2m_table_name = db.shorten_name(u'hooter_app_hashtag_messages')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('hashtag', models.ForeignKey(orm[u'hooter_app.hashtag'], null=False)),
            ('message', models.ForeignKey(orm[u'hooter_app.message'], null=False))
        ))
        db.create_unique(m2m_table_name, ['hashtag_id', 'message_id'])


    def backwards(self, orm):
        # Deleting model 'Utilisateur'
        db.delete_table(u'hooter_app_utilisateur')

        # Removing M2M table for field abonnements on 'Utilisateur'
        db.delete_table(db.shorten_name(u'hooter_app_utilisateur_abonnements'))

        # Deleting model 'Message'
        db.delete_table(u'hooter_app_message')

        # Removing M2M table for field hashtags on 'Message'
        db.delete_table(db.shorten_name(u'hooter_app_message_hashtags'))

        # Deleting model 'Hashtag'
        db.delete_table(u'hooter_app_hashtag')

        # Removing M2M table for field messages on 'Hashtag'
        db.delete_table(db.shorten_name(u'hooter_app_hashtag_messages'))


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
            'date': ('django.db.models.fields.DateField', [], {}),
            'hashtags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['hooter_app.Hashtag']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'utilisateur': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hooter_app.Utilisateur']"})
        },
        u'hooter_app.utilisateur': {
            'Meta': {'object_name': 'Utilisateur'},
            'abonnements': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'abonnements_rel_+'", 'blank': 'True', 'to': u"orm['hooter_app.Utilisateur']"}),
            'date_naiss': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mot_passe': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pays': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'photo': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'pseudo': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'ville': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['hooter_app']