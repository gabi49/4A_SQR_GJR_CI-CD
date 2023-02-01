# CI-CD

Auteurs : 
Massudom Josepha,
Koularambaye Romeo et
Kameni Gabriel

Specialité SQR

## Nous avons choisi le Sujet guidé : Un chemin tout tracé
L'objectif est de créer une API Flask pour de la gestion CRUD d’un système de transaction.

Dans ce projet, nous allons utiliser le langage Python car c'est celui avec lequel nous avons l'habitude de coder. \n
Etant donné que nous découvrons l'intégration continue et le déploiement continu (CI/CD), nous avons opté pour le sujet guidé afin de le réaliser en totalité le au vu du fait que les instructions sont bien définies et mieux explicites.


## Préparation de l'intégration continue
Ici, nous allons créer différentes github actions.

Badge de la github action pour une déclenchée à chaque changement pour builder l’application : [![Build](https://github.com/gabi49/4A_SQR_GJR_CI-CD/actions/workflows/build.yml/badge.svg)](https://github.com/gabi49/4A_SQR_GJR_CI-CD/actions/workflows/build.yml)

Badge de la github actiion pour utiliser le fichier Dockerfile pour créer une image : [![Image Build](https://github.com/gabi49/4A_SQR_GJR_CI-CD/actions/workflows/build_Docker.yml/badge.svg?branch=main)](https://github.com/gabi49/4A_SQR_GJR_CI-CD/actions/workflows/build_Docker.yml)




### Procedure de charmement de données dans l'API à partir d'un fichier.csv
Avec la methode open('data.csv'), on ouvre notre fichier, puis on le parcours et pour chaque ligne de celui_ci, on recupere les elements sender, receiver, time et amount avec lesquels on va former une nouvelle trasaction et on fait un append() pour l'ajouter à notre listre de transaction.


![alttext](https://th.bing.com/th/id/OIP.BNlMMtzkKh4G49JGfp83gwHaFj?pid=ImgDet&rs=1)


![NewPush](https://github.com/gabi49/CI-CD/actions/workflows/blank.yml/badge.svg)



