# mosru-gtfs [![Build Status](https://travis-ci.com/emfataliev/mosru-gtfs.svg?token=p1MD5suP99eunAoAZz1b&branch=master)](https://travis-ci.com/emfataliev/mosru-gtfs)

Программа для построения GTFS файла для Москвы. Источником данных является [API Портала открытых данных][1]

# Запуск

```shell script
pipenv shell 
pipenv install
python main.py --api-key API_KEY
```

```shell script
python main.py -h
usage: main.py [-h] --api-key API_KEY

optional arguments:
  -h, --help         show this help message and exit
  --api-key API_KEY  API key from apidata.mos.ru
```

[1]: https://apidata.mos.ru