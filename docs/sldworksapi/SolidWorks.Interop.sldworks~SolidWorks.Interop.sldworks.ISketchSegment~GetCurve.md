# GetCurve Method (ISketchSegment)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~GetCurve`

Gets the underlying curve for this sketch segment.
Gets the underlying curve for this sketch segment.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCurve() As System.Object
```

```

Dim instance As ISketchSegment
Dim value As System.Object
 
value = instance.GetCurve()
```

```

System.object GetCurve()
```

```

System.Object^ GetCurve(); 
```

#### Return Value

Underlying [curve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)

Remarks

This operation only supports for [ellipse](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse.md), [line](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine.md), [arc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc.md), [spline](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.md), and [parabola](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md) sketch items. All other sketch segment types will return NULL, and S\_false for COM applications.

NOTE: Support for ellipse, line, and arc segments was introduced in SOLIDWORKS 2004.

Example

[Get Curve Spline Points (VBA)](Get_Curve_Spline_Points_Example_VB.htm)  
[Evaluate Curves Defined in Sketch Space (VBA)](Evaluate_Curves_Defined_in_Sketch_Space_Example_VB.htm)  
[Get Sketch Segment and Curve Data (VBA)](Get_Sketch_Segment_and_Curve_Data_Example_VB.htm)  
[Get Start and End Points of Spline (VBA)](Get_Start_and_End_Points_of_Spline_Example_VB.htm)  
[Get Whether Sketch Segment Is Trimmed (VBA)](Get_Whether_Sketch_Segment_is_Trimmed_or_Not_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md)  
[ISketchSegment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.md)  
[ISketchSegment::IGetCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~IGetCurve.md)
