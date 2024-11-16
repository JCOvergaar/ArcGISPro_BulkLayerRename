"""
Author: J.C. Overgaard
From: Guidehouse Digital, on behalf of the United States Small Business Administration
Created: 2024-11-15
Purpose: Rename ArcGIS layers to match standard... or make sense.... or in case you screw up and format them incorrectly the first time :)
Notes: You'll need to edit all the information in here. 
"""
import arcpy
# Define the map and layers
aprx = arcpy.mp.ArcGISProject("CURRENT")
m = aprx.listMaps("Here Am I, Your Special MapName")[0]  # map name

# replace old with new -- syntax -- "Old": "New"
layer_names = {
"crypticandindecipherablelayername": "clearandunderstandablelayername",
"MM-DD-YY_oops_now_we_need_to_order_them_by_date": "YYYYMMDD_much_better",
# ...and so on
}

# Rename layers
for layer in m.listLayers():
    if layer.name in layer_names:
        layer.name = layer_names[layer.name]

# Save the project
aprx.save()
