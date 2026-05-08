# SetImportLayerVisibility Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~SetImportLayerVisibility`

Sets whether the specified layers are imported hidden or visible.
Sets whether the specified layers are imported hidden or visible.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetImportLayerVisibility( _
   ByVal Layers As System.Object, _
   ByVal Visibility As System.Integer _
) As System.Boolean
```

```

Dim instance As IImportDxfDwgData
Dim Layers As System.Object
Dim Visibility As System.Integer
Dim value As System.Boolean
 
value = instance.SetImportLayerVisibility(Layers, Visibility)
```

```

System.bool SetImportLayerVisibility( 
   System.object Layers,
   System.int Visibility
)
```

```

System.bool SetImportLayerVisibility( 
   System.Object^ Layers,
   System.int Visibility
) 
```

#### Parameters

*Layers*
:   Array of strings of the names of the layers (see **Remarks**)

*Visibility*
:   Visibility of the layers as defined in [swImportDxfDwg\_LayerVisibility\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swImportDxfDwg_LayerVisibility_e.html)

#### Return Value

True if setting the visibility of these layers is successful, false if not

Remarks

This method only supports importing to a drawing; it does not support importing to a part sketch.

The Layers argument can contain either a string or an array of strings, where the strings are the layer names with which to work. You can also specify the argument as empty, which indicates all layers. If this method is not used, the default behavior is to import all layers with the same visibility as they have in the DXF/DWG file.  

The layer visibility is the same for all sheets that are imported; you cannot specify the layer visibility on a sheet-by-sheet basis.

Hidden layers are always imported to the drawing sheet.

You should first specify the behavior that applies to all layers, using an empty VARIANT, because this overrides any information you have previously entered for specific layers. Then, you should use this method with layer names in the VARIANT, to override that default behavior on a layer-by-layer basis.

#### Visual Basic for Applications (VBA) Example

To import all layers with the same visibility as in the DXF/DWG file (this is the default behavior):

boolstatus = ImportDxfDwgData.SetImportLayerVisibility (emptyVariant, swImportDxfDwg\_LayerMaintain)

To import layer "A" hidden and the remaining layers visible:

boolstatus = ImportDxfDwgData.SetImportLayerVisibility (emptyVariant, swImportDxfDwg\_LayerVisible)

layerName = "A"

layerVariant = layerName

boolstatus = ImportDxfDwgData.SetImportLayerVisibility ((layerVariant), swImportDxfDwg\_LayerHidden)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IImportDxfDwgData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData.md)  
[IImportDxfDwgData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData_members.md)  
[IImportDxfDwgData::GetImportLayerToSheetFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~GetImportLayerToSheetFormat.md)  
[IImportDxfDwgData::GetImportLayerVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~GetImportLayerVisibility.md)  
[IImportDxfDwgData::SetImportLayerToSheetFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~SetImportLayerToSheetFormat.md)  
[IImportDxfDwgData::ImportMethod Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~ImportMethod.md)
