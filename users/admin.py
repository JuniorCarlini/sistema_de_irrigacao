from .models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Classe personalizada para o admin do modelo User
class CustomUserAdmin(UserAdmin):
    # Campos que serão exibidos na listagem de usuários no admin
    list_display = ('username', 'email', 'is_staff', 'is_active')
    
    # Filtros no lado direito da tela de listagem
    list_filter = ('is_staff', 'is_active', 'date_joined')
    
    # Campos que podem ser editados diretamente na listagem
    list_editable = ('is_active',)

    # Campos que serão exibidos no formulário de edição de um usuário no admin
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informações pessoais', {'fields': ('email',)}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas importantes', {'fields': ('last_login', 'date_joined')}),
    )

    # Campos exibidos ao criar um novo usuário
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_active', 'is_staff')}
        ),
    )

    # Definir os campos de busca no admin
    search_fields = ('username', 'email')

    # Ordenação dos resultados no admin
    ordering = ('username',)

# Registrar o modelo User personalizado com o CustomUserAdmin
admin.site.register(User, CustomUserAdmin)
