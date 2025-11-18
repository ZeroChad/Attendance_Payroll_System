from config.settings import get_secret
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.utils.timezone import localdate

from .models import CustomUser

@receiver(post_migrate)
def create_admin_user(sender, **kwargs):
    if sender.name == "accounts":
        users = [{
            "email": get_secret("ADMIN_EMAIL"),
            "role": "admin",
            "admin": True,
        },{
            "email": "employee@test.com",
            "role": "employee",
            "admin": False,
        }, {
            "email": "manager@test.com",
            "role": "manager",
            "admin": False,
        }]

        for user in users:
            USER = CustomUser.objects.filter(email=user["email"]).first()
            if not USER:
                if user["admin"]:
                    USER = CustomUser.objects.create_superuser(
                        email=user["email"],
                        username=user["email"],
                        password=get_secret("ADMIN_PASSWORD"),
                        sex="Male",
                        birthday=localdate(),
                        role=user["role"],
                    )
                else:
                    USER = CustomUser.objects.create_user(
                        email=user["email"],
                        username=user["email"],
                        password=get_secret("ADMIN_PASSWORD"),
                        sex="Male",
                        birthday=localdate(),
                        role=user["role"]
                    )
                print(f"Created {user['role']} account: {USER.email}")

                USER.first_name = f"DEBUG_USER:{USER.email}"
                USER.is_active = True
                USER.save()

        