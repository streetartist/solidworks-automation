# CurveDegree Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~CurveDegree`

Gets or sets the degree of curve for this Bezier curve style spline.
Gets or sets the degree of curve for this Bezier curve style spline.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CurveDegree As System.Integer
```

```

Dim instance As ISketchSpline
Dim value As System.Integer
 
instance.CurveDegree = value
 
value = instance.CurveDegree
```

```

System.int CurveDegree {get; set;}
```

```

property System.int CurveDegree {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Degree of curve or -1 if not a Bezier curve style spline

Remarks

This property is only valid for a style spline whose [curve type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~CurveType.md) is [swStyleSplineCurveType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swStyleSplineCurveType_e.html).BezierCurve.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchSpline Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.md)  
[ISketchSpline Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline_members.md)  
[ISketchSpline::IsStyleSpline Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~IsStyleSpline.md)
