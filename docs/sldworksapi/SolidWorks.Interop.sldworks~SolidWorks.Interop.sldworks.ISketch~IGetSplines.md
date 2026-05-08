# IGetSplines Method (ISketch)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSplines`

Gets information for each spline by tessellation instead of by interpolation as is done by ISketch::GetSplinesInterpolate and ISketch::IGetSplinesInterpolate.
Gets information for each spline by tessellation instead of by interpolation as is done by [ISketch::GetSplinesInterpolate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplinesInterpolate.md) and [ISketch::IGetSplinesInterpolate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSplinesInterpolate.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetSplines() As System.Double
```

```

Dim instance As ISketch
Dim value As System.Double
 
value = instance.IGetSplines()
```

```

System.double IGetSplines()
```

```

System.double IGetSplines(); 
```

#### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

See [ISketch::GetSketchSegments](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchSegments.md) or [ISketch::IEnumSketchSegments](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IEnumSketchSegments.md) for access to individual [ISketchSegment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md) and [ISketchSpline](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.md) objects.

The returned array of doubles has the format:

[ [ Color, LineType, NumSplinePoints, [x,y,z] ] ]

This complete set of data repeats itself for each spline found in the sketch. For each spline, the array returned contains the color, the line type, the number of spline points in the spline, and the X,Y,Z value for each of those points. Therefore, the [x,y,z] parameter is an array of NumSplinePoints, which may vary in size from spline to spline.

The [x,y,z] points for each spline are not the same as the points used to generate the spline. This method  tessellates the spline based on the display quality and places points along the spline appropriately. LineType may take one of the values in [swLineTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)  
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.md)  
[ISketch::GetSplines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplines.md)  
[ISketch::GetSplineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineCount.md)  
[ISketch::GetSplineInterpolateCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineInterpolateCount.md)  
[ISketch::GetSplineParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineParams2.md)  
[ISketch::GetSplineParamsCount2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineParamsCount2.md)  
[ISketch::GetSplinesInterpolate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplinesInterpolate.md)  
[ISketch::IGetSplineParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSplineParams2.md)  
[ISketch::IGetSplinesInterpolate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSplinesInterpolate.md)  
[ISketchSpline Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.md)
