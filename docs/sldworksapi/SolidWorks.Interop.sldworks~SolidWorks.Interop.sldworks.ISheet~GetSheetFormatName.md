# GetSheetFormatName Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetSheetFormatName`

Gets the name of the sheet format of this drawing sheet, as displayed in the FeatureManager design tree.
Gets the name of the sheet format of this drawing sheet, as displayed in the FeatureManager design tree.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSheetFormatName() As System.String
```

```

Dim instance As ISheet
Dim value As System.String
 
value = instance.GetSheetFormatName()
```

```

System.string GetSheetFormatName()
```

```

System.String^ GetSheetFormatName(); 
```

#### Return Value

Name of the sheet format

Remarks

If the sheet does not have a sheet format, an empty string is returned.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.md)  
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.md)  
[ISheet::GetName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetName.md)  
[ISheet::SetName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetName.md)  
[ISheet::SetSheetFormatName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetSheetFormatName.md)  
[ISheet::GetTemplateName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetTemplateName.md)  
[ISheet::SetTemplateName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetTemplateName.md)  
[ISheet::SheetFormatVisible Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SheetFormatVisible.md)
