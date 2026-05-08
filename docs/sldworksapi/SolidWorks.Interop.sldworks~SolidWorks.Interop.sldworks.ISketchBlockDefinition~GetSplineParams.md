# GetSplineParams Method (ISketchBlockDefinition)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSplineParams`

Gets all the parameters of the splines in the sketch block definition.
Gets all the parameters of the splines in the sketch block definition.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSplineParams() As System.Object
```

```

Dim instance As ISketchBlockDefinition
Dim value As System.Object
 
value = instance.GetSplineParams()
```

```

System.object GetSplineParams()
```

```

System.Object^ GetSplineParams(); 
```

#### Return Value

Array of doubles, containing spline parameters (see **Remarks**)

Remarks

The return value is an array of doubles containing data for all the splines in the sketch block definitioni.

The first two array elements for each spline contain 4 integer values holding information that describes the rest of the data in that splines parameters:

|  |  |  |
| --- | --- | --- |
| Spline Element | Packed Data | |
| **low part** | **high part** |
| 0 | Dim | Order |
| 1 | nCtrlPoints | Periodic |

where:

- Dim is the number of dimensions the spline is defined in
- Order is the order of the spline
- nCtrlPoints is the number of control points
- Periodic is 1 for a closed spline or 0 for an open spline

The number of knots depends on whether the spline is periodic or not:

|  |  |
| --- | --- |
| Periodic: | numKnots = nCtrlPoints + 1 |
| Non-Periodic: | numKnots = nCtrlPoints + Order |

The last three array elements for each spline contain 5 integer values holding style and layer information:

|  |  |  |
| --- | --- | --- |
| Spline Element | Packed Data | |
| **low part** | **high part** |
| i | Color | lineStyle |
| i+1 | lineWidth | Layer |
| i+2 | layerOverride | Not used |

where:

- i is the index following the last Knot or [2 + numKnots + numControlPointDoubles \* Dim]
- Color is the COLORREF value describing the color used for the ith spline
- lineStyle is the line style used for the ith spline. Valid values can be found in the [swLineStyles\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineStyles_e.html) enumeration
- lineWidth is line width used for the ith spline. Valid values can be found in the [swLineWeights\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineWeights_e.html) enumeration
- Layer is an integer index to the layer that the ith spline is on
- layerOverride is integer with bit flags set to determine which properties, if any, have been overridden or should be overridden.

Therefore, the size of the data for each spline is given by:

2 + numKnots + numControlPointDoubles \* Dim + 3

The ControlPoint data (in the sketch coordinate system) follows the 2 packed data elements, the Knot points, and, finally, the last 3 packed data elements. Subsequent splines follow one another in the array.

[ packedDouble1, packedDouble2, ControlPoint1[Dimension elements], ControlPoint2[Dimension elements],... knot1, knot2,..., packedDouble3, packedDouble4, packedDouble5, ]

For information about unpacking double arrays into integer pairs, see:

- [Unpacking Double Arrays into Integer Paris in Visual Basic.NET and Visual Basic](sldworksAPIProgGuide.chm::/OVERVIEW/Unpacking_Double_Arrays_into_Integer_Pairs_in_Visual_Basic_.NET_and_Visual_Basic.htm)
- [Unpacking Double Arrays into Integer Pairs in C++](sldworksAPIProgGuide.chm::/OVERVIEW/PackedIntegersCPlusPlus.htm)
- [Unpacking Double Arrays into Integer Pairs in C#](sldworksAPIProgGuide.chm::/OVERVIEW/Unpacking_Double_Arrays_into_Integer_Pairs_in_C_.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.md)  
[ISketchBlockDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition_members.md)  
[ISketchBlockDefinition::GetSplineParamsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSplineParamsCount.md)  
[ISketchBlockDefinition::IGetSplineParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~IGetSplineParams.md)  
[ISketchBlockDefinition::GetSplineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSplineCount.md)  
[ISketchBlockDefinition::GetSplineInterpolateCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSplineInterpolateCount.md)  
[ISketchBlockDefinition::GetSplines2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSplines2.md)  
[ISketchBlockDefinition::GetSplinesInterpolate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSplinesInterpolate.md)  
[ISketchBlockDefinition::IGetSplines2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~IGetSplines2.md)  
[ISketchBlockDefinition::IGetSplinesInterpolate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~IGetSplinesInterpolate.md)
