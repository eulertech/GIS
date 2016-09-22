def Raster2Point(workDir, inRaster):
    # Name: Raster2Point.py
    # Description: Converts a raster dateset to point features.
    # Requirement: None
    # Input: working Dir, r"c:\work\path\to\dir\"
    #        Raster filename
    #        output filename
    #        attribute name, by default: "VALUE"
    # Output: inRaster+'.shp'
    # Dr. Liang Kuang, 2016/02/26

    #Import system modules
    import os
    from os import path
    import arcpy
    from arcpy import env
    


    # Set environment settings
    env.workspace = workDir
	print(workDir)
    #env.workspace = r"R:\Projects\ESTOFS_for_Micronesia\Data\Bathymetry\ngdc_bathy\BAG\NorthernMarianas"

    # Set local variables
    #inRaster = "W00157_MB_8m_MLLW_Combined1.tif"
    strList = inRaster.split('.')
    outPoint = strList[0] + '.shp' 

    # Execute Raster2Point
    arcpy.RasterToPoint_conversion(inRaster,outPoint,"VALUE")

    print('Raster successfully converted to point feature!')


