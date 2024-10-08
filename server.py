//Iniciar o intrepretador do python
#!/usr/bin/env/ phyton3 
import socket //importar a biblioteca socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) //Instanciando objeto socket
socket.bind(("localhost", 9473)) //Chamando o objeto com o metodo Bind, passando parametro TUPLA do endereço local (como é lab sera local host caso fosse real tera que colocar o
endereço da inferface de rede a ser utilizada) seguido de uma porta alta para não haver problemas de permissão, portas abaixo de 1024 sao reservadas para serviços

socket.listen() //aguardando conexão na porta

con, addr = socket.accept() //criando duas variaveis para mostrar a conexão e o endereço de onde esta vindo a conexao

print(addr) //mostrando endereço que está Conectando
/

//ver se a conexao funcionou - ss -ln | grep 9473
//testar conexao com o nc -v localhost 9473

while True:
    data = conn.recv(1024) 
    if not data: //se nao estiver recebendo nada vai parar
        break;
    print("Nova mensagem do host %s: %s" % (addr,data.decode())) //exibir a mensagem do host, formatada com os valores de addr (ip e porta que estao falando) e a mensagem data.decode em string

//rodar o codigo, no terminal dar um nc -v localhost 9473 para conectar no socket e fornecer a mensagem

conn.close() //boa pratica de fechar conexao ao fim do codigo