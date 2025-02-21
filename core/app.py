from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group

class CoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core"

    def ready(self):
        # Conectar o sinal post_migrate para criar os grupos após a migração
        post_migrate.connect(create_groups, sender=self)

def create_groups(sender, **kwargs):
    """Função que cria os grupos após a migração"""
    # Criação dos grupos se não existirem
    Group.objects.get_or_create(name="SUPERVISORS")
    Group.objects.get_or_create(name="ANALYSTS")
    Group.objects.get_or_create(name="CLIENTS")
    print("Grupos criados com sucesso!")
