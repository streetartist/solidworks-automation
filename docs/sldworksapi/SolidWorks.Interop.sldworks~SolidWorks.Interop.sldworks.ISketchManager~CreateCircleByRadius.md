# CreateCircleByRadius Method (ISketchManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateCircleByRadius`

Creates a circle based on a center point and a specified radius.
Creates a circle based on a center point and a specified radius.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateCircleByRadius( _
   ByVal XC As System.Double, _
   ByVal YC As System.Double, _
   ByVal Zc As System.Double, _
   ByVal Radius As System.Double _
) As SketchSegment
```

```

Dim instance As ISketchManager
Dim XC As System.Double
Dim YC As System.Double
Dim Zc As System.Double
Dim Radius As System.Double
Dim value As SketchSegment
 
value = instance.CreateCircleByRadius(XC, YC, Zc, Radius)
```

```

SketchSegment CreateCircleByRadius( 
   System.double XC,
   System.double YC,
   System.double Zc,
   System.double Radius
)
```

```

SketchSegment^ CreateCircleByRadius( 
   System.double XC,
   System.double YC,
   System.double Zc,
   System.double Radius
) 
```

#### Parameters

*XC*
:   X coordinate of the circle center point in meters

*YC*
:   Y coordinate of the circle center point in meters

*Zc*
:   Z coordinate of the circle center point in meters

*Radius*
:   Radius of the circle in meters

#### Return Value

[Sketch segment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md) for the circle

Remarks

This method creates a full circle in the active 2D sketch. If a sketch is not active, then a new sketch is created. You can check for an active sketch using [ISketchManager::ActiveSketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~ActiveSketch.md).

[ISketchManager::AddToDB](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~AddToDB.md) and [ISketchManager::DisplayWhenAdded](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~DisplayWhenAdded.md) increase performance during entity creation by adding entities directly to the SOLIDWORKS database.

ISketchManager::AddToDB also avoids some of the peculiarities involved with creating entities via the user interface, such as inferencing, automatic relations, and snapping to the grid. Adding entities directly to the database also significantly increases the performance of this method. When you are done creating entities, it is important to ISketchManager::AddToDB(False), to restore SOLIDWORKS to its normal operating mode.

This method also works with ISketchManager::DisplayWhenAdded. If you have called ISketchManager::AddToDB(True), additional performance can be gained by calling ISketchManager::DisplayWhenAdded(False) to disable immediate display of entities as they are added to the database. When you are done creating all of your sketch entities, you must redraw your document window (see [IModelView::GraphicsRedraw](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GraphicsRedraw.md) or [IModelView::IGraphicsRedraw](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~IGraphicsRedraw.md)) to see the entities you added. You should also restore the original display settings by calling ISketchManager::DisplayWhenAdded(True).

To create a circle using a center point and a point on the circle, see [ISketchManager::CreateCircle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateCircle.md). To create a partial arc, see [ISketchManager::CreateArc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateArc.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)
