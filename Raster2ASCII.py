def Raster2ASCII(workDir, inRaster):
    # Name: Raster2ASCII.py
    # Description: Converts a raster dateset to ASCII features.
    # Requirement: None
    # Input: working Dir, r"c:\work\path\to\dir\"
    #        Raster filename
    # Output: inRaster+'.tif'
    # Dr. Liang Kuang, 2016/02/26

    #Import system modules
    import os
    from os import path
    import arcpy
    from arcpy import env
    


    # Set environment settings
    env.workspace = workDir
    #env.workspace = r"R:\Projects\ESTOFS_for_Micronesia\Data\Bathymetry\ngdc_bathy\BAG\NorthernMarianas"

    # Set local variables
    #inRaster = "W00157_MB_8m_MLLW_Combined1.tif"
    strList = inRaster.split('.')
    outPoint = strList[0] + '.tif' 

    # Execute Raster2ASCII
    arcpy.RasterToASCII_conversion(inRaster,outPoint)

    print('Raster successfully converted to ASCII feature!')


