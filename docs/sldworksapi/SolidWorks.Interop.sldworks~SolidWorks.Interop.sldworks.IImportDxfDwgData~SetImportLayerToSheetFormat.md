# SetImportLayerToSheetFormat Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~SetImportLayerToSheetFormat`

Sets whether the specified visible layers are imported to the sheet format or drawing sheet.
Sets whether the specified visible layers are imported to the sheet format or drawing sheet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetImportLayerToSheetFormat( _
   ByVal Layers As System.Object, _
   ByVal SheetFormat As System.Boolean _
) As System.Boolean
```

```

Dim instance As IImportDxfDwgData
Dim Layers As System.Object
Dim SheetFormat As System.Boolean
Dim value As System.Boolean
 
value = instance.SetImportLayerToSheetFormat(Layers, SheetFormat)
```

```

System.bool SetImportLayerToSheetFormat( 
   System.object Layers,
   System.bool SheetFormat
)
```

```

System.bool SetImportLayerToSheetFormat( 
   System.Object^ Layers,
   System.bool SheetFormat
) 
```

#### Parameters

*Layers*
:   Array of strings of the names of the layers (see **Remarks**)

*SheetFormat*
:   True to import the specified visible layers to the sheet format, false to import them to the drawing sheet

#### Return Value

True of importing the specified visible  layers was successful, false if not

Remarks

This method only supports importing to a drawing; it does not support importing to a part sketch.

The Layers argument can contain either a string or an array of strings, where the strings are the layer names with which to work. You can also specify the argument as empty, which indicates all layers. If this method is not used, the default behavior is to import all layers to the drawing sheet.  

The import to sheet or sheet format Boolean is the same for all sheets that are imported; you cannot specify it on a sheet-by-sheet basis.

#### Visual Basic for Applications (VBA) Example

To import all layers on all sheets to drawings sheets in SOLIDWORKS (this is the default behavior):

boolstatus = ImportDxfDwgData.SetImportLayerToSheetFormat (emptyVariant, false)

To import layers "A" and "B" to the drawing sheet and the remaining layers to the sheet format:

boolstatus = ImportDxfDwgData.SetImportLayerToSheetFormat (emptyVariant, True)

layerName(0) = "A"

layerName(1) = "B"

layerVariant = layerName

boolstatus = ImportDxfDwgData.SetImportLayerToSheetFormat ((layerVariant), false)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IImportDxfDwgData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData.md)  
[IImportDxfDwgData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData_members.md)  
[IImportDxfDwgData::GetImportLayerToSheetFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~GetImportLayerToSheetFormat.md)  
[IImportDxfDwgData::GetImportLayerVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~GetImportLayerVisibility.md)  
[IImportDxfDwgData::SetImportLayerVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~SetImportLayerVisibility.md)  
[IImportDxfDwgData::ImportMethod Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~ImportMethod.md)
