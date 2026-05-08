# SetTemplateName Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetTemplateName`

Sets the template name for the sheet format.
Sets the template name for the sheet format.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetTemplateName( _
   ByVal NameIn As System.String _
) 
```

```

Dim instance As ISheet
Dim NameIn As System.String
 
instance.SetTemplateName(NameIn)
```

```

void SetTemplateName( 
   System.string NameIn
)
```

```

void SetTemplateName( 
   System.String^ NameIn
) 
```

#### Parameters

*NameIn*
:   Path name of the sheet format template

Remarks

If you want to use:

- a custom template name, before calling this method, call [ISheet::SetProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetProperties.md) and specify swDwgTemplates\_e.swDwgTemplateCustom for the Templ parameter.
- one of the standard templates provided by SOLIDWORKS, then there is no need to call ISheet::SetTemplateName. Instead, call ISheet::SetProperties and specify the appropriate enumerator for the Templ parameter.

Example

[Get and Set Whether to Hide Cutting Line Shoulders (C#)](Get_and_Set_Whether_to_Hide_Cutting_Line_Shoulders_Example_CSharp.htm)  
[Get and Set Whether to Hide Cutting Line Shoulders (VB.NET)](Get_and_Set_Whether_to_Hide_Cutting_Line_Shoulders_Example_VBNET.htm)  
[Get and Set Whether to Hide Cutting Line Shoulders (VBA)](Get_and_Set_Whether_to_Hide_Cutting_Line_Shoulders_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.md)  
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.md)  
[ISheet::GetTemplateName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetTemplateName.md)  
[ISheet::GetTemplateSketch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetTemplateSketch.md)  
[ISheet::GetProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetProperties.md)  
[ISheet::IGetProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~IGetProperties.md)
