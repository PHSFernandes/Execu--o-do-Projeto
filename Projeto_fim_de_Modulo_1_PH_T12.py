#Projeto de final de módulo
#Autor: Paulo Henrique S. Fernandes
#Grupo: Paulo Henrique, Ronaldo von Parask e Reinaldo Sousa

#TEMÁTICA: INVESTIGAÇÃO
#Meu tema: Caça ao Tesouro

print("""Após a morte do seu avô Abraham, o advogado dele te entregou uma pasta lacrada que 
continha documentos nunca antes revelados à família. Um desses documentos 
contém um mapa que mostra um ponto remoto no Oceano Índico, à aproximadamente 3000 milhas 
náuticas à leste do ponto mais oriental da Ilha de Madagascar. Lá se encontra uma Ilha de 
300 km quadrados, conhecida como Ilha do Dragão. Pouco se sabe sobre esta ilha recoberta 
por densa vegetação. As únicas notícias que se ouve falar é que muitos aventureiros que 
para lá foram, nunca mais voltaram. Junto ao Mapa há uma carta de Abraham dando detalhes de 
um tesouro escondido na Ilha do Dragão, mais precisamente na Montanha Cabeça de Gigante. 
O seu desafio é achar o tesouro, mas não pense que será fácil... Além dos inúmeros perigos 
na Ilha do Dragão, outras pessoas estão de olho no tesouro.\n""")



print('A tabela abaixo exibe as características de cada um dos personagens \n')

#Chama Arquivo Caracteristicas_Personagens.txt que contém a tabela com as características de Força e Inteligência de cada personagem.

with open('Caracteristicas_Personagens.txt', 'r', encoding='utf-8') as file:
    text = file.read()

lines_of_text = text.splitlines()

for line in lines_of_text:
    print(line.center(60))

#Aqui a escolha dos nomes em loop até a escolha do nome correto
print("")

nome_certo = False
forca = 0
inteligencia = 0

while nome_certo == False:
    nome = input('Escolha um dos personagens acima e digite seu nome ao lado: ').title()

    
    if (nome == 'Rick'):
        print ('Você escolheu jogar com o personagem Rick!')
        forca = 7
        inteligencia = 8
        nome_certo = True
    elif (nome == 'Mell'):
        print ('Você escolheu jogar com a personagem Mell!')
        forca = 9 
        inteligencia = 6
        nome_certo = True
    elif (nome == 'Will'):
        print ('Você escolheu jogar com o personagem Will!')
        forca = 6
        inteligencia = 9
        nome_certo = True
    
    else:
        print ('!!! ATENÇÃO!!! Digite o nome como descrito na tabela!')
        nome_certo = False

    if nome_certo == True:
        print ('Muito bem, %s ,você agora irá escolher o meio de transporte até a Ilha do Dragão.' %nome)

#Início da primeira fase com a escolha do meio de transporte
print("")

nome_certo = False
transporte_personagem = 0
with open('Escolha_do_Transporte.txt', 'r', encoding='utf-8') as file:
    text = file.read()

lines_of_text = text.splitlines()

for line in lines_of_text:
    print(line.center(10))


