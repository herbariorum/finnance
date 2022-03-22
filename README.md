# Exemplo programa em PySide6

### Estrutura
gerente.py chama a tela de login
requirements.txt bibliotecas necessarias
-> Controller
   -> loginController faz a validação de usuários
-> Database 
    -> BaseModel faz o acesso ao postgresql e cria a classe basemodel
    -> Dataset classe generica de acesso ao banco de dados
-> Model 
    -> User classe de modelo para usuarios
-> Seguranca
    Seguranca cria hash com senha e faz a validação de senhas 
-> Vies temos as telas de login e a tela principal
