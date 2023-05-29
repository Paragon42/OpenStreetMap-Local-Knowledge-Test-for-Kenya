#!/usr/bin/env python
# coding: utf-8

# In[3]:


import osmium

class OSMHandler(osmium.SimpleHandler):
    def __init__(self):
        super(OSMHandler, self).__init__()
        self.users = {}

    def tag_filter(self, tags):
        for tag in tags:
            if tag.k == "place":
                return True
        return False

    def node(self, n):
        if self.tag_filter(n.tags) and n.timestamp.year == 2022:
            self.users[n.user] = self.users.get(n.user, 0) + 1

    def way(self, w):
        if self.tag_filter(w.tags) and w.timestamp.year == 2022:
            self.users[w.user] = self.users.get(w.user, 0) + 1

handler = OSMHandler()
handler.apply_file(r"C:\Users\USER\Downloads\HOT OSM\Local Knowledge Testing\kenya-latest.osm.pbf")

print(f"Contributors and their contributions in 2022: {handler.users}")


# In[4]:


import osmium

class OSMHandler(osmium.SimpleHandler):
    def __init__(self):
        super(OSMHandler, self).__init__()
        self.users = {}

    def tag_filter(self, tags):
        for tag in tags:
            if tag.k == "amenity":
                return True
        return False

    def node(self, n):
        if self.tag_filter(n.tags) and n.timestamp.year == 2022:
            self.users[n.user] = self.users.get(n.user, 0) + 1

    def way(self, w):
        if self.tag_filter(w.tags) and w.timestamp.year == 2022:
            self.users[w.user] = self.users.get(w.user, 0) + 1

handler = OSMHandler()
handler.apply_file(r"C:\Users\USER\Downloads\HOT OSM\Local Knowledge Testing\kenya-latest.osm.pbf")

print(f"Contributors and their contributions in 2022: {handler.users}")


# In[5]:


import osmium

class OSMHandler(osmium.SimpleHandler):
    def __init__(self):
        super(OSMHandler, self).__init__()
        self.users = {}

    def tag_filter(self, tags):
        for tag in tags:
            if tag.k == "healthcare":
                return True
        return False

    def node(self, n):
        if self.tag_filter(n.tags) and n.timestamp.year == 2022:
            self.users[n.user] = self.users.get(n.user, 0) + 1

    def way(self, w):
        if self.tag_filter(w.tags) and w.timestamp.year == 2022:
            self.users[w.user] = self.users.get(w.user, 0) + 1

handler = OSMHandler()
handler.apply_file(r"C:\Users\USER\Downloads\HOT OSM\Local Knowledge Testing\kenya-latest.osm.pbf")

print(f"Contributors and their contributions in 2022: {handler.users}")


# In[ ]:





# In[ ]:





# In[1]:


import osmium
import pandas as pd
import geopandas as gpd
from shapely.geometry import shape, Point
from collections import defaultdict

class HistoryHandler(osmium.SimpleHandler):
    def __init__(self, kenya_shape):
        super(HistoryHandler, self).__init__()
        self.users = defaultdict(int)
        self.kenya_shape = kenya_shape

    def node(self, n):
        if 'place' in n.tags and n.timestamp.year == 2022:
            point = Point(n.location.lon, n.location.lat)
            if self.kenya_shape.contains(point):
                self.users[n.user] += 1


# Load the GeoJSON file
gdf = gpd.read_file(r'https://geodata.ucdavis.edu/gadm/gadm4.1/json/gadm41_KEN_0.json')

# Convert it to a shapely geometry
kenya_shape = shape(gdf.geometry.iloc[0])

handler = HistoryHandler(kenya_shape)
handler.apply_file(r'C:\Users\USER\Downloads\HOT OSM\Local Knowledge Testing\kenya-internal.osh.pbf')

users_df = pd.DataFrame(list(handler.users.items()), columns=['User', 'Contributions'])
print(users_df)
users_df.to_csv('osm_2022.csv', index=False)


# In[ ]:


import osmium
import pandas as pd
import geopandas as gpd
from shapely.geometry import shape, Point
from collections import defaultdict

class HistoryHandler(osmium.SimpleHandler):
    def __init__(self, kenya_shape):
        super(HistoryHandler, self).__init__()
        self.users = defaultdict(int)
        self.kenya_shape = kenya_shape

    def node(self, n):
        if 'place' in n.tags and n.timestamp.year == 2022:
            point = Point(n.location.lon, n.location.lat)
            if self.kenya_shape.contains(point):
                self.users[n.user] += 1


# Load the GeoJSON file
gdf = gpd.read_file(r'https://geodata.ucdavis.edu/gadm/gadm4.1/json/gadm41_KEN_0.json')

# Convert it to a shapely geometry
kenya_shape = shape(gdf.geometry.iloc[0])

