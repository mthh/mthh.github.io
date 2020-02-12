class: first

# Outils de Communication territoriale

<br>

## M1 IDT2

<br>

### Partie 1 : Cartographie thématique / statistique
### et mise en scéne de la carte

<div style="width: 167px;position: absolute;bottom: -5px;left: 0px;">

<img src="img/logo-uga.jpg" />

</div>

<div style="margin: auto; text-align: center; position: relative; bottom: -100px; left: 20px;">
<p style="font-size: 20px;margin:auto; text-align: center">Matthieu Viry - LIG <em>(Laboratoire d'Informatique de Grenoble)</em></p>
<p style="font-size: 20px;margin:5px auto; text-align: center">🖂 <a href="maito:matthieu.viry@univ-grenoble-alpes.fr">matthieu.viry@univ-grenoble-alpes.fr</a></p>
</div>

---
class: section-change

# Séance 2

<br>

## Rappels & exercices

<br><br><br><br><br>

.center.source[(support élaboré avec l'[UMS RIATE](http://riate.cnrs.fr) dans le cadre des formations à [MAGRIT](http://magrit.cnrs.fr))]

---
class: center, middle

## Combiner les représentations pour guider la lecture de la carte

---

.center.img65[![](img/ratio.png)]

---

.center.img65[![](img/ratio_disc.png)]

???

Les cartes de discontinuités mettent en avant les limites (ou "frontières") entre les entités étudiées, en leur affectant une épaisseur relative au différentiel de valeur existant entre elles.

Deux méthodes permettent de calculer ce différentiel, on parlera ainsi soit de **discontinuité absolue** (écart absolu entre les valeurs de la variable étudiée c'est à dire max(A,B) - min(A,B)) ou de discontinuité relative (rapport max(A,B) / min(A,B)). La visualisation de lignes de discontinuités permet de mettre en exergue les ruptures spatiales des phénomènes socio-économiques étudiés, qui selon la formule de Brunet et Dolphus (1990) montre que « l’espace géographique est fondamentalement discontinu ».

Cette représentation est particulièrement pertinente lorsqu'elle peut être combinée à une représentation par aplats de couleurs (Cf. cartes de ratio).

---

![](img/discont.png)

---

## Exercice 2

.center.img70[![](img/carte_uefa.png)]

???

* **Représentation** - Les données statistiques (quantitatives) représentées à la façon d’une typologie (qualitative).
* Source – non mentionnée
* **Données** – Pas forcément à jour (2016 ?) / période considérée (depuis quand ?) / quels sont les pays qui participent à la compétition ?
* **Légende** – pas claire

---
## Exercice 2

<br><br>

**Objectif thématique** :

- Refaire la carte des pays victorieux en UEFA _Champions League_.

<br>

**Objectifs techniques** :

- Critiquer une carte et proposer des alternatives
- Trouver un fond de carte adapté
- Joindre le jeu de données au fond de carte

.center.img20[![](img/soccer_ball2.svg)]

---
## Exercice 2

<br>

**Source de données pour les fonds de carte à l'échelle du globe:**

- http://naturalearthdata.com/  
_(trouver le bon fond de carte : niveau de détails, présence des 50 pays concernés par le jeu de données, etc.)_

<br>

**Données des victoires par pays:**

- [https://mthh.github.io/carto-magrit/data_uefa.csv](https://mthh.github.io/carto-magrit/data_uefa.csv)  
.source[(Source: [https://fr.wikipedia.org/wiki/Ligue_des_champions_de_l%27UEFA](https://fr.wikipedia.org/wiki/Ligue_des_champions_de_l%27UEFA))]

.center.small[![](img/table_wikipedia.png)]


---
class: align-left

## Exercice 2

<br>

**Fonds de carte à l'échelle du globe:** http://naturalearthdata.com/

**Victoires / pays:** [https://mthh.github.io/carto-magrit/data_uefa.csv](https://mthh.github.io/carto-magrit/data_uefa.csv)

----

[1] **Critique de la carte**  
[2] **Trouver un fond de carte adapté** _(granularité spatiale, généralisation cartographique, etc.)_  
[3] **Importer géométries et données dans Magrit**  
[4] **Ajuster l’étendue géographique**  
[5] **Choisir la représentation**  
[6] **Mise en page**  

<br>

----


.center[Temps de réalisation : **🚀 15 min 🚀**]

---

## Exercice 3

<br><br>

**Objectif thématique** :

- Faire une carte statistique sur le thème des **logements vacants** sur le territoire de Grenoble Alpes Métropole

<br>

**Objectifs techniques** :

- Trouver fond de carte & données adaptés
- Sélectionner les variables d'intérêt et l'emprise de représentation des données
- Proposer une ou plusieurs des représentations adaptées
- Mettre en page la carte pour en faciliter sa lecture


<img src="img/logo_grenoble_metro.png" style="position: absolute; top: 20px; right: 50px;" />

---
class: align-left
## Exercice 3

<br>

**Données sur les logements**



➜ INSEE : [https://www.insee.fr/fr/statistiques/4171415?sommaire=4171436](https://www.insee.fr/fr/statistiques/4171415?sommaire=4171436)

➜ **Extrait** : [https://mthh.github.io/carto-magrit/data_logement.zip](https://mthh.github.io/carto-magrit/data_logement.zip)

.center.img75[![](img/insee_pop.png)]

---
class: align-left

## Exercice 3

<br>

----

[1] **Critique de la carte**  
[2] **Trouver le fond de carte adapté**  
[3] **Sélectionner les données à représenter**  
[4] **Importer géométries et données dans Magrit**  
[5] **Ajuster l’étendue géographique**  
[6] **Choisir la représentation**  
[7] **Mise en page et habillage de la carte**  

<br>

----

.center[Temps de réalisation : **🚀 35 min 🚀**]
