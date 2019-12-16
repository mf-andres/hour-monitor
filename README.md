# Hour Monitor

Hour monitor is a cli that allows to store your work entry and exit hours and see how many hour of work remain per day, 
week and month. 

### Requirements

python 3.7.5
pip 19.3.1

## Tests

Run all tests:

~~~
pytest .
~~~

### Run

You can interact with the app via cli. To do so run the following:

~~~
python cli.py --help
python cli.py --store_entry --day 16/12/2019 --hour 9:00
python cli.py --check_day --day 16/12/2019 --hour 17:30
~~~ 