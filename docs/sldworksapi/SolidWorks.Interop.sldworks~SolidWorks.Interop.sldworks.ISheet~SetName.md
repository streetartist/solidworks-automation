# SetName Method (ISheet)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetName`

Sets the sheet name.
Sets the sheet name.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetName( _
   ByVal NameIn As System.String _
) 
```

```

Dim instance As ISheet
Dim NameIn As System.String
 
instance.SetName(NameIn)
```

```

void SetName( 
   System.string NameIn
)
```

```

void SetName( 
   System.String^ NameIn
) 
```

#### Parameters

*NameIn*
:   Name for the sheet

Example

[Get ID of Active Configuration or Current Drawing Sheet (VB.NET)](Get_ID_of_Active_Configuration_or_Current_Drawing_Sheet_Example_VBNET.htm)  
[Get ID of Active Configuration or Current Drawing Sheet (VBA)](Get_ID_of_Active_Configuration_or_Current_Drawing_Sheet_Example_VB.htm)  
[Get ID of Active Configuration or Current Drawing Sheet (C#)](Get_ID_of_Active_Configuration_or_Current_Drawing_Sheet_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.md)  
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.md)  
[ISheet::GetName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetName.md)  
[ISheet::GetSheetFormatName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetSheetFormatName.md)  
[ISheet::GetTemplateName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetTemplateName.md)  
[ISheet::SetSheetFormatName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetSheetFormatName.md)  
[ISheet::SetTemplateName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetTemplateName.md)
