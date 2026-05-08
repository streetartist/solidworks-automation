# GetArcs Method (ISketchBlockDefinition)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetArcs`

Gets information about all of the arcs in the block definition.
Gets information about all of the arcs in the block definition.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetArcs() As System.Object
```

```

Dim instance As ISketchBlockDefinition
Dim value As System.Object
 
value = instance.GetArcs()
```

```

System.object GetArcs()
```

```

System.Object^ GetArcs(); 
```

#### Return Value

Array containing an array of doubles (see **Remarks**)

Remarks

Return value is an array of doubles with the format:

[ Color, Type, Line Font, Line Width, Layer ID, Layer Override, [Start], [End], [Center] Rotation Dir ]

where

- Color - COLORREF returned as an integer. Return value could be 0 or -1 for default color.
- Type - Line type. Valid returns as defined in [swLineTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html). A LineType is a combination of a line style and line weight.
- Line Font - Line style. Valid line styles as defined in [swLineStyles\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineStyles_e.html) enumeration.
- Line Width - Integer value defining the line width. Valid width values as defined in [swLineWeights\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineWeights_e.html).
- Layer ID - Integer value indicating which layer holds this entity. The [ILayer](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer.md) object can be obtained by passing this integer value to [ILayerMgr::GetLayerById](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~GetLayerById.md) or [ILayerMgr::IGetLayerID](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~IGetLayerById.md).
- Layer Override - Integer with bit flags set to determine which properties, if any, have been overridden with respect to the Layer default properties. If the bit value is set, then the specific property or properties have been overridden. The bit indicators are: color = 0x1, style = 0x2, and width = 0x4. Therefore, if LayerOverride was returned as 3, the color and style have been specifically set for this item and may not match the default values associated with this item's layer.
- Start[3] - An array of 3 doubles (X,Y,Z) describing the start point.
- End[3] - An array of 3 doubles (X,Y,Z) describing the end point. If the arc is closed, then End[3] is the same point as Start.
- Center[3] - An array of 3 doubles (X,Y,Z) describing the center point.
- Rotation Dir - Rotational direction (CW = -1, CCW = 1)

This set of data repeats for each arc in the sketch. The size of the array is (NumArcs \* 16).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.md)  
[ISketchBlockDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition_members.md)  
[ISketchBlockDefinition::IGetArcs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~IGetArcs.md)  
[ISketchBlockDefinition::GetArcCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetArcCount.md)
