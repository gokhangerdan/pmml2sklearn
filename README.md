# pmml2sklearn
Parse pmml files and convert it to sklearn kmeans models.

### Usage
```python3
>>> from pmml2sklearn import pmml2sklearn

>>> parsed_model = pmml2sklearn("your_pmml_file.pmml")

>>> # Cluster centers with cluster names parsed from pmml file:
>>> print(parsed_model.clusters)
```
```
        name              center
0  cluster_0  43.641748692028024
1  cluster_1   29.32112701093236
2  cluster_2  59.892706731733405
3  cluster_3   9.410157007171932
4  cluster_4  117.94557522123894
```
```python3
>>> # Sklearn kmeans model generated with cluster centers:
>>> print(parsed_model.kmeans)
```
```
KMeans(algorithm='auto', copy_x=True,
    init=array([[ 43.64175],
       [ 29.32113],
       [ 59.89271],
       [  9.41016],
       [117.94558]]),
    max_iter=300, n_clusters=5, n_init=1, n_jobs=None,
    precompute_distances='auto', random_state=1, tol=0.0001, verbose=0)
```
