# Generated by Django 5.1.3 on 2024-11-28 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='media_files/')),
                ('name', models.CharField(max_length=255)),
                ('name_af', models.CharField(max_length=255, null=True)),
                ('name_ar', models.CharField(max_length=255, null=True)),
                ('name_ar_dz', models.CharField(max_length=255, null=True)),
                ('name_ast', models.CharField(max_length=255, null=True)),
                ('name_az', models.CharField(max_length=255, null=True)),
                ('name_bg', models.CharField(max_length=255, null=True)),
                ('name_be', models.CharField(max_length=255, null=True)),
                ('name_bn', models.CharField(max_length=255, null=True)),
                ('name_br', models.CharField(max_length=255, null=True)),
                ('name_bs', models.CharField(max_length=255, null=True)),
                ('name_ca', models.CharField(max_length=255, null=True)),
                ('name_ckb', models.CharField(max_length=255, null=True)),
                ('name_cs', models.CharField(max_length=255, null=True)),
                ('name_cy', models.CharField(max_length=255, null=True)),
                ('name_da', models.CharField(max_length=255, null=True)),
                ('name_de', models.CharField(max_length=255, null=True)),
                ('name_dsb', models.CharField(max_length=255, null=True)),
                ('name_el', models.CharField(max_length=255, null=True)),
                ('name_en', models.CharField(max_length=255, null=True)),
                ('name_en_au', models.CharField(max_length=255, null=True)),
                ('name_en_gb', models.CharField(max_length=255, null=True)),
                ('name_eo', models.CharField(max_length=255, null=True)),
                ('name_es', models.CharField(max_length=255, null=True)),
                ('name_es_ar', models.CharField(max_length=255, null=True)),
                ('name_es_co', models.CharField(max_length=255, null=True)),
                ('name_es_mx', models.CharField(max_length=255, null=True)),
                ('name_es_ni', models.CharField(max_length=255, null=True)),
                ('name_es_ve', models.CharField(max_length=255, null=True)),
                ('name_et', models.CharField(max_length=255, null=True)),
                ('name_eu', models.CharField(max_length=255, null=True)),
                ('name_fa', models.CharField(max_length=255, null=True)),
                ('name_fi', models.CharField(max_length=255, null=True)),
                ('name_fr', models.CharField(max_length=255, null=True)),
                ('name_fy', models.CharField(max_length=255, null=True)),
                ('name_ga', models.CharField(max_length=255, null=True)),
                ('name_gd', models.CharField(max_length=255, null=True)),
                ('name_gl', models.CharField(max_length=255, null=True)),
                ('name_he', models.CharField(max_length=255, null=True)),
                ('name_hi', models.CharField(max_length=255, null=True)),
                ('name_hr', models.CharField(max_length=255, null=True)),
                ('name_hsb', models.CharField(max_length=255, null=True)),
                ('name_hu', models.CharField(max_length=255, null=True)),
                ('name_hy', models.CharField(max_length=255, null=True)),
                ('name_ia', models.CharField(max_length=255, null=True)),
                ('name_ind', models.CharField(max_length=255, null=True)),
                ('name_ig', models.CharField(max_length=255, null=True)),
                ('name_io', models.CharField(max_length=255, null=True)),
                ('name_is', models.CharField(max_length=255, null=True)),
                ('name_it', models.CharField(max_length=255, null=True)),
                ('name_ja', models.CharField(max_length=255, null=True)),
                ('name_ka', models.CharField(max_length=255, null=True)),
                ('name_kab', models.CharField(max_length=255, null=True)),
                ('name_kk', models.CharField(max_length=255, null=True)),
                ('name_km', models.CharField(max_length=255, null=True)),
                ('name_kn', models.CharField(max_length=255, null=True)),
                ('name_ko', models.CharField(max_length=255, null=True)),
                ('name_ky', models.CharField(max_length=255, null=True)),
                ('name_lb', models.CharField(max_length=255, null=True)),
                ('name_lt', models.CharField(max_length=255, null=True)),
                ('name_lv', models.CharField(max_length=255, null=True)),
                ('name_mk', models.CharField(max_length=255, null=True)),
                ('name_ml', models.CharField(max_length=255, null=True)),
                ('name_mn', models.CharField(max_length=255, null=True)),
                ('name_mr', models.CharField(max_length=255, null=True)),
                ('name_ms', models.CharField(max_length=255, null=True)),
                ('name_my', models.CharField(max_length=255, null=True)),
                ('name_nb', models.CharField(max_length=255, null=True)),
                ('name_ne', models.CharField(max_length=255, null=True)),
                ('name_nl', models.CharField(max_length=255, null=True)),
                ('name_nn', models.CharField(max_length=255, null=True)),
                ('name_os', models.CharField(max_length=255, null=True)),
                ('name_pa', models.CharField(max_length=255, null=True)),
                ('name_pl', models.CharField(max_length=255, null=True)),
                ('name_pt', models.CharField(max_length=255, null=True)),
                ('name_pt_br', models.CharField(max_length=255, null=True)),
                ('name_ro', models.CharField(max_length=255, null=True)),
                ('name_ru', models.CharField(max_length=255, null=True)),
                ('name_sk', models.CharField(max_length=255, null=True)),
                ('name_sl', models.CharField(max_length=255, null=True)),
                ('name_sq', models.CharField(max_length=255, null=True)),
                ('name_sr', models.CharField(max_length=255, null=True)),
                ('name_sr_latn', models.CharField(max_length=255, null=True)),
                ('name_sv', models.CharField(max_length=255, null=True)),
                ('name_sw', models.CharField(max_length=255, null=True)),
                ('name_ta', models.CharField(max_length=255, null=True)),
                ('name_te', models.CharField(max_length=255, null=True)),
                ('name_tg', models.CharField(max_length=255, null=True)),
                ('name_th', models.CharField(max_length=255, null=True)),
                ('name_tk', models.CharField(max_length=255, null=True)),
                ('name_tr', models.CharField(max_length=255, null=True)),
                ('name_tt', models.CharField(max_length=255, null=True)),
                ('name_udm', models.CharField(max_length=255, null=True)),
                ('name_ug', models.CharField(max_length=255, null=True)),
                ('name_uk', models.CharField(max_length=255, null=True)),
                ('name_ur', models.CharField(max_length=255, null=True)),
                ('name_uz', models.CharField(max_length=255, null=True)),
                ('name_vi', models.CharField(max_length=255, null=True)),
                ('name_zh_hans', models.CharField(max_length=255, null=True)),
                ('name_zh_hant', models.CharField(max_length=255, null=True)),
                ('type', models.CharField(choices=[('icon', 'Icon'), ('gif', 'Gif'), ('video', 'Video'), ('image', 'Image'), ('logo', 'Logo')], max_length=10)),
            ],
        ),
    ]
