# hydro-tools

sandbox to evaluate open source hydro data retrieval tools.

tools evaluated have some sort of ability to retrieve data from NWIS.

sandbox is running on PopOS with `python 3.9`, `ipython 7.28`, and `jupyterlab 3.2.1`.

hydro tools:
- [dataretrieval](https://github.com/USGS-python/dataretrieval)
- [hydrofunctions](https://github.com/mroberge/hydrofunctions)
- [pygeohyrdo](https://github.com/cheginit/pygeohydro)
- [ulmo](https://github.com/ulmo-dev/ulmo)
- [well application](https://github.com/utah-geological-survey/WellApplication)

additonal tools:
- [pastas](https://github.com/pastas/pastas)

## docs and links

[hydrofunctions](https://hydrofunctions.readthedocs.io/en/master/index.html)
[NWIS Help System](https://help.waterdata.usgs.gov/faq/automated-retrievals)
[USGS Water Services](https://waterservices.usgs.gov/)
[GAGES II](https://water.usgs.gov/GIS/metadata/usgswrd/XML/gagesII_Sept2011.xml)

## set up

`git clone git@github.com:mlr07/hydro-tools.git`

`cd hydro-tools`

`python -m venv hydro`

`source bin/activate/hydro`

`sudo apt install libgdal-dev` (`pygeohydro` external requirement)

`pip install -r requirements.txt`

`python -m pytest` (test to check imports)

`jupyter lab`

## TODO

find NWIS sites to query against:

- stream gauge
- groundwater well

in a jupyter notebook:

- pull data for services and at fixed time delta with all tools
- directly compare returned data
    - data match between tools
    - congruent data structures (dict, list, dataframe, array)
    - obvious and non obvious data processing
- pull together integration examples
    - pastas resampling, interpolation, etc
    - convert to geopandas
    - mapping example
- examine interfaces
    - docstrings
    - keyword arguements
    - functions and capabilities

update readme with links to repos

???


