#Definicao da classe, alunos
class Alunos:
    
    #Definicao dos atributos da classe
    aluno_nome = ""
    aluno_tel = ""
    aluno_dt_nasc = ""
    aluno_raca = ""
    aluno_sexo = ""
    
    #Definicao do construtor da classe,
    def __init__(self, nome, raca, sexo):
        self.aluno_nome = nome
        self.aluno_raca = raca
        self.aluno_sexo = sexo

    #Definicao dos metodos setters da classe
    def set_aluno_nome(self, nome):
        self.aluno_nome = nome
    
    def set_aluno_tel(self, tel):
        self.aluno_tel = tel
        
    def set_aluno_dt_nasc(self, dt_nasc):
        self.aluno_dt_nasc = dt_nasc

    def set_aluno_raca(self,raca):
        self.aluno_etinia = raca

    def set_aluno_sexo(self, sexo):
        self.aluno_sexo = sexo

    #Definicao dos metodos getters da classe
    def get_aluno_nome(self):
        return self.aluno_nome

    def get_aluno_tel(self):
        return self.aluno_tel 

    def get_aluno_dt_nasc(self):
        return self.aluno_dt_nasc

    def get_aluno_dt_raca(self):
        return self.aluno_raca

    def get_aluno_sexo(self):
        return self.aluno_sexo
        
#Inicio do codigo, inicio do bloco principal        
if __name__ == "__main__":
    #Instanciando a classe Alunos, criando o objeto aluno_diana
    aluno_diana = Alunos('Diana', 'branca', 'feminino')

    #Chamando um metodo da classe Alunos, definindo o nome do aluno
    aluno_diana.set_aluno_nome('Diana Lima')
    #Chamando um metodo da classe que retorna o nome do aluno e apresenta na saida padrao
    print(aluno_diana.get_aluno_nome())

    #Chamando um metodo da classe Alunos, definindo o telefone do aluno
    aluno_diana.set_aluno_tel('tel: 9999-9999')
    #Chamando um metodo da classe que retorna o tel do aluno e apresenta na saida padrao
    print(aluno_diana.get_aluno_tel())
    
    #Chamando um metodo da classe Alunos, definindo o data de nascimento do aluno
    aluno_diana.set_aluno_dt_nasc('12/12/1986')
    #Chamando um metodo da classe que retorna data de nascimento do aluno e apresenta na saida padrao
    print(aluno_diana.get_aluno_dt_nasc())

     #Chamando um metodo da classe Alunos, definindo raça
    aluno_diana.set_aluno_raca('branca')
    #Chamando um metodo da classe que retorna data de nascimento do aluno e apresenta na saida padrao
    print(aluno_diana.get_aluno_dt_raca())

     #Chamando um metodo da classe Alunos, definindo raça
    aluno_diana.set_aluno_sexo('Feminino')
    #Chamando um metodo da classe que retorna data de nascimento do aluno e apresenta na saida padrao
    print(aluno_diana.get_aluno_sexo())
