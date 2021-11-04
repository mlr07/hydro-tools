# hydro-tools

sandbox to evaluate open source hydro data retrieval tools.

tools evaluated have ability to retrieve data timeseries data from NWIS.

sandbox is running on a linux box with `python 3.8` and `jupyter lab`.

tools checked if they have been evaluated in `hydro-tools.ipynb`.

hydro tools:

- [x] [dataretrieval](https://github.com/USGS-python/dataretrieval)
- [x] [hydrofunctions](https://github.com/mroberge/hydrofunctions)
- [ ] [pygeohyrdo](https://github.com/cheginit/pygeohydro)
- [ ] [ulmo](https://github.com/ulmo-dev/ulmo)
- [ ] [well application](https://github.com/utah-geological-survey/WellApplication)
- [ ] [climata]()https://github.com/heigeo/climata
- [ ] [pydrograph](https://github.com/aleaf/pydrograph)

integration with other tools:

- [x] [pandas to numpy](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_numpy.html)
- [ ] [pastas ARMA](https://github.com/pastas/pastas)
- [ ] [scipy interpolate](https://docs.scipy.org/doc/scipy/reference/tutorial/interpolate.html)
- [ ] [bokeh time series plot](https://docs.bokeh.org/en/latest/)
- [ ] [bottle single page app](http://bottlepy.org/docs/dev/index.html)

## docs and links

[hydrofunctions docs](https://hydrofunctions.readthedocs.io/en/master/index.html)

[NWIS Help System](https://help.waterdata.usgs.gov/faq/automated-retrievals)

[USGS Water Services](https://waterservices.usgs.gov/)

[USGS Parameter Codes](https://nwis.waterdata.usgs.gov/usa/nwis/pmc)

[GAGES II](https://water.usgs.gov/GIS/metadata/usgswrd/XML/gagesII_Sept2011.xml)

[Fox River Gage](https://waterdata.usgs.gov/monitoring-location/040851385/#parameterCode=00065&period=P7D)

[Sand Dunes Well](https://waterdata.usgs.gov/nwis/inventory?agency_code=USGS&site_no=374012105410401)

[PyPi analysis](https://packaging.python.org/guides/analyzing-pypi-package-downloads/)

[streamgaging basics](https://www.usgs.gov/mission-areas/water-resources/science/streamgaging-basics?qt-science_center_objects=0#qt-science_center_objects)

## set up

`git clone git@github.com:mlr07/hydro-tools.git`

`cd hydro-tools`

`python -m venv ~/env/hydro`

`source ~/env/hydro/bin/activate/hydro`

`sudo apt install libgdal-dev` (`pygeohydro` external requirement)

`pip install -r requirements.txt`

`python -m pytest` (test to check imports)

`jupyter lab`

## TODO

[x] find NWIS sites to query against:

- Fox River GB strean gage 040851385
- Sand Dunes CO groundwater well 374012105410401

in a jupyter notebook and other places that make sense:

look at data:

- [x] find data codes
    - discharge
    - stage/head
- [x] pull stream data for services and at fixed time delta with all tools
    - fox river river, gb streamgauge
    - 10/15/2021-10/25/2021
- [x] compare request strings
- [x] directly compare returned data
    - data match between tools
        -timestamps and data
    - congruent data structures (dict, list, dataframe, array)
    - obvious and non obvious data processing
- [ ] pull ground water data
    - sand dunes, co groundwater well
    - repeat checks for stream data

look at code:

- [x] examine interfaces
    - docstrings
    - functions signatures
    - custom errors
    - structure
    - modules, functions, classes, and objects
- [ ] repo background   
    - commits, issues, and branches
    - CI/CD
    - versioning and releases   
    - unit and intergration tests
    - pypi and conda downloads
- [ ] pull together integration examples (maybe out of scope)
    - json to pandas to numpy
    - pastas arma
    - scipy interpolation
    - scikit regeression
    - simple web app with bottle.py

