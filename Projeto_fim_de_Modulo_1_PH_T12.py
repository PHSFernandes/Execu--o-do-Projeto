#Projeto de final de módulo
#Autor: Paulo Henrique S. Fernandes
#Grupo: Paulo Henrique, Ronaldo e Reinaldo

#TEMÁTICA: INVESTIGAÇÃO
#Meu tema: Caça ao Tesouro

print('Após a morte do seu avô Abraham, o advogado dele te entregou uma pasta lacrada que continha documentos nunca antes revelados à família. Quando criança, você sempre ouviu histórias sobre seu avô, que fazia expedições. No entanto, a vida dele era cercada de muitos mistérios. Uns diziam que ele era Arqueólogo, outros diziam que ele era garimpeiro e havia até quem dizia que ele pertencia à máfia. Talvez ele fosse tudo isso. Um desses documentos contém um mapa que mostra um ponto remoto no Oceano Índico, à aproximadamente 3000 milhas náuticas à leste do ponto mais oriental da Ilha de Madagascar. Lá se encontra uma Ilha de 300 km quadrados, conhecida como Ilha do Dragão. Pouco se sabe sobre esta ilha recoberta por densa vegetação. As únicas notícias que se ouve falar é que muitos aventureiros que para lá foram, nunca mais voltaram. Junto ao Mapa há uma carta de Abraham dando detalhes de um tesouro escondido na Ilha do Dragão, mais precisamente na Montanha Cabeça de Gigante. O seu desafio é achar o tesouro, mas não pense que será fácil... Além dos inúmeros perigos na Ilha do Dragão, outras pessoas estão de olho no tesouro.')



print('A tabela abaixo exibe as características de cada um dos personagens')

#Chama Arquivo Caracteristicas_Personagens.txt que contém a tabela com as características de Força e Inteligência de cada personagem

with open('Caracteristicas_Personagens.txt', 'r', encoding='utf-8') as file:
    text = file.read()

lines_of_text = text.splitlines()

for line in lines_of_text:
    print(line.center(60))

#Aqui a escolha dos nomes em loop até a escolha do nome correto

nome_certo = False

while nome_certo == False:
    nome = input('Escolha um dos personagens acima e digite seu nome ao lado: ')

    if (nome == 'Rick'):
        print ('Você escolheu jogar com o personagem Rick!')
        nome_certo = True
    elif (nome == 'Mell'):
        print ('Você escolheu jogar com a personagem Mell!')
        nome_certo = True
    elif (nome == 'Will'):
        print ('Você escolheu jogar com o personagem Will!')
        nome_certo = True
    
    else:
        print ('!!! ATENÇÃO!!! Digite o nome como descrito na tabela!')
        nome_certo = False

    if nome_certo == True:
        print ('Muito bem, %s ,você agora irá escolher o meio de transporte até a Ilha do Dragão.' %nome)

#Início da primeira fase com a escolha do meio de transporte

with open('Escolha_do_Transporte.txt', 'r', encoding='utf-8') as file:
    text = file.read()

lines_of_text = text.splitlines()

for line in lines_of_text:
    print(line.center(10))

#Teste de Git