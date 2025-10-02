# IoT-perusteet
Kurssin ohjelmointiin liittyvät tehtävät

# [VIIKKO 1:](https://github.com/plipsanen/IoT-perusteet-ohjelmointi/tree/main/Viikko%201)
## [Tehtävä 1: Blink the LED](https://github.com/plipsanen/IoT-perusteet-ohjelmointi/tree/main/Viikko%201/1%20Blink%20the%20led)
Tämä projekti demonstroi yksinkertaista LEDin vilkutusta Raspberry Pi Pico W:llä. 
Tehtävää on muokattu alkuperäisestä eteenpäin niin, että LED vilkkuu lyhyt–pitkä–lyhyt–pitkä-kuviolla.
### Laitteistovaatimukset
- Raspberry Pi Pico
- 1 × LED
- Vastus
- Hyppylankoja


## [Tehtävä 2: LED on with a button](https://github.com/plipsanen/IoT-perusteet-ohjelmointi/tree/main/Viikko%201/2%20Led%20on%20with%20a%20button)
Tämä projekti näyttää, miten LEDiä voidaan ohjata napilla Raspberry Pi Pico W:ssä. 
Tehtävää on kehitetty niin, että kun nappia painaa kerran, valo välähtää kerran. Kun nappi painetaan pohjassa, LED vilkkuu nopeasti.

### Laitteistovaatimukset
- Raspberry Pi Pico 
- 1 × LED
- 1 × painonappi  
- Vastus
- Hyppylankoja


## [Tehtävä 3: Traffic Lights](https://github.com/plipsanen/IoT-perusteet-ohjelmointi/tree/main/Viikko%201/3%20Traffic%20lights)
Tämä projekti simuloi liikennevaloja Raspberry Pi Pico W:llä. Projektiin on lisätty LCD-näyttö, jossa lukee englanniksi minkä värinen valo on päällä. 
### Laitteistovaatimukset
- Raspberry Pi Pico W  
- 3 × LED (punainen, keltainen, vihreä)  
- 3 × vastus
- Summeri
- Painonappi
- LCD 12x3 I2C -näyttö
- Hyppylankoja


## [Tehtävä 4: Interrup](https://github.com/plipsanen/IoT-perusteet-ohjelmointi/tree/main/Viikko%201/4%20Interrup)
Tämä projekti on yksinkertainen reaktioaikapeli Raspberry Pi Pico W:llä.  
Ohjelma mittaa käyttäjän reaktion, kun LED sammuu ja summeri piippaa. Tässä tehtävässä ekstrana on tehty summeri.

### Laitteistovaatimukset
- Raspberry Pi Pico W  
- 1 × LED
- 1 × painonappi  
- Summeri 
- Vastus
- Hyppylankoja

## [Tehtävä 5: Bulglary alarm](https://github.com/plipsanen/IoT-perusteet-ohjelmointi/tree/main/Viikko%201/5%20Burglary%20alarm)
Tässä projektissa käytetään Raspberry Pi Pico W -mikrokontrolleria ja PIR-liiketunnistinta liikkeen havaitsemiseen. Kun liikettä havaitaan, Picon sisäinen LED syttyy. Lisäyksenä on liitetty myös ulkoinen LED, joka näyttää punaista valoa liikkeen aikana.

### Laitteistovaatimukset
- Raspberry Pi Pico W  
- 1 × LED
- 1 × painonappi  
- PIR-liiketunnistin 
- Vastus
- Hyppylankoja


## [Tehtävä 6: Weather station](https://github.com/plipsanen/IoT-perusteet-ohjelmointi/tree/main/Viikko%201/6%20Weather%20station)
Tämä projekti käyttää Raspberry Pi Pico W:tä ja DHT22-anturia lämpötilan ja kosteuden mittaamiseen.
Lisäksi käytössä on kaksi LEDiä hälytyksiä varten: Punainen LED syttyy, jos lämpötila ylittää määritellyn rajan ja sininen, jos kosteus laskee alle määritellyn rajan.
## Laitteistovaatimukset
- Raspberry Pi Pico W  
- 2 × LED
- 1 × painonappi 
- 2 × vastus
- DHT22-anturi 
- Hyppylankoja


## [Tehtävä 7: Weather station with backend](https://github.com/plipsanen/IoT-perusteet-ohjelmointi/tree/main/Viikko%201/7%20Weather%20station%20with%20backend)
Tämä projekti toteuttaa IoT-sovelluksen ESP32:lla, joka lukee lämpötila- ja kosteusarvoja DHT22-sensorista ja lähettää tiedot ThingSpeak-pilvipalveluun reaaliaikaista visualisointia varten. Perustehtävää on täydennetty LCD-näytöllä, joka näyttää lukemat.
### Laitteistovaatimukset
- Raspberry Pi Pico W  
- DHT22-anturi 
- LCD 12x3 I2C -näyttö
- Hyppylankoja


# [VIIKKO 2:](https://github.com/plipsanen/IoT-perusteet-ohjelmointi/tree/main/Viikko%202)
Tämä on yksinkertainen express.js-palvelin, joka simuloi IoT-anturidataa.
Palvelin tarjoaa yhden REST-rajapinnan, josta voidaan hakea sensorin mittaustiedot JSON-muodossa.


# [VIIKKO 3:](https://github.com/plipsanen/IoT-perusteet-ohjelmointi/tree/main/Viikko%203)
Tämä projekti on express.js-pohjainen palvelin, joka käynnistyy portissa 3000 ja käyttää SQLite-tietokantaa. Käynnistyessä se luo automaattisesti tiedoston PaulanDatabase.db ja sinne taulun users, jos sitä ei vielä ole. Palvelimessa on rajapinta, joka palauttaa simuloidun sensoridatan lämpötilasta ja kosteudesta, sekä rajapinnat käyttäjien hakemiseen ja lisäämiseen.


# [VIIKKO 4:](https://github.com/plipsanen/IoT-perusteet-ohjelmointi/tree/main/Viikko%204)

## [Websocket](https://github.com/plipsanen/IoT-perusteet-ohjelmointi/tree/main/Viikko%204/Websocket)
Tämä projekti demonstroi WebSocket-yhteyttä node.js-palvelimen ja selaimen välillä. Palvelin vastaanottaa viestejä asiakkailta ja lähettää ne takaisin ("echo").

## [Webhook](https://github.com/plipsanen/IoT-perusteet-ohjelmointi/tree/main/Viikko%204/Webhook)
Tämä projekti on node.js/express-sovellus, joka välittää HTTP POST -pyynnön kautta saapuvat viestit Discord-kanavalle Webhookin avulla.

## [Fetch](https://github.com/plipsanen/IoT-perusteet-ohjelmointi/tree/main/Viikko%204/Fetch)
Tämä projekti hakee lämpötiladataa ThingSpeak API:sta ja näyttää sen selaimessa JSON-muodossa. Sovellus käyttää JavaScriptin fetch-funktiota hakeakseen mittaustiedot määritetystä ThingSpeak-kanavasta. Jokaisesta mittauksesta otetaan aikaleima (created_at) ja lämpötila (field1). Tulokset muunnetaan taulukoksi ja näytetään selaimessa JSON-muodossa.

## [GoogleChart](https://github.com/plipsanen/IoT-perusteet-ohjelmointi/tree/main/Viikko%204/GoogleChart)
Tässä haetaan mittaustietoja ThingSpeak API:sta ja visualisoidaan ne selaimessa Google Charts -kirjaston avulla. Käytössä Curving the Lines -taulukko.
