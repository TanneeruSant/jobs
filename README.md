
# Commands to install if installing with requirements.txt got failed
```
conda create -n python==3.10
pip install -U python-jobspy
conda install pandas
conda install conda-forge::streamlit
pip install requests==2.31.0
conda install chardet
pip install langid
pip install geopy
```

# Adding a particular single library to requirements based on given name (Ex: here streamlit)
```
pip freeze | grep streamlit >> requirements.txt
or 
pip freeze | findstr **streamlit** >> requirements.txt
or 
pip freeze | Select-String streamlit >> requirements.txt
or
pip install pipreqs # but some times it skips few dependencies
```

# Create dependancies in right format instead of conda path
```
pip list --format=freeze > requirements.txt
```

```
plotly==6.0.0
streamlit_dynamic_filters==0.1.9
streamlit-extras==0.5.5
```

# install requirements 
```
conda install --yes --file requirements.txt
```

# prune the old objects in git
```
git repack -a -d -f --depth=250 --window=250
```


