from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from ...models import Vehicle, Location

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
