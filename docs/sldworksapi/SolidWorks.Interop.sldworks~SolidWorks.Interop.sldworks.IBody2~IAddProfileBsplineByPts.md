# IAddProfileBsplineByPts Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IAddProfileBsplineByPts`

Adds a profile B-spline.
Adds a profile B-spline.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IAddProfileBsplineByPts( _
   ByVal NumPoints As System.Integer, _
   ByRef PointArray As System.Double _
) As Curve
```

```

Dim instance As IBody2
Dim NumPoints As System.Integer
Dim PointArray As System.Double
Dim value As Curve
 
value = instance.IAddProfileBsplineByPts(NumPoints, PointArray)
```

```

Curve IAddProfileBsplineByPts( 
   System.int NumPoints,
   ref System.double PointArray
)
```

```

Curve^ IAddProfileBsplineByPts( 
   System.int NumPoints,
   System.double% PointArray
) 
```

#### Parameters

*NumPoints*
:   Number of B-spline points

*PointArray*
:   0-based array of 3 \* NumPoints doubles

#### Return Value

Pointer to the profile B-spline, [ICurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::AddProfileBsplineByPts Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~AddProfileBsplineByPts.md)
