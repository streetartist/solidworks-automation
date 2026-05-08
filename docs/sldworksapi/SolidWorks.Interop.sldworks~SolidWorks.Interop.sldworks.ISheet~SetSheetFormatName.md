# SetSheetFormatName Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetSheetFormatName`

Sets the name of the sheet format of this drawing sheet, as displayed in the FeatureManager design tree.
Sets the name of the sheet format of this drawing sheet, as displayed in the FeatureManager design tree.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetSheetFormatName( _
   ByVal Name As System.String _
) As System.Boolean
```

```

Dim instance As ISheet
Dim Name As System.String
Dim value As System.Boolean
 
value = instance.SetSheetFormatName(Name)
```

```

System.bool SetSheetFormatName( 
   System.string Name
)
```

```

System.bool SetSheetFormatName( 
   System.String^ Name
) 
```

#### Parameters

*Name*
:   Name of the sheet format

#### Return Value

True if the name of the sheet format is set, false if not

Remarks

The name that you specify must:

- be unique in the FeatureManager design tree.
- Not contain any of the SOLIDWORKS reserved special characters.

If either of these conditions is not met, then this method returns false, and the name is not changed. If this sheet does not have a sheet format, this method has no effect.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.md)  
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.md)  
[ISheet::GetName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetName.md)  
[ISheet::GetSheetFormatName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetSheetFormatName.md)  
[ISheet::GetTemplateName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetTemplateName.md)  
[ISheet::SetName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetName.md)  
[ISheet::SetTemplateName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetTemplateName.md)  
[ISheet::SheetFormatVisible Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SheetFormatVisible.md)
