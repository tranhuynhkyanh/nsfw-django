from django.apps import AppConfig
from django.db.models.signals import post_migrate


class PredictConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.predict"

    has_created_superuser = False  # Biến để theo dõi xem superuser đã được tạo chưa

    def ready(self):
        # Kết nối signal post_migrate với hàm create_superuser_on_startup
        post_migrate.connect(self.create_superuser_on_startup, sender=self)

    def create_superuser_on_startup(self, sender, **kwargs):
        # Kiểm tra xem superuser đã được tạo chưa
        if not self.__class__.has_created_superuser:
            # Tạo superuser
            from django.contrib.auth.models import User
            if not User.objects.filter(username='admin').exists():
                print('Add superuser successfully')
                User.objects.create_superuser('admin', '', '123456')
                self.__class__.has_created_superuser = True
            else:
                print('Superuser already had')
