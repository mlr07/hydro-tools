# hydro-tools

sandbox to evaluate open source hydro data retrieval tools.

libraries included:
- `pygeohyrdo`
- `well application`
- `hydrofunctions`
- `dataretrieval`
- `ulmo`

sandbox is running with `python 3.9`, `ipython 7.28`, and `jupyterlab 3.2.1`.

## set up

`git@github.com:mlr07/hydro-tools.git`

`cd hydro-tools`

`python -m venv hydro`

`source bin/activate/hydro`

`sudo apt install libgdal-dev` (`pygeohydro` external requirement)

`pip install -r requirements.txt`

`python -m pytest --disable-warnings` (smoke test to check imports)

## TODO

find NWIS sites to query against:

- stream gauge
- groundwater well

in a jupyter notebook:

- pull data for services and time delta with all tools
- directly compare the returned data
    - data match
    - congruent data structures (dict, list, dataframe, array)
    - obvious and non obvious data processing
- pull together integration examples
    - pastas resampling, interpolation, etc
    - convert to geopandas
    - mapping example

update readme with links to repos

???


