# Gotta Pursue the Squeak
Clementine Galloy, Noe Faucher & Mael Triquet

<img src="rsc/logo_gpsqueak.png" width="500em">


## Architecture

![architecture](rsc/archi_gps_squeak.png)


## UI for server

### Database 
UI visible on `localhost:8081`.

serveur: `postgresql:5432`
utilisateur: `user`
mot de passe: `pass`
db: `gps_db`

### Kafka 
UI visible on `localhost:8080`.

kafka on port 9092,9093 

### api
On `localhost:8084`

### Front
On `localhost:8083`


### Lancement

```sh
    docker compose -f docker-compose-server.yml up

    docker compose -f docker-compose-producer.yml up
```


Pour relancer le front,l'api, le consumer ou le producer après modification:
```sh
docker compose -f docker-compose-server.yml down # ou docker-compose-producer.yml
docker image rm front:latest # ou api:latest ou ...
```
