# GetNotes Method (IView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetNotes`

Gets the notes in this drawing view.
Gets the notes in this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetNotes() As System.Object
```

```

Dim instance As IView
Dim value As System.Object
 
value = instance.GetNotes()
```

```

System.object GetNotes()
```

```

System.Object^ GetNotes(); 
```

#### Return Value

Array of [notes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)

Remarks

Use this method to obtain the array of notes all at once instead of calling [IView::GetFirstNote](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstNote.md) and then repeatedly calling [INote::GetNext](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetNext.md) to obtain the remaining notes on this drawing view.

Example

[Get Views and Notes (VBA)](Get_Views_and_Notes_Example_VB.htm)  
[Get Notes from New or Existing Title Block (VBA)](Get_Notes_from_New_or_Existing_Title_Block_Example_VB.htm)  
[Get Notes from New or Existing Title Block (VB.NET)](Get_Notes_from_New_or_Existing_Title_Block_Example_VBNET.htm)  
[Get Notes from New or Existing Title Block (C#)](Get_Notes_from_New_or_Existing_Title_Block_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetNoteCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetNoteCount.md)  
[IView::IGetNotes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetNotes.md)
