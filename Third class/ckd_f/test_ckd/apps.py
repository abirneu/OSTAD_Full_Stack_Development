from django.apps import AppConfig


class TestCkdConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'test_ckd'

from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.core.exceptions import AppRegistryNotReady

class YourAppConfig(AppConfig):
    name = 'your_app_name'  # Replace with your actual app name

    def ready(self):
        try:
            post_migrate.connect(create_groups, sender=self)
        except AppRegistryNotReady:
            # This might happen during initial setup, but will work on subsequent runs
            pass

def create_groups(sender, **kwargs):
    """
    Creates default groups and permissions after migrations
    """
    from django.contrib.auth.models import Group, Permission
    from django.contrib.contenttypes.models import ContentType
    from django.contrib.auth.management import create_permissions
    
    # Ensure permissions are created first
    for app_config in sender.get_app_configs():
        create_permissions(app_config, verbosity=0, interactive=False)
    
    try:
        # Create or get groups
        doctor_group, created = Group.objects.get_or_create(name='Doctors')
        staff_group, created = Group.objects.get_or_create(name='Staff')
        
        # Get UserProfile content type
        try:
            content_type = ContentType.objects.get_for_model(sender.get_model('UserProfile'))
        except:
            # Fallback if UserProfile isn't registered yet
            from .models import UserProfile
            content_type = ContentType.objects.get_for_model(UserProfile)
        
        # Doctor permissions - give them all permissions for UserProfile
        doctor_permissions = Permission.objects.filter(content_type=content_type)
        doctor_group.permissions.set(doctor_permissions)
        
        # Staff permissions - limited access
        staff_permissions = Permission.objects.filter(
            content_type=content_type,
            codename__in=[
                'view_userprofile', 
                'add_userprofile',
                'change_userprofile'  # Added change permission for staff
            ]
        )
        staff_group.permissions.set(staff_permissions)
        
        # Additional permissions you might want to add
        try:
            # Add model-specific permissions
            from django.contrib.auth.models import User
            user_content_type = ContentType.objects.get_for_model(User)
            
            # Doctors can view and change users
            doctor_group.permissions.add(
                *Permission.objects.filter(
                    content_type=user_content_type,
                    codename__in=['view_user', 'change_user']
                )
            )
            
            # Staff can only view users
            staff_group.permissions.add(
                *Permission.objects.filter(
                    content_type=user_content_type,
                    codename='view_user'
                )
            )
            
        except Exception as e:
            print(f"Could not set additional permissions: {e}")
            
    except Exception as e:
        print(f"Error creating groups: {e}")

class YourAppNameConfig(AppConfig):
    name = 'test_ckd'
    
    def ready(self):
        post_migrate.connect(create_groups, sender=self)