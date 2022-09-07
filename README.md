# reserve

## Descripción

Proyecto de prueba para agendar y ver pedidos con conductores. \
Puedes ver un Demo en vivo del proyecto en [159.65.224.80/swagger/](http://159.65.224.80/swagger/).

## Requerimientos / Características

* Los usuarios se deben autenticar.
* Agendar un pedido a un conductor en una fecha y hora, y especificar su lugar de
  recogida (latitud y longitud) y destino.
* Consultar todos los pedidos asignados en un día en específico ordenados por la hora.
* Consultar todos los pedidos de un conductor en un día en específico ordenados por
  la hora
* Hacer búsquedas del conductor que esté más cerca de un punto geográfico en una
  fecha y hora. (Tener en consideración los pedidos ya asignados al conductor).
* Todo pedido dura 1 hora.
* No se usarán coordenadas reales, Las coordenadas están dadas partiendo de un
  cuadro de 100 x 100 partiendo de la coordenada 0,0 hasta la 100,100.

## Cómo utilizarlo

Puedes entrar a **127.0.0.1:8000/swagger/** para ver información de los endpoints.

## Lanzar el proyecto

* Debes crear el archivo **.env** definiendo las variables de entorno:

```
#Django
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST=
POSTGRES_PORT=
SECRET_KEY=

ALLOWED_HOSTS=
```

#### Correr el proyecto en un servidor local.

* Es necesario contar con Docker y docker-compose en tu maquina.

``` bash
make build
make up
make migrate
make statics
```

#### Construye y lanza el proyecto en tu servidor de producción.

* Es necesario contar con Docker y docker-compose en tu servidor.

``` bash
make prod-buil
make prod-run
make prod-migrate
make prod-makemessages
make prod-compilemessages
```



