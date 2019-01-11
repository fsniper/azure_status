# Azure Status

This is a python package which scrapes [Azure Status Health page](https://azure.microsoft.com/en-gb/status/)

## Usage

```
from azure_status import AzureStatus
a.status()
stats = a.status()

stat[0]
'Last updated 19 seconds ago'

stat[1]['americas']['compute']['virtual_machines']
{'east_us': 'good', 'east_us_2': 'good', 'central_us': 'good', 'north_central_us': 'good', 'south_central_us': 'good', 'west_central_us': 'good', 'west_us': 'good', 'west_us_2': 'good', 'canada_east': 'good', 'canada_central': 'good', 'brazil_south': 'good'}
```

All the keys are lower case, stripped, snake cased, and without any chars except [a-z0-9\ \.]
