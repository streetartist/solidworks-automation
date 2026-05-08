# CreateTangentArc Method (ISketchManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateTangentArc`

Creates a tangent arc.
Creates a tangent arc.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateTangentArc( _
   ByVal X1 As System.Double, _
   ByVal Y1 As System.Double, _
   ByVal Z1 As System.Double, _
   ByVal X2 As System.Double, _
   ByVal Y2 As System.Double, _
   ByVal Z2 As System.Double, _
   ByVal ArcType As System.Integer _
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
Dim ArcType As System.Integer
Dim value As SketchSegment
 
value = instance.CreateTangentArc(X1, Y1, Z1, X2, Y2, Z2, ArcType)
```

```

SketchSegment CreateTangentArc( 
   System.double X1,
   System.double Y1,
   System.double Z1,
   System.double X2,
   System.double Y2,
   System.double Z2,
   System.int ArcType
)
```

```

SketchSegment^ CreateTangentArc( 
   System.double X1,
   System.double Y1,
   System.double Z1,
   System.double X2,
   System.double Y2,
   System.double Z2,
   System.int ArcType
) 
```

#### Parameters

*X1*
:   X coordinate of start point in meters

*Y1*
:   Y coordinate of start point in meters

*Z1*
:   Z coordinate of start point in meters

*X2*
:   X coordinate of end point in meters

*Y2*
:   Y coordinate of end point in meters

*Z2*
:   Z coordinate of end point in meters

*ArcType*
:   Type of tangent arc as defined in [swTangentArcTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTangentArcTypes_e.html)

#### Return Value

[Sketch segment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md) of the tangent arc

Example

[Create Tangent Arc (VBA)](Create_Tangent_Arc_Example_VB.htm)  
[Create Tangent Arc (VB.NET)](Create_Tangent_Arc_Example_VBNET.htm)  
[Create Tangent Arc (C#)](Create_Tangent_Arc_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)