handler = HistoryHandler(kenya_shape)
handler.apply_file(r'C:\Users\USER\Downloads\HOT OSM\Local Knowledge Testing\kenya-internal.osh.pbf')

users_df = pd.DataFrame(list(handler.users.items()), columns=['User', 'Contributions'])
print(users_df)
users_df.to_csv('osm_2022.csv', index=False)


# In[5]:


import osmium
import pandas as pd
import geopandas as gpd
from shapely.geometry import shape, Point
from collections import defaultdict

class HistoryHandler(osmium.SimpleHandler):
    def __init__(self, kenya_shape):
        super(HistoryHandler, self).__init__()
        self.users = defaultdict(int)
        self.kenya_shape = kenya_shape

    def node(self, n):
        if 'place' in n.tags and n.timestamp.year == 2022:
            point = Point(n.location.lon, n.location.lat)
            if self.kenya_shape.contains(point):
                self.users[n.user] += 1

    def way(self, w):
        if 'healthcare' in w.tags and w.timestamp.year == 2022:
            try:
                # Take the first node of the way as a representative point
                node = w.nodes[0].location
                point = Point(node.lon, node.lat)
                if self.kenya_shape.contains(point):
                    self.users[w.user] += 1
            except osmium.InvalidLocationError:
                # Skip this way if the node location is invalid  
                pass


# Load the GeoJSON file
gdf = gpd.read_file(r'https://geodata.ucdavis.edu/gadm/gadm4.1/json/gadm41_KEN_0.json')

# Convert it to a shapely geometry
kenya_shape = shape(gdf.geometry.iloc[0])

handler = HistoryHandler(kenya_shape)
handler.apply_file(r'C:\Users\USER\Downloads\HOT OSM\Local Knowledge Testing\kenya-internal.osh.pbf')

users_df = pd.DataFrame(list(handler.users.items()), columns=['User', 'Contributions'])
print(users_df)
users_df.to_csv('osm_contributorshealthcare_2022.csv', index=False)


# In[ ]:





# In[2]:


import osmium
import pandas as pd
from collections import defaultdict


# In[7]:


class HealthcareHandler(osmium.SimpleHandler):
    def __init__(self, kenya_shape):
        osmium.SimpleHandler.__init__(self)
        self.users = defaultdict(int)
        self.kenya_shape = kenya_shape

    def node(self, n):
        if n.timestamp.year == 2022 and 'healthcare' in n.tags:
            point = Point(n.location.lon, n.location.lat)
            if self.kenya_shape.contains(point):
                self.users[n.user] += 1

    def way(self, w):
        if w.timestamp.year == 2022 and 'healthcare' in w.tags:
            try:
                # Calculate the centroid of all node locations in the way
                lon, lat = zip(*[(node.location.lon, node.location.lat) for node in w.nodes])
                point = Point(sum(lon) / len(lon), sum(lat) / len(lat))
                if self.kenya_shape.contains(point):
                    self.users[w.user] += 1
            except osmium.InvalidLocationError:
                pass

# apply the file
handler = HealthcareHandler(r'https://geodata.ucdavis.edu/gadm/gadm4.1/json/gadm41_KEN_0.json')
handler.apply_file(r'C:\Users\USER\Downloads\HOT OSM\Local Knowledge Testing\kenya-internal.osh.pbf', locations=True, idx='dense_file_array')

# create the dataframe
users_df = pd.DataFrame(list(handler.users.items()), columns=['User', 'Contributions'])
print(users_df)


# In[2]:


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
        if n.timestamp.year == 2022 and 'healthcare' in n.tags:
            point = Point(n.location.lon, n.location.lat)
            if self.kenya_shape.contains(point):
                self.users[n.user] += 1

    def way(self, w):
        if w.timestamp.year == 2022 and 'healthcare' in w.tags:
            try:
                # Calculate the centroid of all node locations in the way
                lon, lat = zip(*[(node.location.lon, node.location.lat) for node in w.nodes])
                point = Point(sum(lon) / len(lon), sum(lat) / len(lat))
                if self.kenya_shape.contains(point):
                    self.users[w.user] += 1
            except osmium.InvalidLocationError:
                pass

# Load the boundary data
gdf = gpd.read_file(r'https://geodata.ucdavis.edu/gadm/gadm4.1/json/gadm41_KEN_0.json')
kenya_shape = shape(gdf.geometry.iloc[0])

# Apply the handler
handler = HealthcareHandler(kenya_shape)
handler.apply_file(r'C:\Users\USER\Downloads\HOT OSM\Local Knowledge Testing\kenya-internal.osh.pbf', locations=True, idx='dense_file_array')

# Create the dataframe
users_df = pd.DataFrame(list(handler.users.items()), columns=['User', 'Contributions'])
print(users_df)
users_df.to_csv('healthcare_2022.csv', index=True)



# In[ ]:




