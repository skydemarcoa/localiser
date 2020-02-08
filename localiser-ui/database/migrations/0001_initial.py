# Generated by Django 2.2.2 on 2019-06-15 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Locale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='LocalisedKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='TranslatedKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=500)),
                ('localised_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.LocalisedKey')),
                ('slug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Locale')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('organization', models.CharField(max_length=128)),
                ('package', models.CharField(max_length=128)),
                ('short_identifier', models.CharField(max_length=10)),
                ('ios_deployment_target', models.CharField(max_length=10)),
                ('default_language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Locale')),
            ],
        ),
        migrations.CreateModel(
            name='Namespace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Project')),
            ],
        ),
        migrations.AddField(
            model_name='localisedkey',
            name='namespace',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Namespace'),
        ),
        migrations.AddConstraint(
            model_name='translatedkey',
            constraint=models.UniqueConstraint(fields=('localised_key', 'slug'), name='unique_translated_key'),
        ),
        migrations.AddConstraint(
            model_name='namespace',
            constraint=models.UniqueConstraint(fields=('project', 'name'), name='unique_namespace'),
        ),
        migrations.AddConstraint(
            model_name='localisedkey',
            constraint=models.UniqueConstraint(fields=('namespace', 'key'), name='unique_key_in_namespace'),
        ),
    ]
