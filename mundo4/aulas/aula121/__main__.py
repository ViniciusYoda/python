from aluno import Aluno
from Professor import Professor
from funcionario import Funcionario
        
a1 = Aluno("Maria", 22)
a1.fazer_aniversario()
a1.fazer_matricula()

p1 = Professor("Dr. Silva", 45)
p1.dar_aula()
f1 = Funcionario("Carlos", 30)
f1.bater_ponto()