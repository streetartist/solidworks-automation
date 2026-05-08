# GetUserPoints2 Method (ISketch)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetUserPoints2`

Gets all of the user points in this sketch.
Gets all of the user points in this sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetUserPoints2() As System.Object
```

```

Dim instance As ISketch
Dim value As System.Object
 
value = instance.GetUserPoints2()
```

```

System.object GetUserPoints2()
```

```

System.Object^ GetUserPoints2(); 
```

#### Return Value

Array of doubles (see **Remarks**)

Remarks

The return value is an array of doubles with this format:

[ Color, Line Font, Line Width, Layer ID, Layer Override, ptLoc[3] ]

where:

- Color = COLORREF returned as an integer. Return value could be 0 or -1 for default color.
- Line Font = line style. Valid line styles can be found in the [swLineStyles\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineStyles_e.html) enumeration.
- Line Width = integer value defining the line width. Valid width values can be found in the [swLineWeights\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineWeights_e.html) enumeration.
- Layer ID = integer value indicating which layer holds this entity. The [ILayer](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer.md) object can be obtained by passing this integer value to [ILayerMgr::GetLayerById](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~GetLayerById.md) or [ILayerMgr::IGetLayerById](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~IGetLayerById.md).
- Layer Override = integer with bit flags set to determine which properties, if any, have been overridden with respect to the Layer default properties. If the bit value is set, then the specific property or properties have been overridden. The bit indicators are: color = 0x1, style = 0x2, and width = 0x4. Therefore, if LayerOverride was returned as 3, you know the color and style have been specifically set for this item and may not match the default values associated with this item's layer.
- ptLoc[3] = an array of doubles (x, y, z) describing the point location

This set of data repeats for each user point in the sketch. The size of the array is (NumPts \* 8). To determine the number of points in the sketch, use [ISketch::GetUserPointsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetUserPointsCount.md).

See [ISketch::GetSketchPoints2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchPoints2.md), [ISketch::IGetSketchPoints2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSketchPoints2.md), or [ISketch::IEnumSketchPoints](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IEnumSketchPoints.md) for access to individual [ISketchPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md) objects.

Example

[Get Sketch Points and Their Persistent IDs (VBA)](Get_Sketch_Points_and_Their_Persistent_IDs_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)  
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.md)  
[ISketch::IGetUserPoints2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetUserPoints2.md)
