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

integration with other tools:

- [ ] [pandas to numpy](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_numpy.html)
- [ ] [pastas ARMA](https://github.com/pastas/pastas)
- [ ] [scipy interpolate](https://docs.scipy.org/doc/scipy/reference/tutorial/interpolate.html)
- [ ] [bokeh time series plot](https://docs.bokeh.org/en/latest/)
- [ ] [bottle single page app](http://bottlepy.org/docs/dev/index.html)

## docs and links

[hydrofunctions docs](https://hydrofunctions.readthedocs.io/en/master/index.html)

[NWIS Help System](https://help.waterdata.usgs.gov/faq/automated-retrievals)

[USGS Water Services](https://waterservices.usgs.gov/)

[GAGES II](https://water.usgs.gov/GIS/metadata/usgswrd/XML/gagesII_Sept2011.xml)

[Fox River Gage](https://waterdata.usgs.gov/monitoring-location/040851385/#parameterCode=00065&period=P7D)

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

find NWIS sites to query against:

- stream gauge: Fox River GB gauge
- groundwater well

in a jupyter notebook and other places that make sense:

- find data codes
    - discharge
    - stage/head
- pull data for services and at fixed time delta with all tools
- directly compare returned data
    - data match between tools
    - congruent data structures (dict, list, dataframe, array)
    - obvious and non obvious data processing
- pull together integration examples
    - json to pandas to numpy
    - pastas arma
    - scipy interpolation
    - scikit regeression
- examine interfaces
    - docstrings
    - functions signatures
    - custom errors
    - structure
    - modules, functions, classes, and objects
- repo background   
    - commits, issues, and branches
    - CI/CD
    - versioning and releases   
    - unit and intergration tests
    - pypi and conda downloads

