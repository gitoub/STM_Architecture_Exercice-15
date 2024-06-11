# STM_Architecture_Exercice-15
Diagramme de Séquence
Le diagramme de séquence inclus dans ce repo illustre les interactions entre les différents composants de l'architecture de services lorsqu'une requête est reçue, traitée et une réponse est renvoyée. Il offre une vue détaillée du flux d'exécution des opérations.

![Diagramme de service](images/Diagramme_Service.png)

Aperçu du Projet
Ce projet consiste à concevoir et développer une architecture de services qui distribue les données de l'Index EgaPro. Le projet est réalisé en groupe de maximum 3 étudiants et implique la création de différents services, la documentation de l'architecture, ainsi que l'intégration de plusieurs schémas pour une meilleure compréhension et une utilisation facilitée.

Documentation de l'API REST avec Swagger
L'API REST développée dans le cadre de ce projet est entièrement documentée à l'aide de Swagger. Cette documentation fournit une description détaillée de chaque endpoint, des paramètres acceptés, des réponses attendues et des exemples d'utilisation.

Documentation de l'API SOAP avec WSDL
L'API SOAP développée dans ce projet est également documentée avec un fichier WSDL (Web Services Description Language). Le fichier WSDL décrit les services disponibles, les opérations qu'ils fournissent, les types de données utilisés et les protocoles de communication.

Base de Données Commune
Tous les services développés dans ce projet partagent une base de données commune. Cette base de données est conçue pour stocker les données de l'Index EgaPro et permettre aux différents services d'accéder et de manipuler ces données de manière cohérente.

Services Développés
Service de Distribution des Données EgaPro en RPC :
Ce service utilise le protocole RPC (Remote Procedure Call) pour distribuer les données de l'Index EgaPro.

Service de Distribution des Données EgaPro par API REST :
Ce service expose une API RESTful permettant d'accéder et de manipuler les données de l'Index EgaPro via des endpoints HTTP.

Service de Distribution des Données EgaPro par API SOAP :
Ce service fournit une API SOAP pour accéder aux données de l'Index EgaPro en utilisant le protocole SOAP (Simple Object Access Protocol
