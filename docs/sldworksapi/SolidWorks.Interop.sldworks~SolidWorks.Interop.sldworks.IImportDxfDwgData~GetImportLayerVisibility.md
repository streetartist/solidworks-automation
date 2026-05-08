# GetImportLayerVisibility Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~GetImportLayerVisibility`

Gets whether the specified layer is imported hidden or visible.
Gets whether the specified layer is imported hidden or visible.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetImportLayerVisibility( _
   ByVal Layer As System.String _
) As System.Integer
```

```

Dim instance As IImportDxfDwgData
Dim Layer As System.String
Dim value As System.Integer
 
value = instance.GetImportLayerVisibility(Layer)
```

```

System.int GetImportLayerVisibility( 
   System.string Layer
)
```

```

System.int GetImportLayerVisibility( 
   System.String^ Layer
) 
```

#### Parameters

*Layer*
:   Name of the layer

#### Return Value

Visibility state as defined in [swImportDxfDwg\_LayerVisibility\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swImportDxfDwg_LayerVisibility_e.html)

Remarks

This method only supports importing to a drawing; it does not support importing to a part sketch.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IImportDxfDwgData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData.md)  
[IImportDxfDwgData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData_members.md)  
[IImportDxfDwgData::GetImportLayerToSheetFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~GetImportLayerToSheetFormat.md)  
[IImportDxfDwgData::SetImportLayerToSheetFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~SetImportLayerToSheetFormat.md)  
[IImportDxfDwgData::SetImportLayerVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~SetImportLayerVisibility.md)  
[IImportDxfDwgData::ImportMethod Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~ImportMethod.md)
