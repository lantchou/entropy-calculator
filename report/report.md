# Inleiding tot de Telecommunicatie - Verslag Opdracht 1

__Naam student__ : Liouka Antchougov

## Uitleg over implementatie
Ik heb ervoor gekozen om mij te focussen op tekstbestanden. Mijn implementatie is geschreven in Python.

Het programma verwacht twee argumenten:

- Tekst waarvoor de entropie berekend moet worden. Dit moet meegegeven worden via standaardinvoer.
- De grootte N van het geheugen van de informatiebron. Dit moet meegegeven worden als command line argument, en dit moet een geheel, niet-negatief getal zijn.

Een voorbeeldoproep waarbij er uit wordt gegaan van een geheugenloze bron ziet er zo uit:

```bash
echo "aaabbbccc" | python3 entropy.py 0 
```

Het programma print de entropie van de tekstbron naar standaarduitvoer. De uitvoer van de bovenstaande voorbeeldoproep is als volgt:

``` Entropy with memory size 0 = 1.8954618442383218```

## Vraag 1

De 3 tekstdocumenten wiens entropieën ik heb gekozen om te vergelijken zijn: een liedje, een hoofdstuk uit Roy Fielding's proefschrift over REST, en een pseudo-random tekst. Deze documenten heb ik gestoken in de folder `input`.



Als we uitgaan van een geheugenloze bron, hebben het liedje en het proefschrift hebben met respectievelijke entropieën van 4,37 en 4,36 bijna identieke entropieën. Dit hoeft ons niet te verbazen. Het zijn beiden teksten geschreven in de Engelse taal, en dus zullen de tekens in beide teksten hoogstwaarschijnlijk ongeveer dezelfde probabiliteiten hebben.



De pseudo-random tekst heeft daarentegen een hogere entropie van 5,97. De tekst heeft nochtans een alfabet dat niet te hard verschilt van die van de Engelse teksten, dus ligt de hoge entropie duidelijk aan het feit dat de kansverdeling van de tekens ongeveer uniform verdeeld is. Dit veroorzaakt dus een entropie die dichtkomt bij de maximale entropie van het alfabet waarmee de tekst gegenereerd is.



