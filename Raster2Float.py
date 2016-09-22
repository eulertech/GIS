def Raster2Float(workDir, inRaster):
    # Name: Raster2Float.py
    # Description: Converts a raster dateset to float.
    # Requirement: None
    # Input: working Dir, r"c:\work\path\to\dir\"
    #        Raster filename
    # Output: inRaster+'.flt'
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
    # inRaster = "W00157_MB_8m_MLLW_Combined1.tif"
    strList = inRaster.split('.')
    outFloat = strList[0] + '.flt' 

    # Execute Raster2Point
    arcpy.RasterToFloat_conversion(inRaster,outFloat)

    print('Raster successfully converted to float DEM!')



