def ProjectRaster(workDir, inRaster,out_coor_system):
    # Name: Project_Raster.py
    # Description: Converts a raster dateset to different coordinate system.
    # Requirement: None
    # Input: working Dir, r"c:\work\path\to\dir\"
    #        inRaster filename
    #        output filename
    #        in_coor_system
    #        out_coor_system
    #        sampling algorithm
    # Output: inRaster_reproject+'.tiff'
    # Dr. Liang Kuang, 2016/02/26

    #Import system modules
    from os import path
    import arcpy
    from arcpy import env
    
	#proj = arcpy.SpatialReference(4326)  #WGS1984

    # Set environment settings
    env.workspace = workDir
    print(workDir)
    #env.workspace = r"R:\Projects\ESTOFS_for_Micronesia\Data\Bathymetry\ngdc_bathy\BAG\NorthernMarianas"

    # Set local variables
    #inRaster = "W00157_MB_8m_MLLW_Combined1.tif"
    strList = inRaster.split('.')
    outRaster = strList[0] + '_reproject.tiff' 
    print(outRaster)
    # Reproject a Raster image to different projection
    #arcpy.ProjectRaster_management(inRaster,outRaster,out_coor_system,sample_alg,"#","#","#","#")
    arcpy.ProjectRaster_management(inRaster,outRaster,out_coor_system)
    print('Projection done!')


