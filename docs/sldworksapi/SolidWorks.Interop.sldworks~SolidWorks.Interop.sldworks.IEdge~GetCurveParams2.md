# GetCurveParams2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetCurveParams2`

Obsolete. Superseded by IEdge::GetCurveParams3.
Obsolete. Superseded by [IEdge::GetCurveParams3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetCurveParams3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCurveParams2() As System.Object
```

```

Dim instance As IEdge
Dim value As System.Object
 
value = instance.GetCurveParams2()
```

```

System.object GetCurveParams2()
```

```

System.Object^ GetCurveParams2(); 
```

#### Return Value

Array values describing the parameterization of the edge

Remarks

Calls to this method must be preceded by a call to [IEdge::GetCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetCurve.md) or [IEdge::IGetCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetCurve.md) because SOLIDWORKS does not keep the underlying curve information. Edge::GetCurve generates this information so that you can extract the curve parameters.

You can use the data returned by this method to determine if a circular edge is a complete circle or an arc.

The return value is the following array of 11 doubles:

[ StartPtX, StartPtY, StartPtZ, EndPtX, EndPtY, EndPtZ, StartUParam, EndUParam, PackDouble1, PackDouble2, PackDouble3 ]

where PackDouble1, PackDouble2, and PackDouble3 are each a set of two integers packed into a double. These variables hold the following pair of integers:

|  |  |
| --- | --- |
| PackDouble1 | Two packed integers:   1. Unused 2. curveType as documented in [ICurve::Identity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~Identity.md) |
| PackDouble2 | Two packed integers:   1. Unused 2. curveTag |
| PackDouble3 | Two packed integers:   1. Unused 2. SenseFlag (indicates whether the curve and edge are in the same direction) |

If SenseFlag is True, then the curve and edge are in the same direction. If SenseFlag is false, then the curve and edge are in opposite directions. In this case, this method returns the start parameter (point) that corresponds to the end of the edge and the end parameter (point) that corresponds to the end of the edge.

The start parameter is always smaller than the end parameter. If the curve and edge are in opposite directions, then the start and end parameters are along the negative portion of the parameter space. For example, if the start parameter of the edge is 10 and the end parameter is 5, then the parameter range returned is -10, -5. This ensures that the start parameter is smaller than the end parameter. To correct the values for the edge, swap the two values between the start and end parameters and then negate both values so that the value of the start parameter is 5 and the end parameter is 10.

If the curve is closed and the curve starts and ends at the same point, then StartUParam and EndUParam are a period apart.

Example

[Dimension Edge in Drawing (VBA)](Dimension_Edge_in_Drawing_Example_VB.htm)  
[Get Edge Curve Parameterization (VBA)](Get_Edge_Curve_Parameterization_Example_VB.htm)  
[Get Intersecting Face and Edge (VBA)](Get_Intersecting_Face_and_Edge_Example_VB.htm)  
[Get Length of Edge (VBA)](Get_Length_of_Edge_Example_VB.htm)  
[Select Tangent Edges Via Iteration (VBA)](Select_Tangent_Edges_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)  
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.md)  
[IEdge::IGetCurveParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IGetCurveParams2.md)  
[ICoEdge::GetCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~GetCurveParams.md)  
[ICoEdge::IGetCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge~IGetCurveParams.md)  
[IEdge::IsParamReversed Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~IsParamReversed.md)
