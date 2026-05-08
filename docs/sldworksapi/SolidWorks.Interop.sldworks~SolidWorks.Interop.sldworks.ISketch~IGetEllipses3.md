# IGetEllipses3 Method (ISketch)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetEllipses3`

Gets all of the ellipses in the sketch.
Gets all of the ellipses in the sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetEllipses3( _
   ByVal ArraySize As System.Integer _
) As System.Double
```

```

Dim instance As ISketch
Dim ArraySize As System.Integer
Dim value As System.Double
 
value = instance.IGetEllipses3(ArraySize)
```

```

System.double IGetEllipses3( 
   System.int ArraySize
)
```

```

System.double IGetEllipses3( 
   System.int ArraySize
) 
```

#### Parameters

*ArraySize*
:   Number of ellipses in the sketch

#### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

See [ISketch::GetSketchSegments](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchSegments.md) or [ISketch::IEnumSketchSegments](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IEnumSketchSegments.md) for access to individual [ISketchSegment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md) and [ISketchEllipse](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse.md) objects.

The return values are in an array of doubles:

[ Color, LineType, LineFont, LineWidth, LayerID, LayerOverride, StartPt[3], EndPt[3], CenterPt[3], MajorPt[3], MinorPt[3],Direction ... ]

where:

|  |  |
| --- | --- |
| Color : | COLORREF returned as an integer. Return value could be 0 or -1 for default color. |
| LineType : | Line type. Valid returns are defined in [swLineTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html). A line type is a combination of a lineStyle and lineWeight. |
| LineFont : | Value is used for polyline font information. This value can be used as an input to the [IDrawingDoc::GetLineFontInfo2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetLineFontInfo2.md) and [IDrawinDoc::GetLineFontName2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetLineFontName2.md). |
| LineWidth : | Integer value defining the line width. Valid width values as defined in [swLineWeights\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineWeights_e.html). |
| LayerID: | Integer value indicating which layer holds this entity. Obtain the [ILayer](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer.md) object by passing this integer value to [ILayerMgr::GetLayerById](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr.md) or [ILayerMgr::IGetLayerById](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~IGetLayerById.md). |
| LayerOverride: | Integer with bit flags set to determine which properties, if any, have been overridden with respect to the Layer default properties. If the bit value is set, then the specific property or properties have been overridden. The bit indicators are: color = 0x1, style = 0x2, and width = 0x4. Therefore, if LayerOverride was returned as 3, you know the color and style have been specifically set for this item and may not match the default values associated with this item's layer. |
| StartPt[3] : | Array of 3 doubles (X,Y,Z) describing the ellipse start point |
| EndPt[3] : | Array of 3 doubles (X,Y,Z) describing the ellipse end point. If the ellipse is closed, then this will be the same point as the StartPt. |
| CenterPt[3] : | Array of 3 doubles (X,Y,Z) describing the ellipse center point. |
| MajorPt[3] : | Array of 3 doubles (X,Y,Z) describing a point on the ellipse and on the major axis. |
| MinorPt[3] : | Array of 3 doubles (X,Y,Z) describing a point on the ellipse and on the minor axis. |
| Direction : | -1 for clockwise, +1 for counterclockwise |

This set of data repeats for each ellipse in the sketch. The size of the array is (NumEllipses \* 20).

To determine the number of ellipses, use [ISketch::GetEllipseCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetEllipseCount.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)  
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.md)  
[ISketch::GetEllipses3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetEllipses3.md)  
[ISketchEllipse Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse.md)
