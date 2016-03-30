import FreeCAD
import Part
import os

doc = App.ActiveDocument
path = os.path.dirname(doc.FileName)

screwTable = [ 'KA1' ]

for name in screwTable:
    FreeCAD.Console.PrintLog(name+'\n')
    name = 'screw'+name
    FreeCAD.Console.PrintLog(name+'\n')
    body = doc.getObjectsByLabel(name+'Body')[0]
    head = doc.getObjectsByLabel(name+'Head')[0]
    tip = doc.getObjectsByLabel(name+'Tip')[0]
    screw = doc.getObjectsByLabel(name)[0]
    for x in range(3,6):
        filename = name+'x'+str(x)
        newDoc = App.newDocument(filename)
        body.NumberZ = (x-1)*2-1
        head.Placement.Base.z = x-4.5
        doc.recompute()
        screwCopy = newDoc.addObject('Part::Feature','Compound').Shape=screw.Shape.removeSplitter()
        newDoc.saveAs(path+'/'+filename+".FCStd")
        FreeCAD.closeDocument(filename)

