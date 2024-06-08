---
title: "Produto Ideal"
date: 2024-06-07T12:00:40+06:00
image: images/blog/beetleBLE.jpg
author: Vasco Marins
editor: Miguel Pereira
bg_image: "images/feature-bg.jpg"
categories: ["Protótipo"]
tags: []
description: "This is meta description"
draft: false
type: "post"
---
# Produto Ideal

No âmbito do Projeto Integrador de 1º Ciclo, do curso de Engenharia Eletrotécnica e de Computadores do Instituto Superior Técnico, seria suposto desenvolver um produto para a resolução de um problema à escolha de cada grupo. Idealmente
esta solução seria um produto que pudesse ser comercializado, tendo este projeto uma componente bastante significativa de empreendedorismo. 

Através de vários seminários complementares ao projeto, foram expostos diversos temas relacionados ao mundo empresarial. No decorrer do semestre, foi desenvolvido um protótipo da solução final, que era o principal do objetivo deste trabalho. No entanto, ir-se-á de seguida idealizar como seria a versão comercial da solução.

## Contexto

O projeto *visa resolver o problema de idosos que vivem sozinhos e estão expostos a incidentes*, como quedas ou ataques cardíacos, sem qualquer apoio nem ajuda.

A *solução apresentada é uma pulseira que deteta quedas e alterações no batimento cardíaca e comunica remotamente para uma aplicação num telefone de um familiar. 

O projeto consiste em três componentes, a pulseira, a aplicação e um router local para envio de dados para o servidor. 

A pulseira foi dimensionada desde o zero e consiste num processador Arduino RP2040, que contém acelerómetro e giroscópio, um sensor de batimento cardíaco MAX30102, uma bateria de 500 mAh e um módulo de carregamento. A junção destes elementos resulta numa pulseira com 36 mm de altura, 42 mm de largura e 52 mm de comprimento, que é demasiado volumosa para uma pulseira comercial. Levanta-se, portanto, a questão de onde é que é possível cortar dimensões. Inicialmente é facilmente observável que as dimensões do arduino RP2040 (18 mm x 45 mm) não colaboram, tendo de se pensar numa solução mais reduzida e que a única aplicação seja este problema. Uma solução passaria por desenhar uma placa de origem e em massa, que teria um custo mais reduzido na ordem dos 5-10€. No entanto, aparece um problema relativamente ao acelerómetro e giroscópio que teria de se adquirir de outra forma. Uma opção seria o modelo Triple Axis Accelerometer & Gyro - MPU-6050 que desempenha todas as funções desejadas, tem um tamanho reduzido (20 mm x 15 mm) e um preço de aproximadamente 6€. Uma componente facilmente otimizada seria a bateria que apresenta uma capacidade muito acima do necessário. Seria facilmente substituída por uma bateria de lítio de 200 mAh com dimensões reduzidas (30 mm x 20 mm). Quanto ao módulo de carregamento e ao sensor de batimentos cardíacos não seria necessário otimizar.

O router local escolhido foi um Raspberry Pi 5 que tem funcionalidades muito mais avançadas do que as necessárias para este projeto. Idealmente apenas seria necessário um router com o mínimo de poder de processamento, uma vez que os dados com que lidamos são residuais a nível de armazenamento (por volta de kB). Uma alternativa válida seria desenhar uma PCB de origem, para efetuar este processamento de dados, comunicar por Bluetooth com a pulseira e por Wi-Fi com a base de dados do servidor. Não é fácil prever o custo desta solução, no entanto andará por volta de 10-30€.

A aplicação apresentada com o protótipo é uma versão bastante próxima daquela que seria a versão comercializada. Sendo assim seria apenas necessário desenvolver a parte estética da aplicação de forma a ser atrativo para o público, bem como adicionar informação adicional para ser mais completa.

## Resumo

*Custos Protótipo:*
- Arduino RP2040: 27€
- Sensor MAX30102: 8€
- Bateria de Lítio 500 mAh: 8€
- Módulo de Carregamento: 8€
- Raspberry Pi 5: 90€

<br>
<br>

*Custos Ideais:*
- Processador personalizado: ~10€
- Sensor MAX30102: 8€
- Bateria de Litio 200 mAh: 3€
- Módulo de carregamento: 8€
- Router local (PCB): ~20€

Esta estimativa é realizada de uma forma superficial e pouco estudada, não tem em conta possíveis parcerias com empresas, nem componentes feitos com este propósito, nem preços adaptados a compras em massa. No entanto, seria esta uma versão ideal da solução apresentada.