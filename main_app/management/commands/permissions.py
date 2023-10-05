from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from ...models import Vehicle, Location


class Command(BaseCommand):
    help = 'Sets up permissions for Admin and Employee groups'

    def handle(self, *args, **kwargs):
        admin_group, created = Group.objects.get_or_create(name='Admin')
        employee_group, created = Group.objects.get_or_create(name='Employee')
        
        vehicle_content_type = ContentType.objects.get_for_model(Vehicle)
        vehicle_permission = Permission.objects.filter(content_type=vehicle_content_type)
        
        location_content_type = ContentType.objects.get_for_model(Location)
        location_permission = Permission.objects.filter(
            content_type=location_content_type)

        for perm in vehicle_permission:
            if perm.codename == "delete_vehicle" or perm.codename == "add_vehicle":
                admin_group.permissions.add(perm)
            else:
                admin_group.permissions.add(perm)
                employee_group.permissions.add(perm)

        for perm in location_permission:
            admin_group.permissions.add(perm)

        self.stdout.write(self.style.SUCCESS('Permissions have been set up.'))
