# IsStyleSpline Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~IsStyleSpline`

Gets whether this spline is a style spline.
Gets whether this spline is a style spline.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property IsStyleSpline As System.Boolean
```

```

Dim instance As ISketchSpline
Dim value As System.Boolean
 
value = instance.IsStyleSpline
```

```

System.bool IsStyleSpline {get;}
```

```

property System.bool IsStyleSpline {
   System.bool get();
}
```

#### Property Value

True if a style spline, false if not

Example

[Get Style Spline Curve Type (C#)](Get_Style_Spline_Curve_Type_Example_CSharp.htm)  
[Get Style Spline Curve Type (VB.NET)](Get_Style_Spline_Curve_Type_Example_VBNET.htm)  
[Get Style Spline Curve Type (VBA)](Get_Style_Spline_Curve_Type_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchSpline Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.md)  
[ISketchSpline Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline_members.md)  
[ISketchSpline::CurveDegree Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~CurveDegree.md)  
[ISketchSpline::CurveType Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~CurveType.md)
