# EditSheet2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~EditSheet2`

Puts the current drawing sheet in edit mode.
Puts the current drawing sheet in edit mode.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub EditSheet2() 
```

```

Dim instance As IDrawingDoc
 
instance.EditSheet2()
```

```

void EditSheet2()
```

```

void EditSheet2(); 
```

Remarks

The drawing sheet in edit mode ensures graphics updates and contains all subsequently created geometry.

You can use this method with [IDrawingDoc::EditSketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~EditSketch.md) or [IDrawingDoc::EditTemplate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~EditTemplate.md). Use [IDrawingDoc::GetEditSheet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetEditSheet.md) to determine the current state.

Example

[Place Note Behind Drawing Sheet (VBA)](Place_Note_Behind_Drawing_Sheet_Example_VB.htm)  
[Place Note Behind Drawing Sheet (VB.NET)](Place_Note_Behind_Drawing_Sheet_Example_VBNET.htm)  
[Place Note Behind Drawing Sheet (C#)](Place_Note_Behind_Drawing_Sheet_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.md)
