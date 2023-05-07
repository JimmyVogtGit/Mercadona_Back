# Generated by Django 3.2.18 on 2023-05-05 22:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categorie',
            new_name='Category',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='nom',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='produit',
            old_name='categorie',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='produit',
            old_name='description',
            new_name='describe',
        ),
        migrations.RenameField(
            model_name='produit',
            old_name='prix',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='produit',
            old_name='libelle',
            new_name='wording',
        ),
        migrations.RenameField(
            model_name='promotion',
            old_name='nom',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='promotion',
            old_name='pourcentage',
            new_name='percentage',
        ),
    ]