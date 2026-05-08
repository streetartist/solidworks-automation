# GetPointCoordinates Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgePoint~GetPointCoordinates`

Gets the coordinates for this midpoint on an edge or an endpoint or midpoint on a reference curve.
Gets the coordinates for this midpoint on an [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) or an endpoint or midpoint on a [reference curve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GetPointCoordinates( _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
) 
```

```

Dim instance As IEdgePoint
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
 
instance.GetPointCoordinates(X, Y, Z)
```

```

void GetPointCoordinates( 
   out System.double X,
   out System.double Y,
   out System.double Z
)
```

```

void GetPointCoordinates( 
   [Out] System.double X,
   [Out] System.double Y,
   [Out] System.double Z
) 
```

#### Parameters

*X*
:   x coordinate for this midpoint or endpoint

*Y*
:   y coordinate for this midpoint or endpoint

*Z*
:   z coordinate for this midpoint or endpoint

Example

[Create Reference Curve (C#)](Create_Reference_Curve_Example_CSharp.htm)  
[Create Reference Curve (VB.NET)](Create_Reference_Curve_Example_VBNET.htm)  
[Create Reference Curve (VBA)](Create_Reference_Curve_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEdgePoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgePoint.md)  
[IEdgePoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgePoint_members.md)
