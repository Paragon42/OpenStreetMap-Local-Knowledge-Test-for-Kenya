#!/usr/bin/env python
# coding: utf-8

# In[1]:


import osmium
import pandas as pd
from collections import defaultdict
from shapely.geometry import shape, Point
import geopandas as gpd

class HealthcareHandler(osmium.SimpleHandler):
    
    def __init__(self, kenya_shape):
        osmium.SimpleHandler.__init__(self)
        self.users = defaultdict(int)
        self.kenya_shape = kenya_shape

    def node(self, n):
        if n.timestamp.year == 2022 and 'place' in n.tags:
            point = Point(n.location.lon, n.location.lat)
            if self.kenya_shape.contains(point):
                self.users[n.user] += 1

    def way(self, w):
        if w.timestamp.year == 2022 and 'place' in w.tags:
            try:
                # Calculate the centroid of all node locations in the way
                lon, lat = zip(*[(node.location.lon, node.location.lat) for node in w.nodes])
                point = Point(sum(lon) / len(lon), sum(lat) / len(lat))
                if self.kenya_shape.contains(point):
                    self.users[w.user] += 1
            except osmium.InvalidLocationError:
                pass

# Load the boundary data
gdf = gpd.read_file(r'C:\Users\USER\Downloads\HOT OSM\Local Knowledge Testing\geoBoundaries-HTI-ADM0_simplified.geojson')
kenya_shape = shape(gdf.geometry.iloc[0])

# Apply the handler
handler = HealthcareHandler(kenya_shape)
handler.apply_file(r'C:\Users\USER\Downloads\HOT OSM\Local Knowledge Testing\haiti-and-domrep-internal.osh.pbf', locations=True, idx='dense_file_array')

# Create the dataframe
users_df = pd.DataFrame(list(handler.users.items()), columns=['User', 'Contributions'])
print(users_df)
users_df.to_csv('haiti_place_2022.csv', index=True)


