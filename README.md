# ohtumini_ryhma7
[![CI](https://github.com/savalre/ohtumini_ryhma7/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/savalre/ohtumini_ryhma7/actions/workflows/main.yml)
[![codecov](https://codecov.io/gh/savalre/ohtumini_ryhma7/branch/main/graph/badge.svg?token=WXI3JMVJOM)](https://codecov.io/gh/savalre/ohtumini_ryhma7)

Ryhmän sprint ja product backlogit löytyvät [täältä](https://docs.google.com/spreadsheets/d/1PqclL4F416XCGlqTMUGlVKjF476jDCD9jPbh827wm8E/edit#gid=0).

[Loppuraportti](https://docs.google.com/document/d/1adWzlUOv29k_rxVCNEW-3Tq7hAJWsvBlkTLEd9czguM/edit?usp=sharing)

## Ohjelman asennus
Tiedostojen ladattua ensin siirry terminaalissa hakemistoon jossa on tiedosto poetry.lock.
Suorita komento:

>**poetry install**

Kun kone on asentanut riippuvuudet, siirry src hakemistoon ja suorita seuraavat käskyt.

>**poetry shell**
>
>**python3 build.py**
>
>**flask run**

Ohjelma on osoitteessa http://127.0.0.1:5000. Ohjelman suorituksen voi lopettaa sulkemalla terminaalin.

## Definition of done
 - Koodi on olemassa
 - Koodi on projektin Pylint asetusten mukainen (alustavasti Pylintin oletus)
 - Koodi on kattavasti yksikkötestattu
 - User storyn pohjalta tehdyt robot-testit menevät läpi
 - Koodi on saatettu main-branchiin pull requestin kautta, jonkun muun kuin alkuperäisen tekijän hyväksymänä

