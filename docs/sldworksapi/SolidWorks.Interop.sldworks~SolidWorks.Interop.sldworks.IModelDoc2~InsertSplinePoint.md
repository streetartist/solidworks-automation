# InsertSplinePoint Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSplinePoint`

Inserts a spline point.
Inserts a spline point.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub InsertSplinePoint( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) 
```

```

Dim instance As IModelDoc2
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
 
instance.InsertSplinePoint(X, Y, Z)
```

```

void InsertSplinePoint( 
   System.double X,
   System.double Y,
   System.double Z
)
```

```

void InsertSplinePoint( 
   System.double X,
   System.double Y,
   System.double Z
) 
```

#### Parameters

*X*
:   X coordinate of spline point

*Y*
:   Y coordinate of spline point

*Z*
:   Z coordinate of spline point

Example

[Insert Spline Point (VBA)](Insert_Spline_Point_Example_VB.htm)  
[Insert Spline Point (VB.NET)](Insert_Spline_Point_Example_VBNET.htm)  
[Insert Spline Point (C#)](Insert_Spline_Point_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::CreateSpline Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateSpline.md)
