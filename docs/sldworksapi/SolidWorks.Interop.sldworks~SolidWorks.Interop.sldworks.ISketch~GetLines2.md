# GetLines2 Method (ISketch)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetLines2`

Gets all of the lines in the sketch with an option to include or exclude crosshatch lines.
Gets all of the lines in the sketch with an option to include or exclude crosshatch lines.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetLines2( _
   ByVal CrossHatchOption As System.Short _
) As System.Object
```

```

Dim instance As ISketch
Dim CrossHatchOption As System.Short
Dim value As System.Object
 
value = instance.GetLines2(CrossHatchOption)
```

```

System.object GetLines2( 
   System.short CrossHatchOption
)
```

```

System.Object^ GetLines2( 
   System.short CrossHatchOption
) 
```

#### Parameters

*CrossHatchOption*
:   Crosshatch option as defined in [swCrossHatchFilter\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCrossHatchFilter_e.html)

#### Return Value

Array of doubles (see **Remarks**)

Remarks

The return value is the following array of doubles:

[ Color, Type, Line Font, Line Width, Layer ID, Layer Override, [Start], [End] ]

where all data values are returned as doubles:

Color = COLORREF returned as an integer. Return value could be 0 or -1 for default color.

Type = line type. Valid returns as defined in [swLineTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html). A line type is a combination of a line style and line weight.

Line Font = line style. Valid line styles as defined in [swLineStyles\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineStyles_e.html).

Line Width = integer value defining the line width. Valid width values as defined in [swLineWeights\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineWeights_e.html).

Layer ID = integer value indicating which layer holds this entity. Obtain the [ILayer](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer.md) object by passing this integer value to [ILayerMgr::GetLayerById](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~GetLayerById.md) or [ILayerMgr::IGetLayerById](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~IGetLayerById.md).

Layer Override = integer with bit flags set to determine which properties, if any, have been overridden with respect to the Layer default properties. If the bit value is set, then the specific property or properties have been overridden. The bit indicators are: color = 0x1, style = 0x2, and width = 0x4. Therefore, if LayerOverride is returned as 3, you know the color and style have been specifically set for this item and may not match the default values associated with this item's layer.

Start[3] = array of 3 doubles (X,Y,Z) describing the line start point.

End[3] = array of 3 doubles (X,Y,Z) describing the line end point.

This set of data repeats for each line in the sketch. The number of doubles returned is (lineCount \* 12). To determine the number of lines in the sketch, use [ISketch::GetLineCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetLineCount2.md).

See [ISketch::GetSketchSegments](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchSegments.md) or [ISketch::IEnumSketchSegments](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IEnumSketchSegments.md) for access to individual [ISketchSegment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md) and [ISketchLine](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine.md) objects.

Example

[Get Lines in Sketch (VBA)](Get_Lines_in_Sketch_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)  
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.md)  
[ISketch::IGetLines2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetLines2.md)  
[ISketchLine Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine.md)
