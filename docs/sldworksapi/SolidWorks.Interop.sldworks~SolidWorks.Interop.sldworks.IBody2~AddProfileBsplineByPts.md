# AddProfileBsplineByPts Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~AddProfileBsplineByPts`

Adds a profile B-spline.
Adds a profile B-spline.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddProfileBsplineByPts( _
   ByVal NumPoints As System.Integer, _
   ByVal PointArray As System.Object _
) As System.Object
```

```

Dim instance As IBody2
Dim NumPoints As System.Integer
Dim PointArray As System.Object
Dim value As System.Object
 
value = instance.AddProfileBsplineByPts(NumPoints, PointArray)
```

```

System.object AddProfileBsplineByPts( 
   System.int NumPoints,
   System.object PointArray
)
```

```

System.Object^ AddProfileBsplineByPts( 
   System.int NumPoints,
   System.Object^ PointArray
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
[IBody2::IAddProfileBsplineByPts Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IAddProfileBsplineByPts.md)
