import xmltodict
import numpy as np
from sklearn.cluster import KMeans
import pandas as pd


class pmml2sklearn:
    def __init__(self, input_location):
        xml_file = open(input_location, "r").read()

        a = dict(xmltodict.parse(xml_file))

        clusters = a["PMML"]["ClusteringModel"]["Cluster"]

        x = np.array([[eval(i["Array"]["#text"])] for i in clusters])

        self.clusters = pd.DataFrame({
            "name": [x["@name"] for x in clusters],
            "center": [x["Array"]["#text"] for x in clusters],
        })

        self.kmeans = KMeans(
            n_clusters=len(x),
            init=x, 
            n_init=1,
            random_state=1
        )
