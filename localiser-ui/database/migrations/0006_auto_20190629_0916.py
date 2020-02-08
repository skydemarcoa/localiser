# Generated by Django 2.2.2 on 2019-06-29 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_auto_20190622_0832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='internal_maven_repo_url',
            field=models.CharField(blank=True, help_text='(optional) Internal maven repository URL to deploy the library locally on a dev computer. file:///Users/yourusername/workspace/maven-repo/releases)', max_length=1024, null=True),
        ),
    ]
