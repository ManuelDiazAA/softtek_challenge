# softtek_challenge

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [API Routes](#api-routes)
* [Testing](#testing)

## General info
This project is a tecnical test for softek
	
## Technologies
Project is created with:
* Python: 3.10
* Pandas: 1.5.3
* Flask: 2.2.3
	
## Setup
To run this project:
1. Create a new Virtual Enviroment
2. Install requeriments.txt with pip
3. This project include the sqlite file ("main.db") but you can create a new one running "prepare_db.py" file
4. Run local server debug
```
python ./app/app.py
```

## API Routes
The local sever is allocated in por 5000, and these are the endpoinds for challenges
1.- /get_ord_status for challenge 1
2.- /get_ord_season for challenge 2
3.- /get_weather_change for challenge 3

## Testing
Run the nex command to run the testing
```
python -m unittest discover ./test/
```
