from sklearn.datasets import fetch_openml
from rich_dataframe import prettify

speed_dating = fetch_openml(name='SpeedDating', version=1, parser='auto')['frame']

table = prettify(speed_dating)