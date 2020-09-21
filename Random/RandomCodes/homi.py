print('Okaeri! Bem vindo ao projeto de estudos para o ENEM do ano de 2020.')
print('We shall begin. Recomendo executar o programa em janela full, caso contrário, os links serão diminuídos!')
import time
list = ['1-Sites de estudo', '2-Materiais de estudo', '3-Editoriais', '4-Sites de organização', '5-Exercícios', '6-Sair.']
for x in list:
     print (x)
     time.sleep(0.25)
What_to_do = int(input("E então, qual vai ser? "))
print ()
while What_to_do > 0:
    if What_to_do == 1:
        Lista_de_link = ['ENEM estuda: https://enem.estuda.com/usuarios_login/?box=', 'Curso ENEM gratuito: https://cursoenemgratuito.com.br/', 'Kultivi: https://www.kultivi.com/login', 'Khan Academy: https://www.khanacademy.org/', 'Percursos Educativos: http://hotsite.tvescola.org.br/percursos/percursos-introducao', 'Unacademy: unacademy.com']
        print('Esta é a lista de links disponíveis: ')
        for x in Lista_de_link:
            print (x)
            time.sleep (0.3)
        print()
        What_to_do = int(input("E então, mais? "))
        print()
    elif What_to_do == 2:
        Lista_de_materiais = ['A matriz de referência do ENEM: http://download.inep.gov.br/download/enem/matriz_referencia.pdf', 'Cartilha redação a mil: https://pt.calameo.com/read/00587698845922210845b?authid=gH2ej0uCuodB', 'Site do IBGE: https://atlasescolar.ibge.gov.br/mapas-atlas/mapas-do-brasil/diversidade-ambiental.html', 'Medmindmaps: http://medmindmaps.com.br/', 'https://www.sniperdequestoes.com.br/materiais/como-se-preparar-4-meses-antes-do-enem/treinamento-junho/?utm_source=campaign&utm_medium=email&utm_campaign=sniper_de_questoes_treinamento_junho_parte_1', 'http://snip.ly/6d7rn3?fbclid=IwAR2TEnvT4ygCDgkrCUeFCWHN5R7PzjsP5Cv7ehUBlV9HA6s-qeUSCmi6daY#https://www.educabras.com/artigos/categoria/historia', 'PDFs de livros: http://lelivros.love/', 'Playlist do Procopio: https://www.youtube.com/watch?v=I-fPlExG5y4&list=PL83s8LGM84J5TWrnuGrnmi632CfjdM93j']
        print('Esta é a lista de links disponíveis:')
        print('Vale dar uma olhada na pasta de estudos também!')
        for x in Lista_de_materiais:
            print (x)
            time.sleep (0.3)
        print()
        What_to_do = int(input("E então, algo mais? "))
        print()
    elif What_to_do == 3:
        Lista_editoriais = ['Hoje em dia: https://www.hojeemdia.com.br/opini%C3%A3o/colunas/editorial-1.334042', 'O Globo: https://oglobo.globo.com/opiniao/', 'IstoÉ: https://istoe.com.br/categoria/editorial/', 'Instituo Millenium: https://www.institutomillenium.org.br/categoria/divulgacao/editoriais/', 'Jornal NEXO: https://www.nexojornal.com.br/']
        print('Está é a lista de links disponíveis:')
        for x in Lista_editoriais:
            print (x)
            time.sleep (0.3)
        print()
        What_to_do = int(input("E então, algo mais? "))
        print()
    elif What_to_do == 4:
        Lista_sitesorg = ['Evernote: evernote.com', 'Notion: https://www.notion.so/', 'https://trello.com/']
        for x in Lista_sitesorg:
            print (x)
            time.sleep (0.3)
        print()
        What_to_do = int(input("E então, algo mais? "))
        print()
    elif What_to_do == 5:
        Lista_exercícios = ['Questões de geografia: https://drive.google.com/file/d/1ESYx3fQMWi_ZN2AEbiGYnH_Ezov8ttbT/view', 'Questões de matemática: http://professoresdematematica.com.br/lista.html', 'Matematiques: http://www.matematiques.com.br/materiais.php', 'Matemática é fácil: https://www.matematicaefacil.com.br/', 'Matemática zup: https://matematicazup.com.br/exercicios-de-matematica/', 'História geral: https://historiaonline.com.br/listas-de-exercicios-historia-geral/', 'Grupo exatas: https://www.grupoexatas.com.br/#AboutUs']
        print('Esta é a lista de links disponíveis:')
        for x in Lista_exercícios:
            print (x)
            time.sleep (0.3)
        print()
        What_to_do = int(input("E então, algo mais? "))
        print()
    elif What_to_do == 6:
        print()
        print("Ok, bons estudos!")
        break

    else:    
        What_to_do = int(input("Parece que você escolheu um número que não estava na lista. Tente novamente: "))
    
