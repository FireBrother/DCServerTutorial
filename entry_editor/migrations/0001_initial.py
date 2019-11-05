# Generated by Django 2.0.1 on 2019-11-05 05:42

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EntryEditor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='标题')),
                ('word', models.CharField(default='', max_length=32, verbose_name='词条名')),
                ('cells', jsonfield.fields.JSONField(default=[], verbose_name='内容')),
                ('status', models.CharField(choices=[('UNINITIALIZED', '未初始化'), ('NORMAL', '正常'), ('MERGING', '合并中')], default='NORMAL', max_length=32)),
                ('is_public', models.BooleanField(default=False, verbose_name='是否公开')),
                ('kernel_id', models.UUIDField(null=True, verbose_name='内核id')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
