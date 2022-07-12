from django.contrib import admin
from rh.models import Departamento, Funcionario

class FuncionarioAdmin(Admin.ModelAdmin):
    list_display = ['nome', 'departamento', 'cargo']
    list_filter = ['departamento', 'cargo']

# Register your models here.
admin.site.register (Funcionario, FuncionarioAdmin)
admin.site.register (Departamento)