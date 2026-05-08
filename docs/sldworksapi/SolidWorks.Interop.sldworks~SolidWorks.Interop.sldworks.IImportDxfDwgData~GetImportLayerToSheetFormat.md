# GetImportLayerToSheetFormat Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~GetImportLayerToSheetFormat`

Gets whether the specified visible layer is imported to the drawing sheet or sheet format.
Gets whether the specified visible layer is imported to the drawing sheet or sheet format.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetImportLayerToSheetFormat( _
   ByVal Layer As System.String _
) As System.Boolean
```

```

Dim instance As IImportDxfDwgData
Dim Layer As System.String
Dim value As System.Boolean
 
value = instance.GetImportLayerToSheetFormat(Layer)
```

```

System.bool GetImportLayerToSheetFormat( 
   System.string Layer
)
```

```

System.bool GetImportLayerToSheetFormat( 
   System.String^ Layer
) 
```

#### Parameters

*Layer*
:   Name of the layer

#### Return Value

True to import the specified visible layer to the sheet format, false to import it to the drawing sheet

Remarks

This method only supports importing to a drawing; it does not support importing to a part sketch.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IImportDxfDwgData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData.md)  
[IImportDxfDwgData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData_members.md)  
[IImportDxfDwgData::GetImportLayerVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~GetImportLayerVisibility.md)  
[IImportDxfDwgData::SetImportLayerToSheetFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~SetImportLayerToSheetFormat.md)  
[IImportDxfDwgData::SetImportLayerVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~SetImportLayerVisibility.md)  
[IImportDxfDwgData::ImportMethod Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~ImportMethod.md)
