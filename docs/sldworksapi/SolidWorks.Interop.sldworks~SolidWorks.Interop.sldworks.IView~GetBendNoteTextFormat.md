# GetBendNoteTextFormat Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBendNoteTextFormat`

Gets the text format of all bend notes in this drawing view of a sheet metal part.
Gets the text format of all bend notes in this drawing view of a sheet metal part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetBendNoteTextFormat() As System.String
```

```

Dim instance As IView
Dim value As System.String
 
value = instance.GetBendNoteTextFormat()
```

```

System.string GetBendNoteTextFormat()
```

```

System.String^ GetBendNoteTextFormat(); 
```

#### Return Value

Format of all bend notes in this drawing view

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::SetBendNoteTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetBendNoteTextFormat.md)  
[IView::GetBendNoteAttributeString Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBendNoteAttributeString.md)  
[IView::ShowSheetMetalBendNotes Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ShowSheetMetalBendNotes.md)
