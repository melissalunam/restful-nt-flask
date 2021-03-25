# RESTFUL - FLASK

Api de recetas

Para empezar con el proyecto ocupas tener flask:

Ocupas instalar estas librerías que se van a usar aunque ya lo configure casi todo:

`> pip install flask-jsonpify flask-sqlalchemy flask-restful`

Otra cosa para que estes moviendole de mejor manera y no estarlo corriendo a cada rato ocuparás usar el comando:

`> flask run`

Pero este no te va a funcionar sin antes hacer estos 2:

`> export FLASK_APP=app.py` 

> *OJO:* El archivo app.py es el que esta en el directorio que se te clono de github asi que trata de hacer todos los comandos que te digo desde ahí

`> export FLASK_ENV=development`

Ya que corras estos 2 comandos ya podrás usar `flask run`