# CreateCenterLine Method (ISketchManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateCenterLine`

Creates a center line between the specified points.
Creates a center line between the specified points.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateCenterLine( _
   ByVal X1 As System.Double, _
   ByVal Y1 As System.Double, _
   ByVal Z1 As System.Double, _
   ByVal X2 As System.Double, _
   ByVal Y2 As System.Double, _
   ByVal Z2 As System.Double _
) As SketchSegment
```

```

Dim instance As ISketchManager
Dim X1 As System.Double
Dim Y1 As System.Double
Dim Z1 As System.Double
Dim X2 As System.Double
Dim Y2 As System.Double
Dim Z2 As System.Double
Dim value As SketchSegment
 
value = instance.CreateCenterLine(X1, Y1, Z1, X2, Y2, Z2)
```

```

SketchSegment CreateCenterLine( 
   System.double X1,
   System.double Y1,
   System.double Z1,
   System.double X2,
   System.double Y2,
   System.double Z2
)
```

```

SketchSegment^ CreateCenterLine( 
   System.double X1,
   System.double Y1,
   System.double Z1,
   System.double X2,
   System.double Y2,
   System.double Z2
) 
```

#### Parameters

*X1*
:   X coordinate of first end point, in meters

*Y1*
:   Y coordinate of first end point, in meters

*Z1*
:   Z coordinate of first end point, in meters

*X2*
:   X coordinate of second end point, in meters

*Y2*
:   Y coordinate of second end point, in meters

*Z2*
:   Z coordinate of second end point, in meters

#### Return Value

[Sketch segment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md) for the center line

Remarks

You can also create centerline construction geometry using [ISketchManager::CreateLine](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateLine.md) and [ISketchSegment::ConstructionGeometry](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~ConstructionGeometry.md).

Example

[Create 3D Sketch Plane (C#)](Create_3D_Sketch_Plane_Example_CSharp.htm)  
[Create 3D Sketch Plane (VB.NET)](Create_3D_Sketch_Plane_Example_VBNET.htm)  
[Create 3D Sketch Plane (VBA)](Create_3D_Sketch_Plane_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)
