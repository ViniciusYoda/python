import serial
conexao=""
for porta in range(10):
    try:
        conexao = serial.Serial("COM3"+str(porta), 115200, timeout=0.5)
        print("Conectado na porta: ", conexao.portstr)
        break
    except serial.SerialException:
        pass
if conexao!="":
    acao=input("Digite: <L> para Ligar <D> para Desligar: ").upper()
    while acao=="L" or acao=="D":
        if acao=="L":
            conexao.write(b'1')
        else: 
            conexao.write(b'0')
        acao=input("Digite: <L> para Ligar <D> para Desligar: ").upper()
    conexao.close()
    print("Conexão encerrada")
else:
    print("Sem portas disponíveis")