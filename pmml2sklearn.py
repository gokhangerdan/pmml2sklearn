import xmltodict
import numpy as np
from sklearn.cluster import KMeans
import pandas as pd


class pmml2sklearn:
    def __init__(self, input_location):
        xml_file = open(input_location, "r").read()

        a = dict(xmltodict.parse(xml_file))

        clusters = a["PMML"]["ClusteringModel"]["Cluster"]
        fields = a["PMML"]["ClusteringModel"]["ClusteringField"]
        x = np.array([[eval(x) for x in i["Array"]["#text"].split(" ")] for i in clusters])
        a = {
            "name": [x["@name"] for x in clusters],
        }
        for n, i in enumerate(fields):
            a[i["@field"]] = [eval(i["Array"]["#text"].split(" ")[n]) for i in clusters]
        self.clusters = pd.DataFrame(a)

        self.kmeans = KMeans(
            n_clusters=len(x),
            init=x,
            n_init=1,
            random_state=1
        )
