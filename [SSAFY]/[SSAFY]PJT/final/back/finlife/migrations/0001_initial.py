# Generated by Django 4.2.16 on 2024-11-25 23:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DepositProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_month', models.IntegerField(blank=True)),
                ('fin_prdt_cd', models.TextField(unique=True)),
                ('kor_co_nm', models.TextField()),
                ('fin_prdt_nm', models.TextField()),
                ('join_way', models.TextField()),
                ('mtrt_int', models.TextField()),
                ('spcl_cnd', models.TextField()),
                ('join_deny', models.IntegerField()),
                ('join_member', models.TextField()),
                ('etc_note', models.TextField()),
                ('max_limit', models.IntegerField(blank=True, null=True)),
                ('dcls_strt_day', models.IntegerField(blank=True, null=True)),
                ('dcls_end_day', models.IntegerField(blank=True, null=True)),
                ('fin_co_subm_day', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SavingProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_month', models.IntegerField(blank=True)),
                ('fin_prdt_cd', models.TextField()),
                ('kor_co_nm', models.TextField()),
                ('fin_prdt_nm', models.TextField()),
                ('join_way', models.TextField()),
                ('mtrt_int', models.TextField()),
                ('spcl_cnd', models.TextField()),
                ('join_deny', models.IntegerField()),
                ('join_member', models.TextField()),
                ('etc_note', models.TextField()),
                ('max_limit', models.IntegerField(blank=True, null=True)),
                ('dcls_strt_day', models.IntegerField(blank=True, null=True)),
                ('dcls_end_day', models.IntegerField(blank=True, null=True)),
                ('fin_co_subm_day', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserFavoriteSavings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('saving', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_saving_relations', to='finlife.savingproducts')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_saving_relations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserFavoriteDeposits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deposit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_deposit_relations', to='finlife.depositproducts')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_deposit_relations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='savingproducts',
            name='favorited_by',
            field=models.ManyToManyField(blank=True, related_name='favorited_saving_products', through='finlife.UserFavoriteSavings', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='SavingOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_prdt_cd', models.TextField()),
                ('intr_rate_type_nm', models.CharField(max_length=100)),
                ('rsrv_type_nm', models.CharField(max_length=100)),
                ('intr_rate', models.FloatField()),
                ('intr_rate2', models.FloatField()),
                ('save_trm', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='finlife.savingproducts')),
            ],
        ),
        migrations.AddField(
            model_name='depositproducts',
            name='favorited_by',
            field=models.ManyToManyField(blank=True, related_name='favorited_deposit_products', through='finlife.UserFavoriteDeposits', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='DepositOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_prdt_cd', models.TextField()),
                ('intr_rate_type_nm', models.CharField(max_length=100)),
                ('intr_rate', models.FloatField()),
                ('intr_rate2', models.FloatField()),
                ('save_trm', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='finlife.depositproducts')),
            ],
        ),
        migrations.AddConstraint(
            model_name='userfavoritesavings',
            constraint=models.UniqueConstraint(fields=('user', 'saving'), name='unique_user_saving'),
        ),
        migrations.AddConstraint(
            model_name='userfavoritedeposits',
            constraint=models.UniqueConstraint(fields=('user', 'deposit'), name='unique_user_deposit'),
        ),
        migrations.AddConstraint(
            model_name='savingoptions',
            constraint=models.UniqueConstraint(fields=('product', 'fin_prdt_cd', 'intr_rate_type_nm', 'save_trm'), name='unique_saving_options'),
        ),
        migrations.AddConstraint(
            model_name='depositoptions',
            constraint=models.UniqueConstraint(fields=('product', 'fin_prdt_cd', 'intr_rate_type_nm', 'save_trm'), name='unique_deposit_options'),
        ),
    ]