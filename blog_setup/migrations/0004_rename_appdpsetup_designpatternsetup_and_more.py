# Generated by Django 4.2.4 on 2023-09-05 02:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_setup', '0003_alter_appdpsetup_options_menulink_dpsetup'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AppDPSetup',
            new_name='DesignPatternSetup',
        ),
        migrations.AlterModelOptions(
            name='designpatternsetup',
            options={'verbose_name': 'Design pattern - Setup', 'verbose_name_plural': 'Design pattern - Setup'},
        ),
    ]
