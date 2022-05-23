<p align="center">
<img src="https://user-images.githubusercontent.com/37037163/169902035-61e7472e-b45f-419e-a16c-728ab59e49fc.png" width="500"/><br><br><br>    
</p>

# **<p align="center">Boarding system dla portu lotniczego</p><br>**


### **<p align="right"><a href="https://github.com/verduttio">Bartłomiej Szwaja</a></p>**
### **<p align="right"><a href="https://github.com/YuriiBatkovych">Yurii  Titov</a></p>**
### **<p align="right"><a href="https://github.com/Stempnio">Jakub Stępień</a></p><br>**  


# <p align="center">Spis treści</p>  
1. [Ogólny opis projektu](#ogolny_opis)  
2. [Harmonogram realizacji](#harmonogram)
3. [Realizacja techniczna systemu](#realizacja_techniczna)
4. [API aplikacji](#api)
5. [Diagram API](#diagram_api)
6. [Diagramy sekwencji](#diagramy_sekwencji)
7. [Diagram przypadków użycia](#diagramy_uzycia)
8. [Diagram klas](#diagram_klas)

## **<p align="center">Ogólny opis projektu</p> <a name="ogolny_opis"></a>**

Celem projektu jest utworzenie oprogramowania dla portu lotniczego. W dzisiejszych czasach porty lotnicze są miejscami niezwykle ważnymi w podróżowaniu. Umożliwiają najszybsze dotarcie do wybranego celu podróży spośród dostępnych powszechnie środków transportu. Dlatego coraz więcej ludzi wyraża chęć skorzystania z takich udogodnień. Stąd efektem takiego działania jest rosnąca z roku na rok liczba wykonanych lotów na świecie. Jak przed chwilą wspomnieliśmy, zaletą podróży samolotem jest zyskany czas, jednakże z uwagi na duże zainteresowanie czas ten musi być starannie rozplanowany przez administrację portu lotniczego, by w ciągu doby lotnisko mogło obsłużyć jak najwięcej lotów.  

Dlatego stworzone przez nas oprogramowanie będzie umożliwiało optymalną i intuicyjną organizację lotów, będzie ponadto wspomagać pracowników lotniska w ich codziennej pracy. 

Nasz boarding system ułatwia przeprowadzaną przez pracowników lotniska kontrolę pasażerów przed wejściem na podkład. Mieści w sobie wszystkie niezbędne informacje dotyczące osób, które zrobiły rezerwację na konkretny lot, listę lotów oraz osób poszukiwanych przez policje i inne służby bezpieczeństwa. Interfejs systemu jest intuicyjny i wygodny.  
<br>

## **<p align="center">Harmonogram realizacji</p> <a name="harmonogram"></a>**

25.02.2022 – 13.03.2022
* Planowanie, doprecyzowanie ogólnej koncepcji systemu, stworzonej w semestrze zimowym
  
14.03.2022 – 01.04.2022 
* Analiza wykonalności projektu, wybór narzędzi informatycznych, modelowanie systemu
  
02.04.2022 – 25.04.2022 
* Implementacja funkcjonalności systemu
  
25.04.2022 – 30.04.2022 
* Praca nad widokiem interfejsu użytkownika 
  
01.05.2022 – 06.05.2022 
* Testowanie systemu i naprawa ewentualnych błędów
  
07.05.2022 – 08.05.2022 
* Stworzenie dokumentacji zrealizowanego projektu informatycznego  
  
<br> 

## **<p align="center">Realizacja techniczna systemu</p> <a name="realizacja_techniczna"></a>**

### Wykorzystane narzędzia programistyczne
**Język oprogramowania:** Python 3.10.0  
**Framework, na którym bazuje system:** Django 4.0.3  

System jest dostępny przez przeglądarkę. Jest to optymalne rozwiązanie, ze względu na przeznaczenie systemu: kontrola pasażerów przed wejściem na pokład samolotu. Zatem każdy uprawniony do tego pracownik lotniska będzie w stanie zalogować się do systemu ze swojego urządzenia.  

Aby uzyskać dostęp do systemu niezbędne jest podanie loginu i hasła użytkownika. 

Wspomniane wyżej informacje o planowanych i obsłużonych lotach, listy osób, które weszły na pokłady samolotów lub zarezerwowali miejsca w odpowiednich lotach, listy osób niebezpiecznych są przechowywane w rozbudowanym systemie plikowym, który pełni rolę swego rodzaju bazy danych.

<br>

## **<p align="center">API aplikacji</p> <a name="api"></a>**

**{host:port}/flights/login** 
* ekran logowania  
  
**{host:port}/flights/boarding/** 
* ekran główny, zawierający listę przyszłych i przeszłych lotów oraz informację o statusie boardingu na te loty   
  
**{host:port}/flights/boarding/{flight_number}** 
*  ekran zawierający informacje o boardingu na lot numer flight_number, listę pasażerów lotu z ich satusem boardingu. Umożliwia zmiane statusu boardingu konkretnego pasażera lub zakończenie całego boardingu na dany lot.  
  
**{host:port}/flights/security/fugitives** 
*  ekran zawierający zdjęcia osób niebezpiecznych   
  
<br>

## **<p align="center">Diagram API</p> <a name="diagram_api"></a>**  
<p align="center">
<img src="https://user-images.githubusercontent.com/37037163/169899885-cf9d02ca-59bf-4e74-9b34-0d82992298d6.png" width="500"/>
</p>

<br><br>

## **<p align="center">Diagramy sekwencji</p> <a name="diagramy_sekwencji"></a>**  
* ### **logowanie**
  
<p align="center">
<img src="https://user-images.githubusercontent.com/37037163/169900708-94f798fd-33be-461f-a6f8-9577acae669b.png" width="500"/>
</p>

* ### **Wybór lotu**
<p align="center">
<img src="https://user-images.githubusercontent.com/37037163/169900805-9708c8d8-25dc-47c2-b3bb-69facecfe3ab.png" width="500"/>
</p>

* ### **Proces boardingu pasażerów**
<p align="center">
<img src="https://user-images.githubusercontent.com/37037163/169900848-c3eba9dd-f62a-4ac7-b203-f79d39bb1532.png" width="500"/>
</p>

<br><br>

## **<p align="center">Diagram przypadków uzycia</p> <a name="diagramy_uzycia"></a>**  
<p align="center">
<img src="https://user-images.githubusercontent.com/37037163/169900883-b81f46cc-0764-4147-89e5-8b266ef434dc.png" width="500"/>
</p>

<br><br>

## **<p align="center">Diagram klas</p> <a name="diagram_klas"></a>**  
<p align="center">
<img src="https://user-images.githubusercontent.com/37037163/169900915-77cbb017-d3ae-4017-9385-1d7894445d14.png" width="500"/>
</p>
