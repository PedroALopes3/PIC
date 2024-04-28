---
title: "Service"
description: "this is meta description"
bg_image: "images/feature-bg.jpg"
layout: "service"
draft: false

########################### about service #############################
about:
  enable : true
  title : "Creative UX/UI Design Agency"
  content : "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptate soluta corporis odit, optio
          cum! Accusantium numquam ab, natus excepturi architecto earum ipsa aliquam, illum, omnis rerum, eveniet
          officia nihil. Eum quod iure nulla, soluta architecto distinctio. Nesciunt odio ullam expedita, neque fugit
          maiores sunt perferendis placeat autem animi, nihil quis suscipit quibusdam ut reiciendis doloribus natus nemo
          id quod illum aut culpa perspiciatis consequuntur tempore? Facilis nam vitae iure quisquam eius harum
          consequatur sapiente assumenda, officia voluptas quas numquam placeat, alias molestias nisi laudantium
          nesciunt perspiciatis suscipit hic voluptate corporis id distinctio earum. Dolor reprehenderit fuga dolore
          officia adipisci neque!"
  image : "images/company/company-group-pic.jpg"


########################## featured service ############################
featured_service:
  enable : true
  service_item:
    # featured service item loop
    - name : "Interface Design"
      icon : "fas fa-flask"
      color : "primary"
      content : "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Saepe enim impedit repudiandae omnis est temporibus."

    # featured service item loop
    - name : "Product Branding"
      icon : "fas fa-leaf"
      color : "primary-dark"
      content : "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Saepe enim impedit repudiandae omnis est temporibus."

    # featured service item loop
    - name : "Game Development"
      icon : "fas fa-lightbulb"
      color : "primary-darker"
      content : "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Saepe enim impedit repudiandae omnis est temporibus."


############################# Service ###############################
service:
  enable : false
  title : "Prototype components"
  description : "This is the list of elements that build our project, for more detailed information consult the blog."
  service_item:
    # service item loop
    - icon : fas fa-layer-group #https://fontawesome.com/v5.15/icons
      name: Server
      content: "Used to store the data and compute the algorithms - Firebase"

    # service item loop
    - icon : fas fa-wifi #https://fontawesome.com/v5.15/icons
      name: Local Router
      content: "Relay between the bracelet and the server, makes some compute - Raspberry Pie 5"

    # service item loop
    - icon : fas fa-ring #https://fontawesome.com/v5.15/icons
      name: Bracelet
      content: "Used to secure the prototype to the arm of the user."

    # service item loop
    - icon : fas fa-microchip #https://fontawesome.com/v5.15/icons
      name: Processor
      content: "Controles the sensors and sends the data via Bluetooth tho the local router - Beetle BLE"

    # service item loop
    - icon : fas fa-battery-three-quarters #https://fontawesome.com/v5.15/icons
      name: Battery
      content: "Used to power the prototype - <br> Li-Po 500mAh"

    # service item loop
    - icon : fas fa-tachometer-alt #https://fontawesome.com/v5.15/icons
      name: Gyroscope and Acelerometer
      content: "Collect data of the user moviments to identify falls"

    # service item loop
    - icon : fas fa-heartbeat #https://fontawesome.com/v5.15/icons
      name: Vitals sensor
      content: "Composed of a hearthbeat sensor and an oximeter collects the vitals of the user."

    # service item loop
    - icon : fas fa-charging-station #https://fontawesome.com/v5.15/icons
      name: Battery Charger
      content: "Alows to rechage the prototype"

############################# call to action #################################
cta:
  enable : true
  # call to action content comes from "_index.md"
---
