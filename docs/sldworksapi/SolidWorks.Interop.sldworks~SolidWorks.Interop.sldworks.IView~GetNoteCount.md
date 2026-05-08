# GetNoteCount Method (IView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetNoteCount`

Gets the number notes in this drawing view.
Gets the number notes in this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetNoteCount() As System.Integer
```

```

Dim instance As IView
Dim value As System.Integer
 
value = instance.GetNoteCount()
```

```

System.int GetNoteCount()
```

```

System.int GetNoteCount(); 
```

#### Return Value

Number of notes in this drawing view

Remarks

Call this method before calling [IView::IGetNotes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetNotes.md) to determine the size of the array for that method.

Example

[Get Views and Notes (VBA)](Get_Views_and_Notes_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetNotes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetNotes.md)  
[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)
