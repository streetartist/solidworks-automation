# SaveFormat Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SaveFormat`

Saves the sheet format in the specified file.
Saves the sheet format in the specified file.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SaveFormat( _
   ByVal FileName As System.String _
) As System.Boolean
```

```

Dim instance As ISheet
Dim FileName As System.String
Dim value As System.Boolean
 
value = instance.SaveFormat(FileName)
```

```

System.bool SaveFormat( 
   System.string FileName
)
```

```

System.bool SaveFormat( 
   System.String^ FileName
) 
```

#### Parameters

*FileName*
:   Path and file name to which to save the sheet format (see Remarks)

#### Return Value

True if the sheet format is saved to the specified file, false if not

Remarks

You must specify the path, file name, and filename extension to which to save the sheet format. Use .slddrt for the filename extension.

Before calling this method, use [IDrawingDoc::ActivateSheet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ActivateSheet.md) to make the sheet active.

Example

[Modify and Reload Sheet Format Template (C#)](Modify_and_Reload_Sheet_Format_Template_Example_CSharp.htm)  
[Modify and Reload Sheet Format Template (VB.NET)](Modify_and_Reload_Sheet_Format_Template_Example_VBNET.htm)  
[Modify and Reload Sheet Format Template (VBA)](Modify_and_Reload_Sheet_Format_Template_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.md)  
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.md)  
[IDrawingDoc::EditTemplate Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~EditTemplate.md)  
[ISheet::ReloadTemplate Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~ReloadTemplate.md)
