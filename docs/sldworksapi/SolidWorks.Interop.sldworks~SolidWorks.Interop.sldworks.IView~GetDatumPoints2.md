# GetDatumPoints2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDatumPoints2`

Gets all of the information about all the datum points in this view.
Gets all of the information about all the datum points in this view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDatumPoints2() As System.Object
```

```

Dim instance As IView
Dim value As System.Object
 
value = instance.GetDatumPoints2()
```

```

System.object GetDatumPoints2()
```

```

System.Object^ GetDatumPoints2(); 
```

#### Return Value

Array of doubles (see **Remarks**)

Remarks

Return value is an array of doubles with the format:

[ Color, LineStyleIndex, LineWidth, LayerID, LayerOverride, ptLoc[3] ... ]

Color = COLORREF returned as an integer. Return value can be 0 or -1 for default color.

LineStyleIndex = line style. Valid line styles as defined in [swLineStyles\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html).

LineWidth = integer value defining the line width. Valid width values as defined in [swLineWeights\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineWeights_e.html).

LayerID = integer value indicating which layer holds this entity. This integer value is the array index value into the layerList array. The layerList array can be obtained using [ILayerMgr::GetLayerList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~GetLayerList.md) or [ILayerMgr::IGetLayerList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~IGetLayerList.md). A value of 1 indicates that this item is not on a layer.

LayerOverride = integer with bit flags set to determine which properties, if any, have been overridden with respect to the [ILayer](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer.md) default properties. If the bit value is set, then the specific property or properties have been overridden. The bit indicators are: color = 0x1, style = 0x2, and width = 0x4. Therefore, if LayerOverride is returned as 3, you know the color and style have been specifically set for this item and may not match the default values associated with this item's layer.

ptLoc[3] = array of 3 doubles (X,Y,Z) describing the point location

...

This entire set of data repeats for each datum point in the view. The size of the array is (NumPts \* 8). To determine the number of points,use [IView::GetDatumPointsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDatumPointsCount.md).

The data returned from this method is in terms of view space. If you want the data in terms of sheet space (for example, the 0,0 origin being the lower-left corner of the sheet), then combine this data with the three return values from [IView::GetXForm](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetXform.md) or [IView::IGetXForm](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetXform.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::IGetDatumPoints2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDatumPoints2.md)
