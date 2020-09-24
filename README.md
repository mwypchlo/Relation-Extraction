# Relation-Extraction
Projekt jest jednym z wyzwań OKE2018 CHALLENGE – ESWC 2018, który zakłada, aby
na podstawie danych zawartych w plikach tekstowych zapisanych w formacie RDF takich jak zdanie, encje i linki do bazy dbpedii wykryć zależności jakie łączy obiekty podane w zdanie. Wszystkie zależności jakie mogą łączyć dane jednostki są z góry sprecyzowane, tak jak i cechy składające się na nie.


## Cel Projektu
Głównym celem zadania było znalezienie relacji binarnych pomiędzy bytami(encjami) znalezionymi w plikach tekstowych(*.ttl).


## Podział zadań
Rafał Adamski:
- Budowa bazy łączących zależności między poszczególnymi jednostkami
- Opracowanie parsera który czytał dane z przykładowych plików tekstowych
- Napisanie w języku SPARQL zapytania mającego za zadanie pobranie informacji z DBPedii

Michał Wypchło:
- Praca nad parserem odczytującym sentencje(wersja 1 z biblioteką nltk)
- Prace nad narzędziem określającym typ bytu S/V/O
- Menu aplikacji i praca nad skryptem głównym


## Omówienie modułów aplikacji
`GetDBPediaInfo.py` - klasa zawierająca zapytanie SPARQL, które pobiera dodatkowe informacje z DBPedii, gdy URI jest podane w pliku .ttl,

`parse.py` - skrypt odczytujący dane z pików z przykładami. Jego działanie opiera się na wyszukaniu odpowiednich wyrażeń naturalnych,

`knowledgeBase.py` - baza z zapisanymi relacjami jakie mogą łączyć poszczególne byty, w zależności od ich predykatów,

`NLpreprocessing.py` - klasa zajmująca się przetwarzaniem języka naturalnego,

`main.py` - główny plik programu łączący wszystkie moduły. Odpowiada za znalezienie relacji między poszczególnymi obiektami.

`#NOTUSED_svo_extractor.py` - plik, który docelowo nie znalazł zastosowania w projekcie, ponieważ nie udało się doprowadzić go do poprawnego działania, miał na celu określenie typu bytu pomiędzy obiektem,subiektem, a predykatem(działa tylko na krótkich zdaniach).


## Omówienie działania aplikacji
Uruchomienie aplikacji wyświetla proste menu, obsługiwane z linii poleceń.
Aplikacja umożliwia odczytanie danych bezpośrednio z pliku *.ttl(opcja 1) lub wprowadzenia własnego zdania(opcja 2).
Wybór pierwszej opcji wymusza na użytkowniku wskazanie ścieżki do pliku, z którego dane mają zostać odczytane.
Wybór drugiej opcji umożliwi wprowadzenie własnej sentencji. 

W pierwszym wariancie, po wprowadzeniu nazwy/ścieżki odpowiedniego pliku aplikacja rozpoczyna pracę udostępniając kolejne 4 możliwości.  
Opcja ‘1’ wyświetla oczekiwane trójki, odczytywane bezpośrednio z pliku *.ttl(plik jest rozkładany na części pierwsze za pomocą funkcji parse_answer w pliku parse.py).  
Opcja ‘2’ umożliwia wyświetlenie odnalezionych w pliku *.ttl bytów(za pomocą funkcji getObjectsFromSentence z pliku main.py)  
Opcja ‘3’ umożliwia wyświetlenie relacji między bytami, a cały proces skłąda się z następujących operacji.


Najpierw informacje z pliku są sczytywane przez parser. Jego funkcją jest odnalezienie zdefiniowanych w programie wyrażeń naturalnych występujących w podanym pliku. Poszukiwane są:
- zdanie na podstawie którego powinny być przypasowywane odpowiednie relacje do obiektów,
- encje,
- własności encji,
- URI DBPedii, gdzie może znajdować się więcej informacji o encjach (o ile występuje).

W momencie parsowania odbywa się również ściągniecie dodatkowych informacji o obiekcie z DBPedii, a odpowiada za to klasa GetDBPediaInfo.py. Moduł ten za pomocą biblioteki SPARQLWrapper wysyła zapytanie RDF mające znaleźć własność rdf:type i z niej pobrać wszystkie ontologie.

Sam parser zwraca takie informacje jak:
- zdanie podane w pliku,
- słownik wykrytych encji wraz z ich predykatami.

Ostatnim krokiem działania programu jest znalezienie relacji, mogących łączyć wyszukane jednostki. W tym celu zostają porównane wszystkie znalezione obiekty jak i wszystkie znalezione ich cechy ze sobą, tak by wyszukać jak najwięcej relacji ich łączących.

Ostatnia opcja dostępna pod numerem ‘4’ kończy działanie programu.


