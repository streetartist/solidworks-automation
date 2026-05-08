# IGetCurve Method (ISketchSegment)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~IGetCurve`

Gets the underlying curve for this sketch segment.
Gets the underlying curve for this sketch segment.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetCurve() As Curve
```

```

Dim instance As ISketchSegment
Dim value As Curve
 
value = instance.IGetCurve()
```

```

Curve IGetCurve()
```

```

Curve^ IGetCurve(); 
```

#### Return Value

Underlying [curve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)

Remarks

This operation only supports for [ellipse](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse.md), [line](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine.md), [arc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc.md), [spline](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.md), and [parabola](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md) sketch items. All other sketch segment types will return NULL, and S\_false for COM applications.

NOTE: Support for ellipse, line, and arc segments was introduced in SOLIDWORKS 2004.

Example

[Get Curve Spline Points (C++)](Get_Curve_Spline_Points_Example_CPlusPlus_COM.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md)  
[ISketchSegment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.md)  
[ISketchSegment::GetCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~GetCurve.md)
