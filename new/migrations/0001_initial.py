# Generated by Django 5.0.6 on 2024-11-27 10:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Answer",
            fields=[
                ("ans_id", models.AutoField(primary_key=True, serialize=False)),
                ("answer_text", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="JobPost",
            fields=[
                ("post_id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=100)),
                ("education_requirement", models.CharField(max_length=100)),
                ("deadline", models.DateField()),
                ("description", models.TextField()),
                ("location", models.CharField(max_length=100)),
                ("job_type", models.CharField(max_length=100)),
                ("years_experience", models.PositiveIntegerField()),
                ("key_responsibilities", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="JobSeeker",
            fields=[
                ("js_id", models.AutoField(primary_key=True, serialize=False)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("fname", models.CharField(max_length=100)),
                ("lname", models.CharField(max_length=100)),
                ("password", models.CharField(max_length=128)),
                ("address", models.TextField()),
                ("education", models.TextField()),
                ("resume", models.FileField(upload_to="resumes/")),
            ],
        ),
        migrations.CreateModel(
            name="Recruiter",
            fields=[
                ("r_id", models.AutoField(primary_key=True, serialize=False)),
                ("fname", models.CharField(max_length=100)),
                ("lname", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("password", models.CharField(max_length=128)),
                ("address", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Assessment",
            fields=[
                ("asses_id", models.AutoField(primary_key=True, serialize=False)),
                ("marks", models.JSONField()),
                (
                    "answer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="assessments",
                        to="new.answer",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Bookmark",
            fields=[
                ("bm_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "job_post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="bookmarks",
                        to="new.jobpost",
                    ),
                ),
                (
                    "job_seeker",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="bookmarks",
                        to="new.jobseeker",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Application",
            fields=[
                ("app_id", models.AutoField(primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "job_post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="applications",
                        to="new.jobpost",
                    ),
                ),
                (
                    "job_seeker",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="applications",
                        to="new.jobseeker",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Question",
            fields=[
                ("ques_id", models.AutoField(primary_key=True, serialize=False)),
                ("question_text", models.TextField()),
                (
                    "application",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="questions",
                        to="new.application",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="answer",
            name="question",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="answers",
                to="new.question",
            ),
        ),
        migrations.AddField(
            model_name="jobpost",
            name="recruiter",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="job_posts",
                to="new.recruiter",
            ),
        ),
        migrations.CreateModel(
            name="Company",
            fields=[
                ("c_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("address", models.TextField()),
                ("description", models.TextField()),
                ("trade_license_number", models.CharField(max_length=100, unique=True)),
                (
                    "recruiter",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="companies",
                        to="new.recruiter",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Skill",
            fields=[
                ("skill_id", models.AutoField(primary_key=True, serialize=False)),
                ("skill_name", models.CharField(max_length=100)),
                (
                    "job_seeker",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="skills",
                        to="new.jobseeker",
                    ),
                ),
            ],
        ),
    ]