# Simplify Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~Simplify`

Reduces the number of points in a spline to increase system performance in models with complex spline curves.
Reduces the number of points in a spline to increase system performance in models with complex spline curves.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Simplify( _
   ByVal ToleranceIn As System.Double _
) 
```

```

Dim instance As ISketchSpline
Dim ToleranceIn As System.Double
 
instance.Simplify(ToleranceIn)
```

```

void Simplify( 
   System.double ToleranceIn
)
```

```

void Simplify( 
   System.double ToleranceIn
) 
```

#### Parameters

*ToleranceIn*
:   Smoothing factor, in meters, to use to simplify sketch

Remarks

The sketch must be in edit mode and a spline must be preselected.

Example

[Create Equation-driven Curve (VBA)](Create_Equation-driven_Curve_Example_VB.htm)  
[Create Equation-driven Curve (VB.NET)](Create_Equation-driven_Curve_Example_VBNET.htm)  
[Create Equation-driven Curve (C#)](Create_Equation-driven_Curve_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchSpline Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.md)  
[ISketchSpline Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline_members.md)
