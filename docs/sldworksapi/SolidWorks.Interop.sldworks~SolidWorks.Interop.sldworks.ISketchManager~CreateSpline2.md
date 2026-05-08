# CreateSpline2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSpline2`

Obsolete. Superseded by ISketchManager::CreateSpline3.
Obsolete. Superseded by [ISketchManager::CreateSpline3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSpline3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateSpline2( _
   ByVal PointData As System.Object, _
   ByVal SimulateNaturalEnds As System.Boolean _
) As SketchSegment
```

```

Dim instance As ISketchManager
Dim PointData As System.Object
Dim SimulateNaturalEnds As System.Boolean
Dim value As SketchSegment
 
value = instance.CreateSpline2(PointData, SimulateNaturalEnds)
```

```

SketchSegment CreateSpline2( 
   System.object PointData,
   System.bool SimulateNaturalEnds
)
```

```

SketchSegment^ CreateSpline2( 
   System.Object^ PointData,
   System.bool SimulateNaturalEnds
) 
```

#### Parameters

*PointData*
:   Array of X,Y,Z point coordinates to use in creating the spline (see **Remarks**)

*SimulateNaturalEnds*
:   True to simulate natural ends, false to not simulate natural ends

#### Return Value

[Sketch segment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md) for the spline

Remarks

This method creates a spline in the active 2D sketch. If a sketch is not active, then a new sketch is created. Use [ISketchManager::ActiveSketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~ActiveSketch.md) to check if the sketch active.

The PointData array is a set of, at least, two X, Y, Z values. For example, in VBA and VB.NET, the X value for the start point of the spline is PointData[0], the Y value for the start point is PointData[1], and the Z value for the start point is PointData[2]. The X value for the next point is PointData[3], and so on.

This method does not work with [ISketchManager::AddToDB](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~AddToDB.md) or [ISketchManager::DisplayWhenAdded](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~DisplayWhenAdded.md). It always adds the spline directly to the database (as if ISketchManager::AddToDB(True) was in effect), and you must redraw your document window to see the entities that you added (as if ISketchManager::DisplayWhenAdded(False) was in effect).

In 2D sketches, SOLIDWORKS ignores the Z value in PointData.

Example

[Insert a Composite Curve (C#)](Insert_a_Composite_Curve_Example_CSharp.htm)  
[Insert a Composite Curve (VB.NET)](Insert_a_Composite_Curve_Example_VBNET.htm)  
[Insert a Composite Curve (VBA)](Insert_a_Composite_Curve_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)  
[ISketchManager::ICreateSpline2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~ICreateSpline2.md)  
[ISketchManager::CreateSplineByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSplineByEqnParams.md)  
[ISketchManager::CreateSplinesByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSplinesByEqnParams.md)  
[ISketchManager::ICreateSplineByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~ICreateSplineByEqnParams.md)  
[ISketchManager::ICreateSplinesByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~ICreateSplinesByEqnParams.md)
