# GetEditSheet Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetEditSheet`

Gets whether the current drawing is in edit sheet mode or edit template mode.
Gets whether the current drawing is in edit sheet mode or edit template mode.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetEditSheet() As System.Boolean
```

```

Dim instance As IDrawingDoc
Dim value As System.Boolean
 
value = instance.GetEditSheet()
```

```

System.bool GetEditSheet()
```

```

System.bool GetEditSheet(); 
```

#### Return Value

True for edit sheet mode, false for edit template mode

Remarks

Use:

- [IDrawingDoc::EditSheet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~EditSheet.md) to set the drawing to be editing the sheet.
- [IDrawingDoc::EditTemplate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~EditTemplate.md) to set the drawing to be editing the template.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDrawingDoc::EditSketch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~EditSketch.md)
