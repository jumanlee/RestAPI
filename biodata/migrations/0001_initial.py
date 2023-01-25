# Generated by Django 3.0.3 on 2022-06-23 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('auto_increment_id', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('domain_id', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=256)),
                ('start', models.IntegerField(blank=True)),
                ('stop', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organism',
            fields=[
                ('auto_increment_id', models.IntegerField(default=1, unique=True)),
                ('taxa_id', models.CharField(db_index=True, max_length=256, primary_key=True, serialize=False)),
                ('clade', models.CharField(max_length=256)),
                ('genus', models.CharField(blank=True, max_length=256)),
                ('species', models.CharField(blank=True, max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Protein',
            fields=[
                ('auto_increment_id', models.IntegerField(default=1, unique=True)),
                ('protein_id', models.CharField(db_index=True, max_length=256, primary_key=True, serialize=False)),
                ('sequence', models.CharField(blank=True, max_length=40000)),
                ('length', models.IntegerField(blank=True)),
                ('foreign_taxa_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biodata.Organism')),
            ],
        ),
        migrations.CreateModel(
            name='Pfam',
            fields=[
                ('auto_increment_id', models.IntegerField(default=1, unique=True)),
                ('pfam_id', models.CharField(db_index=True, max_length=256, primary_key=True, serialize=False)),
                ('domain_description', models.CharField(max_length=256)),
                ('foreign_domain_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biodata.Domain')),
            ],
        ),
        migrations.AddField(
            model_name='domain',
            name='foreign_protein_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biodata.Protein'),
        ),
    ]