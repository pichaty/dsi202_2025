# Generated by Django 4.2 on 2025-04-16 14:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_donationcase'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonationRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='donations/')),
                ('urgent', models.BooleanField(default=False)),
                ('urgent_message', models.CharField(blank=True, max_length=200, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('amount_needed', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('amount_raised', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='products/')),
            ],
        ),
        migrations.RenameField(
            model_name='pet',
            old_name='story',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='pet',
            name='age',
        ),
        migrations.RemoveField(
            model_name='pet',
            name='disability',
        ),
        migrations.RemoveField(
            model_name='pet',
            name='personality',
        ),
        migrations.RemoveField(
            model_name='pet',
            name='photo',
        ),
        migrations.AddField(
            model_name='pet',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='pet',
            name='image',
            field=models.ImageField(default='pets/default.jpg', upload_to='pets/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pet',
            name='is_adopted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='pet',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=6),
        ),
        migrations.AlterField(
            model_name='pet',
            name='pet_type',
            field=models.CharField(choices=[('Dog', 'Dog'), ('Cat', 'Cat')], default='Dog', max_length=10),
        ),
        migrations.DeleteModel(
            name='DonationCase',
        ),
        migrations.AddField(
            model_name='donationrequest',
            name='pet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='donation_requests', to='myapp.pet'),
        ),
    ]
