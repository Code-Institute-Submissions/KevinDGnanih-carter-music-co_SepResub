# Generated by Django 3.2 on 2022-08-30 01:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_testimony_review_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testimony',
            name='name',
        ),
        migrations.AlterField(
            model_name='testimony',
            name='item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='testimony', to='products.product'),
        ),
        migrations.AlterField(
            model_name='testimony',
            name='review_score',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0),
        ),
    ]