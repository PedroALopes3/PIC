---
title: "I2c"
date: 2024-03-15T12:22:40+06:00
image: images/blog/i2c.jpg
author: Tiago Dias
bg_image: "images/feature-bg.jpg"
categories: ["Protótipo"]
tags: ["Sensores"]
description: "This is meta description"
draft: false
type: "post"
---

# I2C

### O que é?

É um protocolo de comunicação, neste caso vai ser usado entre o arduino e os diversos sensores utilizando apenas 2 cabos. Não é dos protocolos mais rápidos, mas dos mais compactos e simples implementação.

### Como funciona?

Existem 4 fios que temos de ligar VDD (alimentação), GND,  SDA (pino usado para transmitir os dados) e SCL(pino usado para sincronizar a transmissão de dados entre os dispositivos). Depois para o código é necessário dar include Wire.h e das bibliotecas especificas de cada sensor, mas no link afixado encontram se exemplos de código.
