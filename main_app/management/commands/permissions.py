from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from ...models import Vehicle

admin_group, created = Group.objects.get_or_create(name='Admin')
employee_group, created = Group.objects.get_or_create(name='Employee')
content_type = ContentType.objects.get_for_model(Vehicle)
vehicle_permission = Permission.objects.filter(content_type=content_type)

for perm in vehicle_permission:
    if perm.codename == "delete_vehicle" or perm.codename == "add_vehicle":
        admin_group.permissions.add(perm)
    else:
        admin_group.permissions.add(perm)
        employee_group.permissions.add(perm)