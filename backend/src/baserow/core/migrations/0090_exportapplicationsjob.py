# Generated by Django 4.2.13 on 2024-08-26 08:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0089_alter_snapshot_unique_together"),
    ]

    operations = [
        migrations.CreateModel(
            name="ExportApplicationsJob",
            fields=[
                (
                    "job_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="core.job",
                    ),
                ),
                (
                    "user_ip_address",
                    models.GenericIPAddressField(
                        help_text="The user IP address.", null=True
                    ),
                ),
                (
                    "user_websocket_id",
                    models.CharField(
                        help_text="The user websocket uuid needed to manage signals sent correctly.",
                        max_length=36,
                        null=True,
                    ),
                ),
                (
                    "user_session_id",
                    models.CharField(
                        help_text="The user session uuid needed for undo/redo functionality.",
                        max_length=36,
                        null=True,
                    ),
                ),
                (
                    "user_action_group_id",
                    models.CharField(
                        help_text="The user session uuid needed for undo/redo action group functionality.",
                        max_length=36,
                        null=True,
                    ),
                ),
                (
                    "workspace_id",
                    models.PositiveIntegerField(
                        help_text="The workspace id that the applications are going to be exported from."
                    ),
                ),
                (
                    "application_ids",
                    models.TextField(
                        help_text="The comma separated list of application ids that are going to be exported."
                    ),
                ),
                (
                    "only_structure",
                    models.BooleanField(
                        default=False,
                        help_text="Indicates if only the structure of the applications should be exported, without user data.",
                    ),
                ),
                (
                    "exported_file_name",
                    models.TextField(
                        blank=True, help_text="The name of the exported archive file."
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("core.job", models.Model),
        ),
    ]