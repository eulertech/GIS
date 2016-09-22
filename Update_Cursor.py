def Update_Cursor(workDir, fileName):
    #Name: Update Cursor.py
    #Description: Shift shapefile dx,dy
    #Input: workDir, r"c:\work\path\to\dir\"
    #       fileName:
    #Output fileName+'shifted.shp'
    #Dr. Liang Kuang, 2016/04/15

    import os
    from os import path
    import arcpy
    from arcpy import env



    #Set environment settings
    env.workspace = workDir

    strList = fileName.split('.')
    outFileName = strList[0] + 'shifted.shp'

    #Execute Updatecursor
    shapeField = arcpy.Describe(fileName).ShapeFileName

    deltaX = -300
    deltaY = +300

    c = arcpy.UpdateCursor(fileName)

    for row in c:
        partnum = 0
        feat = row.getValue(shapefield)
        for part in feat:
            for pnt in feat.getPart(partnum):
                pnt.X = pnt.X + deltaX
                pnt.Y = pnt.Y + deltaY

        c.updateRow(row)


        
    
