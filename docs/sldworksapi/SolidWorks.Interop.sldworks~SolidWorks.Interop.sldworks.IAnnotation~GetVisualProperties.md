# GetVisualProperties Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetVisualProperties`

Gets the visual properties of this annotation.
Gets the visual properties of this annotation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetVisualProperties() As System.Object
```

```

Dim instance As IAnnotation
Dim value As System.Object
 
value = instance.GetVisualProperties()
```

```

System.object GetVisualProperties()
```

```

System.Object^ GetVisualProperties(); 
```

#### Return Value

Array of five longs or five integers (see [Long vs. Integer](sldworksapiprogguide.chm::/overview/Long_vs_Integer.htm) and see **Remarks**)

Remarks

The return value is the following array:

> [*color, style, width, layerID, layerOverride* ]

where:

|  |  |
| --- | --- |
| *color* | COLORREF returned as an integer. Return value can be 0 or -1 for default color. |
| *style* | Line style as defined in [swLineStyles\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineStyles_e.html). |
| *width* | Line width as defined in [swLineWeights\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineWeights_e.html). |
| *layerID* | Integer value indicating which layer holds this entity. The Layer object can be obtained  by passing this integer value to [ILayerMgr::GetLayerById](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~GetLayerById.md) or [ILayerMgr::IGetLayerById](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~IGetLayerById.md). |
| *layerOverride* | Integer with bit flags set to determine which properties, if any, have been overridden  with respect to the layer default properties. If the bit value is set, then the specific  property or properties have been overridden. The bit indicators are: color = 0x1,  style = 0x2, and width = 0x4. Therefore, if *layerOverride* was returned as 3, we know  the color and style have been specifically set for this annotation and might not  match the default values associated with this annotations layer. |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)  
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.md)  
[IAnnotation::IGetVisualProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~IGetVisualProperties.md)
