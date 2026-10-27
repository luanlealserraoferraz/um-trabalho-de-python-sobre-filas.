
fila = []

# controles gerais e estatisticas
proxima_senha = 1
total_senhas = 0
atendidos = 0
qtd_desistencias = 0
soma_tempo = 0

while True:
    print("G - Gerar senha comum")
    print("P - Gerar senha preferencial")
    print("C - Chamar próximo cliente")
    print("A - Avançar tempo")
    print("F - Exibir fila")
    print("E - Exibir estatísticas")
    print("S - Sair")
    
    opcao = input("Escolha uma opção: ").upper().strip()
    
    if opcao == 'G':
        # cria o cliente comum e joga pro fim da lista
        novo = [proxima_senha, "C", 0]
        fila.append(novo)
        print(f"Senha {proxima_senha} criada (Comum).")
        
        proxima_senha = proxima_senha + 1
        total_senhas = total_senhas + 1
        
    elif opcao == 'P':
        # cria o cliente preferencial e joga pro fim da lista
        novo = [proxima_senha, "P", 0]
        fila.append(novo)
        print(f"Senha {proxima_senha} criada (Preferencial).")
        
        proxima_senha = proxima_senha + 1
        total_senhas = total_senhas + 1
        
    elif opcao == 'C':
        if len(fila) == 0:
            print("Não há clientes na fila.")
        else:
            # Inicializamos como None para saber se alguém já foi capturado
            chamado = None  
            
            # Regra 1: busca cliente comum com tempo de espera >= 8
            for i, cliente in enumerate(fila):
                if cliente[1] == "C" and cliente[2] >= 8:
                    chamado = fila.pop(i)
                    break # Interrompe a busca da Regra 1
            
            # Regra 2: SÓ roda se ninguém foi chamado na Regra 1
            if chamado is None:
                for i, cliente in enumerate(fila):
                    if cliente[1] == "P":
                        chamado = fila.pop(i)
                        break # Interrompe a busca da Regra 2
            
            # Regra 3: SÓ roda se ninguém foi chamado nas regras anteriores
            if chamado is None:
                for i, cliente in enumerate(fila):
                    if cliente[1] == "C":
                        chamado = fila.pop(i)
                        break # Interrompe a busca da Regra 3
            
            # Garante que processa o atendimento apenas se alguém foi encontrado
            if chamado is not None:
                print(f"Chamando cliente -> Senha: {chamado[0]} | Tipo: {chamado[1]} | Espera: {chamado[2]}")
                atendidos = atendidos + 1
                soma_tempo = soma_tempo + chamado[2]     
                
    elif opcao == 'A':
        # aumenta o tempo de todo mundo que ta na fila
        for i in range(len(fila)):
            fila[i][2] = fila[i][2] + 1
            
        # remove desistencias varrendo de tras para frente pra nao quebrar o indice
        i = len(fila) - 1
        while i >= 0:
            if fila[i][2] >= 10:
                desistiu = fila[i]
                print(f"Cliente desistiu (espera longa) -> Senha: {desistiu[0]} | Tipo: {desistiu[1]}")
                fila.pop(i)
                qtd_desistencias = qtd_desistencias + 1
            i = i - 1
            
        print("Tempo avancado em 1 unidade.")
        
    elif opcao == 'F':
        if len(fila) == 0:
            print("Nao ha ninguem na fila agora.")
        else:
            print("\n--- FILA ATUAL ---")
            print("Senha\tTipo\tTempo de Espera")
            for cliente in fila:
                print(f"{cliente[0]}\t{cliente[1]}\t{cliente[2]}")
                
    elif opcao == 'E':
        print("ESTATISTICAS DA AGENCIA")
        print(f"Senhas geradas: {total_senhas}")
        print(f"Clientes atendidos: {atendidos}")
        print(f"Desistencias: {qtd_desistencias}")
        print(f"Pessoas na fila agora: {len(fila)}")
        
        # validacao para nao dar erro de divisao por zero
        if atendidos == 0:
            print("Tempo medio de espera: Nao houve atendimentos ainda.")
        else:
            media = soma_tempo / atendidos
            print(f"Tempo medio de espera: {media:.2f} unidades de tempo")
            
    elif opcao == 'S':
        print("Saindo do sistema.")
        break
        
    else:
        print("Opcao incorreta! Digite uma letra que esteja no menu.")