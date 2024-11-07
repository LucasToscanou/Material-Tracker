# Generated by Django 5.1.1 on 2024-10-15 23:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExtremeFormsApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('multiple_choice', 'Multiple Choice'), ('long_answer', 'Long Answer')], default='multiple_choice', max_length=20),
        ),
        migrations.CreateModel(
            name='LongAnswerQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.TextField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='long_answer_question', to='ExtremeFormsApp.question')),
            ],
        ),
        migrations.CreateModel(
            name='MultipleChoiceQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('options', models.JSONField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='multiple_choice_question', to='ExtremeFormsApp.question')),
            ],
        ),
        migrations.DeleteModel(
            name='Option',
        ),
    ]