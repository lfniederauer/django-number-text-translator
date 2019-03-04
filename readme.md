# Django Number to Text API PT_BR

Given a number between -1^65 to 1^65, returns the written number in Json.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.


### Prerequisites

Have a Docker up and running.
Clone the repository:

```
git clone XXX
```

### Installing and Running

With the terminal, access the local folder you cloned into. The root contains the Dockerfile and alike. Then run:

```
docker-compose up -d
```

The flag ```-d``` let you return to the terminal, so:

```
docker ps
curl localhost:3000/<number>
```
or from the browser curl localhost:3000/-22 returns:

```
{"extenso": "menos vinte e dois"}
```

## Authors

* **Translator API Implementation** - [Luis Filipe Niederauer](https://servicos.pro)
* **File tradutor.py** - adapted inputs and hability to hand operators - [Marcos Paulo Ferreira (Daemonio)](https://daemoniolabs.wordpress.com/2013/09/12/classe-python-de-numeros-por-extenso/)


## License

This project is licensed under the MIT License.

## Acknowledgments

“The human foot is a masterpiece of engineering and a work of art.”

― Leonardo da Vinci


 “The world would be a better place if more engineers, like me, hated technology. The stuff I design, if I’m successful, nobody will ever notice. Things will just work, and be self-managing.”

― Radia Pearlman