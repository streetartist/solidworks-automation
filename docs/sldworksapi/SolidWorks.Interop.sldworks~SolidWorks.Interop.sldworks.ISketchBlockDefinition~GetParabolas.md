# GetParabolas Method (ISketchBlockDefinition)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetParabolas`

Gets information about all of the parabolas in this block definition.
Gets information about all of the parabolas in this block definition.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetParabolas() As System.Object
```

```

Dim instance As ISketchBlockDefinition
Dim value As System.Object
 
value = instance.GetParabolas()
```

```

System.object GetParabolas()
```

```

System.Object^ GetParabolas(); 
```

#### Return Value

Array of doubles (see **Remarks**)

Remarks

The return values are in an array of doubles:

[ Color, LineType, LineStyleIndex, LineWidth, LayerID, LayerOverride, StartPt[3], EndPt[3], FocusPt[3], ApexPt[3] ]

where:

Color = COLORREF returned as an integer. Return value could be 0 or -1 for default color.

LineType = line type. Valid returns as defined in [swLineTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html). A LineType is a combination of a line style and line weight.

LineStyleIndex = line style. Valid line styles as defined in [swLineStyles\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineStyles_e.html).

LineWidth = integer value defining the line width. Valid width values as defined in [swLineWeights\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineWeights_e.html).

LayerID = integer value indicating which layer holds this entity. Obtain the [ILayer](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer.md) object by passing this integer value to [ILayerMgr::GetLayerById](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~GetLayerById.md) or [ILayerMgr::IGetLayerById](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~IGetLayerById.md).

LayerOverride = integer with bit flags set to determine which properties, if any, have been overridden with respect to the Layer default properties. If the bit value is set, then the specific property or properties have been overridden. The bit indicators are: color = 0x1, style = 0x2, and width = 0x4. Therefore, if LayerOverride was returned as 3, you know the color and style have been specifically set for this item and may not match the default values associated with this item's layer.

StartPt[3] = array of 3 doubles (X,Y,Z) describing the parabola start point.

EndPt[3] = array of 3 doubles (X,Y,Z) describing the parabola end point.

FocusPt[3] = array of 3 doubles (X,Y,Z) describing the parabola focus point.

ApexPt[3] = array of 3 doubles (X,Y,Z) describing the parabola apex point.

This set of data repeats for each parabola in the sketch. The size of the array is (NumParabolas \* 18).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.md)  
[ISketchBlockDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition_members.md)  
[ISketchBlockDefinition::GetParabolaCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetParabolaCount.md)  
[ISketchBlockDefinition::IGetParabolas Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~IGetParabolas.md)
