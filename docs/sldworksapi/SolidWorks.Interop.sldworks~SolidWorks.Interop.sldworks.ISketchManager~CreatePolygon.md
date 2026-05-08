# CreatePolygon Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreatePolygon`

Creates a polygon in the active sketch.
Creates a polygon in the active sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreatePolygon( _
   ByVal XC As System.Double, _
   ByVal YC As System.Double, _
   ByVal Zc As System.Double, _
   ByVal Xp As System.Double, _
   ByVal Yp As System.Double, _
   ByVal Zp As System.Double, _
   ByVal Sides As System.Integer, _
   ByVal Inscribed As System.Boolean _
) As System.Object
```

```

Dim instance As ISketchManager
Dim XC As System.Double
Dim YC As System.Double
Dim Zc As System.Double
Dim Xp As System.Double
Dim Yp As System.Double
Dim Zp As System.Double
Dim Sides As System.Integer
Dim Inscribed As System.Boolean
Dim value As System.Object
 
value = instance.CreatePolygon(XC, YC, Zc, Xp, Yp, Zp, Sides, Inscribed)
```

```

System.object CreatePolygon( 
   System.double XC,
   System.double YC,
   System.double Zc,
   System.double Xp,
   System.double Yp,
   System.double Zp,
   System.int Sides,
   System.bool Inscribed
)
```

```

System.Object^ CreatePolygon( 
   System.double XC,
   System.double YC,
   System.double Zc,
   System.double Xp,
   System.double Yp,
   System.double Zp,
   System.int Sides,
   System.bool Inscribed
) 
```

#### Parameters

*XC*
:   X coordinate for the center

*YC*
:   Y coordinate for the center

*Zc*
:   Z coordinate for the center

*Xp*
:   X coordinate of a vertex

*Yp*
:   Y coordinate of a vertex

*Zp*
:   Z coordinate of a vertex

*Sides*
:   Number of sides in the polygon

*Inscribed*
:   True to show an inscribed construction circle, false to show a circumscribed construction circle

#### Return Value

Array of [sketch segments](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md) in the polygon

Example

[Create Polygon (VBA)](Create_Polygon_Example_VB.htm)  
[Create Polygon (VB.NET)](Create_Polygon_Example_VBNET.htm)  
[Create Polygon (C#)](Create_Polygon_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)
