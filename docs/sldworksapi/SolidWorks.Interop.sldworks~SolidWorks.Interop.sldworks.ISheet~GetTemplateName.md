# GetTemplateName Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetTemplateName`

Gets the name of the template used by this sheet.
Gets the name of the template used by this sheet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTemplateName() As System.String
```

```

Dim instance As ISheet
Dim value As System.String
 
value = instance.GetTemplateName()
```

```

System.string GetTemplateName()
```

```

System.String^ GetTemplateName(); 
```

#### Return Value

Template path name

Remarks

To ensure a correct return value, open the document in edit mode.

If the sheet does not use a template, i.e., uses a custom layout, this method returns "**\*.drt**".

Example

[Get Name of Drawing Sheet Template (VBA)](Get_Name_and_Properties_of_Drawing_Sheet_Template_Example_VB.htm)  
[Modify and Reload Sheet Format Template (C#)](Modify_and_Reload_Sheet_Format_Template_Example_CSharp.htm)  
[Modify and Reload Sheet Format Template (VB.NET)](Modify_and_Reload_Sheet_Format_Template_Example_VBNET.htm)  
[Modify and Reload Sheet Format Template (VBA)](Modify_and_Reload_Sheet_Format_Template_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.md)  
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.md)  
[ISheet::GetTemplateSketch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetTemplateSketch.md)  
[ISheet::SetTemplateName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetTemplateName.md)  
[ISheet::GetProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetProperties.md)  
[ISheet::IGetProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~IGetProperties.md)  
[ISheet::SetProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetProperties.md)
