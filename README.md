# CI-CD

Auteurs : 
Massudom Josepha,
Koularambaye Romeo et
Kameni Gabriel

Specialité SQR

## Nous avons choisi le Sujet guidé : Un chemin tout tracé
L'objectif est de créer une API Flask pour de la gestion CRUD d’un système de transaction.

Dans ce projet, nous allons utiliser le langage *Python* car c'est un langage flexible et relativement simple à comprendre. Mais surtout, c'est celui avec lequel nous avons l'habitude de coder. 

Etant donné que nous découvrons l'intégration continue et le déploiement continu (CI/CD), nous avons opté pour le sujet guidé afin de le réaliser en totalité au vu du fait que les instructions sont bien définies et mieux explicites.


## Préparation de l'intégration continue (CI)
Ici, nous allons créer différentes github actions.

Badge de la github action pour une action déclenchée à chaque changement pour builder l’application: [![Build](https://github.com/gabi49/4A_SQR_GJR_CI-CD/actions/workflows/build.yml/badge.svg)](https://github.com/gabi49/4A_SQR_GJR_CI-CD/actions/workflows/build.yml)

Badge de la github action déclenchée manuellement pour utiliser le fichier Dockerfile pour créer une image: [![Image Build](https://github.com/gabi49/4A_SQR_GJR_CI-CD/actions/workflows/build_Docker.yml/badge.svg?branch=main)](https://github.com/gabi49/4A_SQR_GJR_CI-CD/actions/workflows/build_Docker.yml)

Badge  de la github action déclenchée pour chaque tag semver pour utiliser le fichier Dockerfile pour créer et
pousser l’image de l’API avec en tag la version semver spécifiée: [![Docker push GCR](https://github.com/gabi49/4A_SQR_GJR_CI-CD/actions/workflows/Docker_push.yml/badge.svg)](https://github.com/gabi49/4A_SQR_GJR_CI-CD/actions/workflows/Docker_push.yml)


### Procédure de chargement de données dans l'API à partir d'un fichier.csv

Avec la méthode open('data.csv'), on ouvre notre fichier, puis on le parcours et pour chaque ligne de celui ci, on récupère les éléments sender, receiver, time et amount avec lesquels on va former une nouvelle transaction et on fait un append() pour l'ajouter à notre liste de transactions.

### Fichier swagger.yaml : https://github.com/gabi49/4A_SQR_GJR_CI-CD/blob/main/4A_SQR_GJR_CI-CD.yaml

## Anticipation du déploiement continu (CD)

Nous publions  automatiquement les nouvelles versions dans un registre de conteneur Google (GCR).

[![Docker push GCR](https://github.com/gabi49/4A_SQR_GJR_CI-CD/actions/workflows/Docker_push.yml/badge.svg)](https://github.com/gabi49/4A_SQR_GJR_CI-CD/actions/workflows/Docker_push.yml)


## Amélioration de l'API

Déployons une release publique de l’API à ce stade via GitHub avec un tag équivalent à la bonne version sémantique

[![Docker push GCR](https://github.com/gabi49/4A_SQR_GJR_CI-CD/actions/workflows/Docker_push.yml/badge.svg)](https://github.com/gabi49/4A_SQR_GJR_CI-CD/actions/workflows/Docker_push.yml)

Vérifions l’intégrité des données envoyées en recalculant les hashs à partir des données envoyées et en les comparant avec les hashs stockés
précédemment: 

[![Docker push GCR](https://github.com/gabi49/4A_SQR_GJR_CI-CD/actions/workflows/Docker_push.yml/badge.svg)](https://github.com/gabi49/4A_SQR_GJR_CI-CD/actions/workflows/Docker_push.yml)

Corrigeons le calcul de hash en prenant en compte le paramètre t : la date de transfert:


#### Github actions

![alttext](https://th.bing.com/th/id/OIP.BNlMMtzkKh4G49JGfp83gwHaFj?pid=ImgDet&rs=1)

![NewPush](https://github.com/gabi49/CI-CD/actions/workflows/blank.yml/badge.svg)





