from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da cidade")
    uf = models.CharField(max_length=2, verbose_name="UF")

    def __str__(self):
        return f"{self.nome}, {self.uf}"

class Ocupacao(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    nome_do_pai = models.CharField(max_length=100)
    nome_da_mae = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True, verbose_name="CPF da pessoa")
    data_nasc = models.DateField(verbose_name="Data de nascimento")
    email = models.EmailField()
    cidade = models.ForeignKey(Cidade, on_delete=models.SET_NULL, null=True)
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome

class Instituicao(models.Model):
    nome = models.CharField(max_length=100)
    site = models.URLField()
    telefone = models.CharField(max_length=20)
    cidade = models.ForeignKey(Cidade, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome

class AreaSaber(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    carga_horaria_total = models.PositiveIntegerField()
    duracao_meses = models.PositiveIntegerField()
    area_saber = models.ForeignKey(AreaSaber, on_delete=models.SET_NULL, null=True)
    instituicao = models.ForeignKey(Instituicao, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome

class Turno(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    area_saber = models.ForeignKey(AreaSaber, on_delete=models.SET_NULL, null=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome


class TipoAvaliacao(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
class Avaliacao(models.Model):
    descricao = models.TextField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=5, decimal_places=2)
    tipo_avaliacao = models.ForeignKey(TipoAvaliacao, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.descricao

class Frequencia(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    numero_faltas = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.pessoa} - {self.disciplina}"

class Turma(models.Model):
    nome = models.CharField(max_length=100)
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Matricula(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_previsao_termino = models.DateField()
    turma = models.ForeignKey("Turma", on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.pessoa} - {self.curso}"
    
class Ocorrencia(models.Model):
    descricao = models.TextField()
    data = models.DateField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao

class CursoDisciplina(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    turno = models.ForeignKey(Turno, on_delete=models.SET_NULL, null=True)
    carga_horaria = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.curso} - {self.disciplina}"
