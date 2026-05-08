# CreateEllipse Method (ISketchManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateEllipse`

Creates an ellipse using the specified center, major-axis, and minor-axis points.
Creates an ellipse using the specified center, major-axis, and minor-axis points.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateEllipse( _
   ByVal XC As System.Double, _
   ByVal YC As System.Double, _
   ByVal Zc As System.Double, _
   ByVal XMajor As System.Double, _
   ByVal YMajor As System.Double, _
   ByVal ZMajor As System.Double, _
   ByVal XMinor As System.Double, _
   ByVal YMinor As System.Double, _
   ByVal ZMinor As System.Double _
) As SketchSegment
```

```

Dim instance As ISketchManager
Dim XC As System.Double
Dim YC As System.Double
Dim Zc As System.Double
Dim XMajor As System.Double
Dim YMajor As System.Double
Dim ZMajor As System.Double
Dim XMinor As System.Double
Dim YMinor As System.Double
Dim ZMinor As System.Double
Dim value As SketchSegment
 
value = instance.CreateEllipse(XC, YC, Zc, XMajor, YMajor, ZMajor, XMinor, YMinor, ZMinor)
```

```

SketchSegment CreateEllipse( 
   System.double XC,
   System.double YC,
   System.double Zc,
   System.double XMajor,
   System.double YMajor,
   System.double ZMajor,
   System.double XMinor,
   System.double YMinor,
   System.double ZMinor
)
```

```

SketchSegment^ CreateEllipse( 
   System.double XC,
   System.double YC,
   System.double Zc,
   System.double XMajor,
   System.double YMajor,
   System.double ZMajor,
   System.double XMinor,
   System.double YMinor,
   System.double ZMinor
) 
```

#### Parameters

*XC*
:   X coordinate of the ellipse center point

*YC*
:   Y coordinate of the ellipse center point

*Zc*
:   Z coordinate of the ellipse center point

*XMajor*
:   X coordinate of the point on the ellipse that is on the major axis

*YMajor*
:   Y coordinate of the point on the ellipse that is on the major axis

*ZMajor*
:   Z coordinate of the point on the ellipse that is on the major axis

*XMinor*
:   X coordinate of the point on the ellipse that is on the minor axis

*YMinor*
:   Y coordinate of the point on the ellipse that is on the minor axis

*ZMinor*
:   Z coordinate of the point on the ellipse that is on the minor axis

#### Return Value

[Sketch segment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md) for the ellipse

Remarks

This method creates a full ellipse in the active 2D sketch. If a sketch is not active, then a new sketch is created. You can check for an active sketch using [ISketchManager::ActiveSketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~ActiveSketch.md).

[ISketchManager::AddToDB](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~AddToDB.md) and [ISketchManager::DisplayWhenAdded](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~DisplayWhenAdded.md) increase performance during entity creation by adding entities directly to the SOLIDWORKS database.

ISketchManager::AddToDB also avoids some of the peculiarities involved with creating entities via the user interface, such as inferencing, automatic relations, and snapping to the grid. Adding entities directly to the database also significantly increases the performance of this method. When you are done creating entities, it is important to ISketchManager::AddToDB(False), to restore SOLIDWORKS to its normal operating mode.

This method also works with ISketchManager::DisplayWhenAdded. If you have called ISketchManager::AddToDB(True), additional performance can be gained by calling ISketchManager::DisplayWhenAdded(False) to disable immediate display of entities as they are added to the database. When you are done creating all of your sketch entities, you must redraw your document window (see [IModelView::GraphicsRedraw](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GraphicsRedraw.md) or [IModelView::IGraphicsRedraw](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~IGraphicsRedraw.md)) to see the entities you added. You should also restore the original display settings by calling ISketchManager::DisplayWhenAdded(True).

To create a partial ellipse, use [ISketchManager::CreateEllipticalArc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateEllipticalArc.md).

Example

[Create Ellipse (VBA)](Create_Ellipse_Example_VB.htm)  
[Create Ellipse (VB.NET)](Create_Ellipse_Example_VBNET.htm)  
[Create Ellipse (C#)](Create_Ellipse_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)  
[ISketchManager::CreateConic Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateConic.md)
