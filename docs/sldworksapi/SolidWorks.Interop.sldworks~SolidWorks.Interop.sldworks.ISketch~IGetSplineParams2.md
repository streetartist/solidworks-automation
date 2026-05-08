# IGetSplineParams2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSplineParams2`

Obsolete. Superseded by ISketch::IGetSplineParameters3.
Obsolete. Superseded by [ISketch::IGetSplineParameters3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSplineParams3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetSplineParams2() As System.Double
```

```

Dim instance As ISketch
Dim value As System.Double
 
value = instance.IGetSplineParams2()
```

```

System.double IGetSplineParams2()
```

```

System.double IGetSplineParams2(); 
```

#### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

See [ISketch::GetSketchSegments](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchSegments.md) or [ISketch::IEnumSketchSegments](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IEnumSketchSegments.md) for access to individual [ISketchSegment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md) and [ISketchSpline](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.md) objects.

The return value is an array of doubles containing data for all the splines in the sketch:

> [ packedDouble1, packedDouble2, ControlPoint1[Dimension elements], ControlPoint2[Dimension elements],... knot1, knot2,..., packedDouble3, packedDouble4, packedDouble5, ]

*packedDouble1 and packedDouble2*

> The first two array elements for each spline contain four integer values holding information that describes the rest of the data in that spline's parameters:
>
> |  |  |  |
> | --- | --- | --- |
> | Spline Element | Packed Data | |
> | **low part** | **high part** |
> | 0 | Dim | Order |
> | 1 | nCtrlPoints | Periodic |
>
> where:
>
> - Dim is the number of dimensions in which the spline is defined
> - Order is the order of the spline
> - nCtrlPoints is the number of control points
> - Periodic is 1 for a closed spline or 0 for an open spline

***ControlPoint**#*

The ControlPoint data (in the sketch coordinate system) follows the two packed data elements.

***knots**#*

The number of knots depends on whether the spline is periodic or not:

|  |  |
| --- | --- |
| Periodic: | numKnots = nCtrlPoints + 1 |
| Non-Periodic: | numKnots = nCtrlPoints + Order |

***packedDouble3, packedDouble4, and packedDouble5***

The last three array elements for each spline contain five integer values holding style and layer information:

|  |  |  |
| --- | --- | --- |
| Spline Element | Packed Data | |
| **low part** | **high part** |
| i | Color | lineStyle |
| i+1 | lineWidth | Layer |
| i+2 | layerOverride | Not used |

where:

- i is the index following the last Knot or [2 + numKnots + numControlPointDoubles \* Dim]
- Color is the COLORREF value describing the color used for the *ith* spline
- lineStyle is the line style used for the ith spline. Valid values can be found in the [swLineStyles\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineStyles_e.html) enumeration
- lineWidth is line width used for the ith spline. Valid values can be found in the [swLineWeights\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineWeights_e.html) enumeration
- Layer is an integer index to the layer that the ith spline is on
- layerOverride is integer with bit flags set to determine which properties, if any, have been overridden or should be overridden.

Therefore, the size of the data for each spline is given by:

2 + numKnots + numControlPointDoubles \* Dim + 3

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)  
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.md)  
[ISketch::GetSplineParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineParams2.md)  
[ISketch::GetSplineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineCount.md)  
[ISketch::GetSplineInterpolateCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineInterpolateCount.md)  
[ISketch::GetSplines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplines.md)  
[ISketch::GetSplinesInterpolate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplinesInterpolate.md)  
[ISketch::IGetSplines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSplines.md)  
[ISketch::IGetSplinesInterpolate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSplinesInterpolate.md)
