# Generated by Django 4.2.11 on 2024-05-06 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CLient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statut', models.CharField(blank=True, max_length=10, null=True)),
                ('Nom', models.CharField(blank=True, max_length=500, null=True)),
                ('Prenom', models.CharField(blank=True, max_length=500, null=True)),
                ('code_Postal', models.CharField(blank=True, max_length=50, null=True)),
                ('adresse', models.CharField(blank=True, max_length=200, null=True)),
                ('Age', models.PositiveIntegerField(blank=True, null=True)),
                ('Situation_familiale', models.CharField(blank=True, max_length=100, null=True)),
                ('Nombre_d_enfants', models.FloatField(blank=True, default=0, null=True)),
                ('Ville', models.CharField(blank=True, max_length=100, null=True)),
                ('E_mail', models.EmailField(blank=True, max_length=254, null=True)),
                ('N_de_téléphone', models.CharField(blank=True, max_length=200, null=True)),
                ('Surface_habitable_m2', models.FloatField(blank=True, max_length=100, null=True)),
                ('facture_d_electricite', models.CharField(blank=True, max_length=100, null=True)),
                ('type_de_toiture', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
