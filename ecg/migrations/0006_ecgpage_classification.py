# Generated by Django 4.2.9 on 2024-05-05 17:13

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ecg', '0005_remove_ecgpage_classification'),
    ]

    operations = [
        migrations.AddField(
            model_name='ecgpage',
            name='classification',
            field=wagtail.fields.StreamField([('prediction', wagtail.blocks.StructBlock([('label', wagtail.blocks.ChoiceBlock(choices=[('F', 'F'), ('M', 'M'), ('N', 'N'), ('V', 'V'), ('S', 'S'), ('Q', 'Q')], help_text='Choose Label')), ('description', wagtail.blocks.RichTextBlock(features=['bold', 'italic', 'link'], help_text='Some Description'))]))], blank=True, use_json_field=True),
        ),
    ]