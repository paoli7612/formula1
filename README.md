## FORMULA 1 - paoli7612

### Requisiti
- python3
- pygame
- shapely

### Regole
Se la macchia esce dalla finestra o dal circuito viene riportato nel ultima posizione valida a velocità 0

### Giocatori
Ogni giocatore parte sulla linea di partenza con una macchina del proprio colore.
Per ora, nome, colore e posizione di partenza vengono definiti nel **main.py**.

```python
from player import Player
from match import Match

def main():
    p1 = Player("nome1", 10, 10, "red")
    p2 = Player("nome2", 10, 12, "blue")
    m = Match(p1)
    m.start()

if __name__ == "__main__":
    main()
```

### Multiplayer
Un processo **server** riceve le "decisioni" dai vari **client**; esso esegue tutti i calcoli e rimanda ai vari **clien** solo l'intera immagine della finestra, oltre ad un booleano che rappresenta la **fine partita** e quindi se qualcuno ha vinto.

#### Mappa
<img src="doc/img/Schermata del 2018-06-03 11-57-12.png">
<img src="doc/img/Schermata del 2018-06-04 19-14-40.png">
#### Partita


#### Comandi
Utilizzando i primi nove tasti a sinistra della tastiera, il giocatore può decidere una delle 9 opzioni con cui muovere la propria macchina.

<table>
  <tr><td>Q</td><td>W</td><td>E</td></tr>
  <tr><td>A</td><td>S</td><td>D</td></tr>
  <tr><td>Z</td><td>X</td><td>C</td></tr>
</table>
