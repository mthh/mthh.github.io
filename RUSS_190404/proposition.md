Titre : L'écosystème calcul scientifique / analyse de données en Python - Quand et pourquoi (ne pas ?) utiliser R.

- Question du chapitre sur l'incertitude (je manque d'idées - en tout cas là ces 2 dernières semaines - et je ne me sens finalement pas au point comme il faudrait pour proposer un truc... je passe à coté de trucs si je fais ça etc. - mais ooportunité de pvr écrire un chapire etc;...)

Calcul représentation incertitude incomplétude (état de l'art, etc.)
Sémio et techno.

- COnstruction de la connaissance supplémentaire (-> valeur ajoutée à la connaissance).

- Question document MCD ()
- Question de l'article ICC et de ce que j'ai prévu d'e (voir autres memberes )



-> Présenter le fait que les structures de données de base en Python ne sont pas particulièrement performantes (`list`, etc.)
-> Présenter le package numpy -> Manipulation de tableaux typés de n'importe quelle dimension
-> Présenter le package pandas -> Données sous forme ligne/colonne
-> Présenter le packages xarrays -> Manipulation de données multidimensionnelles et avec labels.

-> Présenter les packages scipy, statsmodel et scikit-learn

-> Parler de matplotlib et seaborn (et des autres de l'écosystème qu'on retrouve également en R -> Plotly, Bokeh, possibilité d'exporter vers leaflet).

-> Parler de l'aspect reproductible science avec des solutions comme les notebook jupyter et jupyter lab.
Parler de l'intérêt que ça peut

-> Parler de possibilité de faire appli web avec solutions simples comme flask ou aiohttp. Et ou de possibilités d'intégrations dans d'autres appli (QGIS, blender, etc.)




-> Parler du concept de "tidy" data en R. Concept quasiment jamais mobilisé tel
quel en Python.
Mais parler de la préparation des données en Python / pour Pandas quoi qu'il en soit.
Parler de la puissance / facilité du Python pour ce qui est de l'ouverture
de fichier sous forme brute (peut être utile si on veut écrire nous même une bibliothèque pour ouvrir ce type de fichier par exemple, ou lors de récupération de fichier mal formaté, dans un mauvais format, etc)

En R : data tidying -> partie importante du nettoyage des données qui consiste en la structuration du jeu de données pour faciliter sa manipulation, sa visualiation et les modélisations à effectuer.
L'auteur qui met en avant cette notion met en avant l'envie de comprendre les facteurs cognitifs liés à l'analyse de données, notamment en vue de permettre la conception d'outils plus appropriés.


-> Faire comparaison rapide avec SQL au passage quand ça vaut le coup. Genre exemple de la suppression d'une ligne (DELETE FROM table WHERE col > 12 .. en SQL) alors que en Python / avec Pandas on va sélectionner toute les lignes à conserver (et en R on va utiliser la fonction subset).

-> Mettre en avant ls concepts qui sont propres au Python / à Pandas : alignement des données, la gestion des valeurs manquantes,

-> Insister sur le fait que les gens soient visiblement moins dogmatiques quand ils présentent l'analyse de données en Python qu'en R -> Il y a surement une phénomène intéressant -> c'est qu'ils n'ont pas confiance dans la supériorité du language dont ils font la promo.


-> Trouver des vrais cas d'usage d'analyse de données qui nécessitent le passage par d'autres languages (voir trucs qui nécessitent d'extraire des données OSM par exemple ?) pour pouvoir écrire des scripts permettant d'instrumenter une partie de la préparation des données.

-> Regarder l'état de l'écosystème permettant de faire des trucs trop gros pour la mémoire (spark, dask, etc. ?) et de l'écosystème des trucs permettant de faire du deeplearning / de l'apprentissage automatique / des réseaux neuronaux / etc. (cf. Tensorflow, keras, etc.)

-> Trouver idée de trucs géosptatial nécessitant manipulation / fusion de rasters -> Montrer exemple simple à implémenter avec rasterio et plutot compliqué avec la bibliothèque R "rasters".

-> Montrer l'intérêt d'avoir une gestion de concepts tels que "coroutine"/"thread"/"processus" au sein du language même quand c'est pour faire de l'analyse de données (et/ou encore plus quand c'est pour faire de l'analyse de données ?)

-> Montrer exemple avec changement de kernel dans jupyter -> mixage de R, Python, node.js et Rust -> gros effort pour permettre ça aussi pour des langages compilés, pour ceux qui s'en rendent compte.

->

-> Parler éventuellement d'API plus rarement utilisées mais qui ne seraient pas disponible en R -> API python pour GRASS, API python pour blender,


-> Voir pour parler d'anciens sujets qui auraient pu être traités à RUSS :
  - webscrapping
  - analyse de réseaux
  - traitement de données historiques (-> nettoyage de données avec expressions régulières)
