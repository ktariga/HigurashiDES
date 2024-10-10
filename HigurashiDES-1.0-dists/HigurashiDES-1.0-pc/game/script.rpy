# Definição da transformação para reduzir o tamanho das personagens
transform small_character:
    xalign 0.5  # Alinhamento horizontal
    yalign 1.0  # Alinhamento vertical
    zoom 0.5    # Reduz a imagem para 50% do tamanho original

# Definições dos personagens
define k = Character("Keiichi")
define rena = Character("Rena")
define mion = Character("Mion")
define satoko = Character("Satoko")
define rika = Character("Rika")

label start:
    # Música de fundo
    play music "paris.mp3" fadein 1.0

    # Background inicial
    scene gk1

    # Apresentação de Keiichi
    k "Bom dia, pessoal! O que estamos planejando para hoje?"

    # Apresentação da Rena
    show rena1 at small_character
    with dissolve

    rena "Keiichi-kun! Hoje nós temos um desafio para você. E eu já preparei lanches para a ocasião!"

    # Esconde Rena e apresenta Mion
    hide rena1
    show mion1 at small_character
    with dissolve

    mion "Espero que você esteja preparado! E não se preocupe, a Mion não vai te dar um desafio tão difícil quanto um de verdade!"

    # Esconde Mion e apresenta Satoko
    hide mion1
    show satoko1 at small_character
    with dissolve

    satoko "E se você errar, eu vou... bem, vou tentar não te assustar demais com a minha surpresa!"

    # Esconde Satoko e apresenta Rika
    hide satoko1
    show rika1 at small_character
    with dissolve

    rika "E não se esqueça, Keiichi! Se você se sair bem, eu posso até te dar um presente especial."

    # Preparação para as perguntas
    k "Tudo bem, eu aceito o desafio. Vamos começar!"
    
    # Esconde todos os personagens para iniciar as perguntas
    hide rika1
    
    jump question_1

label question_1:
    # Primeira pergunta
    scene gk1
    show mion1 at small_character
    with dissolve
    
    mion "Primeira pergunta: Qual dos seguintes é um dispositivo de entrada? E não se preocupe, não é um truque!"

    menu:
        "Teclado":
            $ score = 1
            k "Certo! Próxima pergunta."
            jump question_2
        "Impressora":
            $ score = 0
            k "Errado! Acho que você precisa de um pouco mais de treinamento para isso."
            jump bad_route

label question_2:
    # Segunda pergunta
    scene gk1
    show mion1 at small_character
    with dissolve
    
    mion "Segunda pergunta: Qual dos seguintes é um dispositivo de saída? Não vale usar sua inteligência do café!"

    menu:
        "Monitor":
            $ score += 1
            k "Isso mesmo! Próxima pergunta."
            jump question_3
        "Mouse":
            $ score = 0
            k "Não, não é esse. Acho que o café está afetando sua mente!"
            jump bad_route

label question_3:
    # Terceira pergunta
    scene gk1
    show mion1 at small_character
    with dissolve
    
    mion "Terceira pergunta: Qual dispositivo pode ser tanto de entrada quanto de saída? E não é uma máquina de café!"

    menu:
        "Touchscreen":
            $ score += 1
            k "Exatamente! Você realmente sabe suas coisas."
            jump good_route
        "Scanner":
            $ score = 0
            k "Isso está errado! Parece que você deve estudar mais sobre tecnologia!"
            jump bad_route

label good_route:
    # Final Bom
    scene gk1

    # Apresenta a Rena
    show rena1 at small_character
    with dissolve
    rena "Você acertou todas as perguntas, Keiichi-kun! E eu trouxe o lanche especial como recompensa!"
    pause 1.0

    # Esconde Rena e apresenta a Mion
    hide rena1
    show mion2 at small_character
    with dissolve
    mion "Parece que você estudou bem! Talvez eu tenha subestimado sua habilidade!"
    pause 1.0

    # Esconde Mion e apresenta a Satoko
    hide mion2
    show satoko1 at small_character
    with dissolve
    satoko "Dessa vez você escapou, Keiichi! Mas não se acostume muito com isso!"
    pause 1.0

    # Esconde Satoko e apresenta a Rika
    hide satoko1
    show rika1 at small_character
    with dissolve
    rika "Parabéns, Keiichi. Parece que você é o mestre dos dispositivos agora!"

    k "Obrigado, pessoal! Foi divertido! E eu estou pronto para o próximo desafio, se houver!"

    return

label bad_route:
    # Final Ruim
    scene gk1

    # Apresenta a Rena
    show rena2 at small_character
    with dissolve
    rena "Oh não, Keiichi-kun... Você errou uma das perguntas. Acho que você precisa de mais treino."
    pause 1.0

    # Esconde Rena e apresenta a Mion
    hide rena2
    show mion2 at small_character
    with dissolve
    mion "Parece que você não se preparou o suficiente. Talvez na próxima vez, você se saia melhor!"
    pause 1.0

    # Esconde Mion e apresenta a Satoko
    hide mion2
    show satoko2 at small_character
    with dissolve
    satoko "Agora você terá que enfrentar as consequências! Mas não se preocupe, eu trouxe um 'prêmio de consolação'."
    pause 1.0

    # Esconde Satoko e apresenta a Rika
    hide satoko2
    show rika2 at small_character
    with dissolve
    rika "Melhor sorte na próxima vez, Keiichi. E lembre-se, sempre há uma próxima vez!"

    k "Isso foi mais difícil do que eu pensei... Mas com certeza vou tentar de novo!"

    return
