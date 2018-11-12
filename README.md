I don't know why, but after --import-mode pytest begins to work
pytest -v tests/test_app.py --import-mode=append

curl localhost:8080/

curl localhost:8080/filtred

## REQUIRMENTS
```
conda install -c conda-forge bottle
conda install -c conda-forge xgboost
conda install -c conda-forge schedule
conda install -c anaconda webtest
conda install schedule
```

#TODO
-- add test to engine.py
-- add test to request_filter.py
-- add config
-- add logging to server.py


https://speakerdeck.com/jakubjarosz/a-quick-look-at-webtest-and-pytest?slide=9
http://webtest.pythonpaste.org/en/latest/testapp.html#what-is-tested-by-default
https://wsgi.readthedocs.io/en/latest/frameworks.html
https://anaconda.org/anaconda/webtest
https://stackoverflow.com/questions/45256603/how-to-run-webtest-example
https://bottlepy.org/docs/0.12/recipes.html#embedding-other-wsgi-apps
