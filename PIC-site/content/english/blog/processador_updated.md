---
title: "Processadores e sensores"
date: 2024-04-23T12:22:40+06:00
image: images/blog/beetleBLE.jpg
author: Bernardo Santos
editor: Miguel Pereira, Vasco Martins
bg_image: "images/feature-bg.jpg"
categories: ["Protótipo"]
tags: ["Processador", "Sensores"]
description: "This is meta description"
draft: false
type: "post"
---


# Processadores e Sensores

Nas primeiras semanas de projeto decidimos que o processador (lilypad arduino), que o grupo pretendia usar, não vai ser o utilizado uma vez que foi descontinuado, por isso para combater este impedimento, foi escolhido outro processador (beetle BLE) que consideramos ser o ideal. Nesta sequência, foi-nos atribuído um arduino nano rp2040 connect, um arduino nano 33 BLE para prototipagem e posteriormente um beetle BLE. 

Nas últimas semanas realizámos testes com estes três processadores de forma a ver qual deles é o mais adequado passando agora à explicação das suas diferenças:
## Arduino Nano 33 BLE
<img src="https://media.cablematic.com/__sized__/images_1000/ar14301-03-thumbnail-1080x1080-70.jpg" alt="image" width="400" height="auto">

No arduino nano 33 BLE **testámos o sensor de sinais vitais** e obtivemos alguns resultados, tais como, dados nominais e gráficos referentes a frequência cardíaca. No entanto, foi observado que o sensor apenas apresenta resultados relevantes e corretos caso esteja em contacto com o dedo de uma forma fixa, uma vez que se estiver em contacto com o pulso ( que é a zona que nós pretendemos medir os batimentos) não apresenta dados fiáveis.

## Arduino Nano RP2040 Connect
<img src="https://cdn-learn.adafruit.com/guides/cropped_images/000/003/342/medium640/edited_P1310607.png?1622749808" alt="image" width="400" height="auto">

No arduino nano rp2040 foram **realizados testes referentes ao sensor de giroscópio e acelerómetro**, que estão integrados no arduino. Na sequência destes testes, obtivemos informações referentes à simulação de movimentos que nos transmitem se o sensor diz se estamos a andar ou a correr, entre outras informações. Estas não são as que nós necessitamos para o projeto em questão, mas apresenta uma ajuda relevante para perceber que realmente o sensor, não só funciona corretamente, como ainda pode ser adaptado para as nossas necessidades. Existiu ainda uma tentativa de testar o sensor de sinais vitais com este arduino, no entanto, após várias tentativas, concluiu-se que o sensor não funciona com este arduino.

## Beetle BLE
<img src="https://static.rapidonline.com/catalogueimages/product/75/02/s75-0218p02wc.jpg" alt="image" width="400" height="auto">

No beetle BLE ainda **não nos foi possível iniciar o processo de testagem**, uma vez que ainda não temos as ferramentas e materiais necessários para ligar o processador aos sensores.

# Conclusões
Ao fim de algumas semanas de testes deparámo-nos com alguns problemas que precisam de solução rápida, relativamente à escolha do processador. Estes devem-se à falta de compatibilidade e mau funcionamento com o sensor de sinais vitais. O sensor de sinais vitais apenas funciona com o arduino que não possuí o sensor giroscópio e acelerómetro, e mesmo a funcionar no arduino 33 BLE não apresenta dados corretos em contacto com o pulso. **Conclui-se assim que o sensor de frequência cardíaca utilizado até ao momento, não poderá estar presente na versão final do projeto**.

A solução pensada passava por encontrar outro sensor de frequência cardíaca que funcionasse com o arduino rp2040 connect e desta forma não teríamos de arranjar nenhum sensor extra. Outra solução seria arranjar um sensor com giroscópio e acelerómetro que fosse compatível com o arduino 33 BLE e assim teríamos os 2 sensores a funcionar no arduino. Nenhuma das soluções pensadas passou pelo processador beetle BLE, uma vez que, como referido anteriormente, ainda não conseguimos experimentar os sensores neste mesmo processador.