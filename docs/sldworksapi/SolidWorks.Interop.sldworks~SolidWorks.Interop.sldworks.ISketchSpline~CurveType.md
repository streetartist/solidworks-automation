# CurveType Property (ISketchSpline)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~CurveType`

Gets or sets the type of curve for this style spline.
Gets or sets the type of curve for this style spline.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CurveType As System.Integer
```

```

Dim instance As ISketchSpline
Dim value As System.Integer
 
instance.CurveType = value
 
value = instance.CurveType
```

```

System.int CurveType {get; set;}
```

```

property System.int CurveType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Type of curve as defined in [swStyleSplineCurveType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swStyleSplineCurveType_e.html)

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
[ISketchSpline::IsStyleSpline Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~IsStyleSpline.md)
