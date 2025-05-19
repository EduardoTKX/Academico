from django.contrib import admin
from .models import *
from django.contrib import admin

class PessoaInline(admin.TabularInline):
    model = Pessoa
    extra = 1

class OcupacaoAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)
    inlines = [PessoaInline]

class CursoInline(admin.TabularInline):
    model = Curso
    extra = 1

class InstituicaoAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)
    inlines = [CursoInline]

class CursoInline(admin.TabularInline):
    model = Curso
    extra = 1

class AreaSaberAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)
    inlines = [CursoInline]

class DisciplinasInline(admin.TabularInline):
    model = Disciplina
    extra = 1

class CursoAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)
    inlines = [DisciplinasInline]

class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao
    extra = 1

class DisciplinasAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)
    inlines = [AvaliacaoInline]

class AlunosInline(admin.TabularInline):
    model = Matricula
    extra = 1

class TurmasAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)
    inlines = [AlunosInline]



admin.site.register(Cidade)
admin.site.register(Pessoa)
admin.site.register(Instituicao, InstituicaoAdmin)
admin.site.register(AreaSaber, AreaSaberAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Turno)
admin.site.register(Disciplina, DisciplinasAdmin)
admin.site.register(Matricula)
admin.site.register(TipoAvaliacao)
admin.site.register(Avaliacao)
admin.site.register(Frequencia)
admin.site.register(Turma, TurmasAdmin)
admin.site.register(Ocorrencia)
admin.site.register(CursoDisciplina)
admin.site.register(Ocupacao, OcupacaoAdmin)

