# TestCase


Usage:

    git clone https://github.com/steklyanov/image_comparsion.git

BACKEND:

    cd image_comparsion/image_comparsion
    python manage.py runserver
    redis-server
    celery -A image_comparsion worker -l info

FRONTEND:

    cd frontend
    npm install
    npm start

Backend: *Django + DRF*  
Frontend: *Vue*  
Database: *postgreSQL*  
Worker: *Celery*  
Broker: *Redis*



|       Endpoint         |  Description|
| ----------------       | ------- |
| /api/v1/person/create/                  |Create user endpoint|
| /api/v1/person/list/        |List all users|
| /api/v1/person/details/<id>           | Show detaiUpload image|
| /api/v1/person/distance/<id1>/<id2>/  | Show Euclidean distance between two images |
| /api/v1/person/details/<id>/delete/  | Delete user by id|
