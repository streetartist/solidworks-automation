# ReloadTemplate Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~ReloadTemplate`

Reloads the sheet format from the original sheet format template.
Reloads the sheet format from the original sheet format template.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ReloadTemplate( _
   ByVal KeepNoteChanges As System.Boolean _
) As System.Integer
```

```

Dim instance As ISheet
Dim KeepNoteChanges As System.Boolean
Dim value As System.Integer
 
value = instance.ReloadTemplate(KeepNoteChanges)
```

```

System.int ReloadTemplate( 
   System.bool KeepNoteChanges
)
```

```

System.int ReloadTemplate( 
   System.bool KeepNoteChanges
) 
```

#### Parameters

*KeepNoteChanges*
:   True to keep note modifications made to the sheet format and reload all other elements from the original sheet format template, false to reload all elements from the original sheet format template and discard any note modifications made to the sheet format

#### Return Value

Status as defined in [swReloadTemplateResult\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swReloadTemplateResult_e.html)

Remarks

If new notes are added or existing notes modified or deleted on the sheet format, then specifying true for KeepNoteChanges:

- adds the new notes to the sheet format template, but does not duplicate the new notes on the sheet format.
- restores any deleted notes from the sheet format template on the sheet format.
- duplicates all other notes in their original position from the sheet format template on the sheet format.

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
[ISheet::SaveFormat Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SaveFormat.md)
