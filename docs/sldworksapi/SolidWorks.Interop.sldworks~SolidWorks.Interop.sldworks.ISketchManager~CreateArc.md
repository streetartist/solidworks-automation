# CreateArc Method (ISketchManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateArc`

Creates an arc based on a center point, a start point, an end point, and a direction.
Creates an arc based on a center point, a start point, an end point, and a direction.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateArc( _
   ByVal XC As System.Double, _
   ByVal YC As System.Double, _
   ByVal Zc As System.Double, _
   ByVal X1 As System.Double, _
   ByVal Y1 As System.Double, _
   ByVal Z1 As System.Double, _
   ByVal X2 As System.Double, _
   ByVal Y2 As System.Double, _
   ByVal Z2 As System.Double, _
   ByVal Direction As System.Short _
) As SketchSegment
```

```

Dim instance As ISketchManager
Dim XC As System.Double
Dim YC As System.Double
Dim Zc As System.Double
Dim X1 As System.Double
Dim Y1 As System.Double
Dim Z1 As System.Double
Dim X2 As System.Double
Dim Y2 As System.Double
Dim Z2 As System.Double
Dim Direction As System.Short
Dim value As SketchSegment
 
value = instance.CreateArc(XC, YC, Zc, X1, Y1, Z1, X2, Y2, Z2, Direction)
```

```

SketchSegment CreateArc( 
   System.double XC,
   System.double YC,
   System.double Zc,
   System.double X1,
   System.double Y1,
   System.double Z1,
   System.double X2,
   System.double Y2,
   System.double Z2,
   System.short Direction
)
```

```

SketchSegment^ CreateArc( 
   System.double XC,
   System.double YC,
   System.double Zc,
   System.double X1,
   System.double Y1,
   System.double Z1,
   System.double X2,
   System.double Y2,
   System.double Z2,
   System.short Direction
) 
```

#### Parameters

*XC*
:   X coordinate of the circle center point in meters

*YC*
:   coordinate of the circle center point in meters

*Zc*
:   Z coordinate of the circle center point in meters

*X1*
:   X coordinate of the start point of the arc in meters

*Y1*
:   coordinate of the start point of the arc in meters

*Z1*
:   Z coordinate of the start point of the arc in meters

*X2*
:   X coordinate of the end point of the arc in meters

*Y2*
:   Y coordinate of the end point of the arc in meters

*Z2*
:   coordinate of the end point of the arc in meters

*Direction*
:   +1 : Go from the start point to the end point in a counter-clockwise direction

    -1 : Go from the start point to the end point in a clockwise direction

#### Return Value

[ISketchArc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc.md)

Remarks

This method creates a partial arc in the active 2D sketch. If a sketch is not active, then a new sketch is  created. You can check for an active sketch using I[SketchManager::ActiveSketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~ActiveSketch.md).

[ISketchManager::AddToDB](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~AddToDB.md) and [ISketchManager::DisplayWhenAdded](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~DisplayWhenAdded.md) increase performance during entity creation by adding entities directly to the SOLIDWORKS database.

ISketchManager::AddToDB also avoids some of the peculiarities involved with creating entities via the user interface, such as inferencing, automatic relations, and snapping to the grid. Adding entities directly to the database also increases the performance of this API. When you are done creating entities, it is important to call ISketchManager::AddToDB(False), to restore SOLIDWORKS to its normal operating mode.

This method also works with ISketchManager::DisplayWhenAdded. If you have called ISketchManager::AddToDB (True), additional performance can be gained by calling ISketchManager::DisplayWhenAdded(False) to disable immediate display of entities as they are added to the database. When you are done creating all of your sketch entities, you must redraw your document window (see [IModelView::GraphicsRedraw](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GraphicsRedraw.md) or [IModelView::IGraphicsRedraw](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~IGraphicsRedraw.md)) to see the entities that you added. You should also restore the original display settings by calling ISketchManager::DisplayWhenAdded(True).

Example

[Get Sketch Arc Data (VBA)](Get_Sketch_Arc_Data_Example_VB.htm)  
[Get Sketch Arc Data (VB.NET)](Get_Sketch_Arc_Data_Example_VBNET.htm)  
[Get Sketch Arc Data (C#)](Get_Sketch_Arc_Data_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)  
[IModelDoc2::CreateArcByCenter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateArcByCenter.md)  
[ISketchManager::Create3PointArc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~Create3PointArc.md)  
[ISketchManager::CreateTangentArc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateTangentArc.md)
