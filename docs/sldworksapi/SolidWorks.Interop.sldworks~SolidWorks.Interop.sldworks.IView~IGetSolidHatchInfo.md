# IGetSolidHatchInfo Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSolidHatchInfo`

Gets the boundary data for all visible solid-fill hatches in a detail, break, or crop view.
Gets the boundary data for all visible solid-fill hatches in a detail, break, or crop view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetSolidHatchInfo( _
   ByVal ArraySize As System.Integer _
) As System.Double
```

```

Dim instance As IView
Dim ArraySize As System.Integer
Dim value As System.Double
 
value = instance.IGetSolidHatchInfo(ArraySize)
```

```

System.double IGetSolidHatchInfo( 
   System.int ArraySize
)
```

```

System.double IGetSolidHatchInfo( 
   System.int ArraySize
) 
```

#### Parameters

*ArraySize*
:   Size of array to allocate for the boundary data as determined by [IView::GetSolidHatchCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSolidHatchCount.md)

#### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

The return value, which is an array of doubles, describes the geometry for each hatch boundary loop in each visible solid-fill hatch in a detail or broken view. The first two array elements indicate:

- [0] 1 if the loop is an outer loop, which is the first loop in the boundary, or 0 if the loop is an inner loop in the boundary
- [1] Number of polylines in the loop

The remaining array elements describe the polyline data and include information about these types of boundary segments:

- arcs: Returned using a center point, radius, and start and stop location
- ellipses: Returned as equation parameters
- splines: Returned as equation parameters
- straight lines: Returned as tessellated polylines

The format of the remaining array elements ([2], [3], ...) of polyline data is as follows:

[ Type, GeomDataSize, GeomData[ ], LineColor, LineStyle, LineFont, LineWeight, LayerID, LayerOverride, NumPolyPoints, [x,y,z] ]

where:

Type = underlying geometry type, possible values are:

- 0 = Polyline type
- 1 = Arc or Circle type

GeomDataSize = number of elements in the GeomData array, for Type = 0 this will be 0.

GeomData[ ] = geometric data that can be used to represent the underlying geometry type. The data returned in this array is based on the underlying geometry type:

- Type = 0. This array is empty
- Type = 1. [ centerPtX, centerPtY, centerPtZ, startPtX, startPtY, startPtZ, endPtX, endPtY, endPtZ, normalX, normalY, normalZ ]

LineColor = polyline color. This value is determined either by the explicitly set value or by the layer that the polyline is on.

LineStyle = value combines polyline font and weight information. This value can be used as an input to GetLineFontInfo and GetLineFontName. If this value is -1, then the user has probably modified the line display manually in the drawing and you should use the LineFont and LineWeight return values to recreate the exact polyline style.

LineFont = value is used for polyline font information. This value can be used as an input to the GetLineFontInfo2 and GetLineFontName2 functions. This value will only be valid if LineStyle is -1.

LineWeight = polyline weight where Thin = 0.0, Normal = 1.0, Thick = 2.0. This value will only be valid if LineStyle is -1.

LayerID = integer value indicating which layer holds this polyline. The [ILayer](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer.md) object can be obtained by passing this integer value to [ILayerMgr::GetLayerById](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~GetLayerById.md) and [ILayerMgr::IGetLayerById](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~IGetLayerById.md).

LayerOverride = integer with bit flags set to determine which properties, if any, have been overridden with respect to the Layer default properties. If the bit value is set, then the specific property or properties have been overridden. The bit indicators are: color = 0x1, style = 0x2, and width = 0x4. Therefore, if LayerOverride was returned as 3, you know the color and style have been specifically set for this item and may not match the default values associated with this item's layer.

NumPolyPoints = number of XYZ points found in the [x,y,z] return value.

[x,y,z] = array of points used to describe the polyline. This array has NumPolyPoints points. This data will be returned for every polyline regardless of Type.

To get information about solid-fill hatches in drawing views, use [IView::GetFaceHatchCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFaceHatchCount.md), [IView::GetFaceHatches](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFaceHatches.md), and [IView::IGetFaceHatches](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetFaceHatches.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetSolidHatchInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSolidHatchInfo.md)  
[ISketch::GetSketchHatches Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchHatches.md)