def escolhaTransporte():
    global inteligencia    
    transporte = input("Digite o meio de transporte desejado [Veleiro/Hidroaviao/Barco] : ")

    if transporte.upper() == "VELEIRO":
        print("")
        
        if inteligencia >= 7:
            print("\033[32m\033[32mVOCÊ PASSOU DE FASE\033[0m\033[0m")
            escolhaDocaminho()    
        else:
            print("""\033[31m!!!GAME OVER!!!\033[0m Os ventos inconstantes nessa época do ano requerem 
conhecimento e habilidades, você ficou mais tempo no mar que o programado 
e seus suprimentos acabaram! """)
        
    elif transporte.upper() == "HIDROAVIAO":
        print("")
        
        if inteligencia >=8:
            print("\033[32mVOCÊ PASSOU DE FASE\033[0m")
            escolhaDocaminho()
        else:
            print("""\033[31m!!!GAME OVER!!!\033[0m Uma pane no sistema de navegação exigiu conhecimentos 
            técnicos que você não tinha. Infelizmente seu avião caiu no mar.""")

    elif transporte.upper() == "BARCO":
        print("")
        
        if forca >= 7:
            print("\033[32mVOCÊ PASSOU DE FASE\033[0m")
            escolhaDocaminho()
        else:
            print("""\033[31m!!!GAME OVER!!!\033[0m O mar agitado exigia muita força no leme. Infelizmente sua 
        força era pequena.""")

    else:
        print ('!!! ATENÇÃO!!! Digite o nome como descrito!')
        escolhaTransporte()   

def escolhaDocaminho():
    global inteligencia
    global forca
#Para escolher o Caminho:
    with open('Escolha_do_Caminho.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    lines_of_text = text.splitlines()

    for line in lines_of_text:
        print(line.center(60))

    caminho = input('Escolha o caminho que você vai percorrer até o tesouro [Floresta / Pantano / Costa]: ') 

    if caminho.upper() == "FLORESTA":
        print("")
        print("\033[32mVOCÊ PASSOU DE FASE\033[0m")
        escolhaFerramenta()

    elif caminho.upper() == "PANTANO":
        print("")
        if inteligencia >= 8:
            print("\033[32mVOCÊ PASSOU DE FASE\033[0m")
            escolhaFerramenta()
        else:
            print("""\033[31m!!!GAME OVER!!!\033[0m Sobreviver no pântano exige muitas habilidades e 
            menos força! """)

    elif caminho.upper() == "COSTA":
        print("")
        if forca >= 8:
            print ("\033[32mVOCÊ PASSOU DE FASE\033[0m")
            escolhaFerramenta()
        else:
            print("""\033[31m!!!GAME OVER!!!\033[0m A costa é pedregosa e requer muita força muscular 
            para transpor os obstáculos. Você precisava ser mais forte!""")
    else:
        print ('!!! ATENÇÃO!!! Digite o nome como descrito!')
        escolhaDocaminho()   


def escolhaFerramenta():
    global inteligencia
    global forca

#Para escolher da Ferramenta:
    with open('Escolha_da_Ferramenta.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    lines_of_text = text.splitlines()

    for line in lines_of_text:
        print(line.center(60))

    ferramenta = input("""Escolha a ferramenta que você pretende utilizar 
para acessar o tesouro [Dinamite / Alavanca de Ferro / Corda]: """) 

    if ferramenta.upper() == "DINAMITE":
        print("")
        if inteligencia >= 8:
            print("\033[32m!!!VOCÊ GANHOU O JOGO!!!\033[0m")
        else:
            print("""\033[31m!!!GAME OVER!!!\033[0m O uso de dinamite exige 
            conhecimentos que você não tinha. Infelizmente você morreu na explosão!""")
    elif ferramenta.upper() == "ALAVANCA DE FERRO":
        print("")
        if forca >= 9:
            print("\033[32m!!!VOCÊ GANHOU O JOGO!!!\033[0m")
        else:
            print("""\033[31m!!!GAME OVER!!!\033[0m O uso da alavanca exige uma força que você não tinha. 
            Você não conseguiu entrar na caverna! """)

    elif ferramenta.upper() == "CORDA":
        print("")
        if forca >= 7:
            print ("\033[32m!!!VOCÊ GANHOU O JOGO!!!\033[0m")
        else:
            print("""\033[31m!!!GAME OVER!!!\033[0m O uso da Corda iria te ajudar a entrar pelas frestas, 
            mas a força necessária era maior do que a que você tinha.""")

    else: 
        print ('!!! ATENÇÃO!!! Digite o nome como descrito!')
        escolhaFerramenta()   

escolhaTransporte()