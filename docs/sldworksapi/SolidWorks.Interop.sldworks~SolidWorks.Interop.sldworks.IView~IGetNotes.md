# IGetNotes Method (IView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetNotes`

Gets the notes in this drawing view.
Gets the notes in this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetNotes( _
   ByVal NumberOfNotes As System.Integer _
) As Note
```

```

Dim instance As IView
Dim NumberOfNotes As System.Integer
Dim value As Note
 
value = instance.IGetNotes(NumberOfNotes)
```

```

Note IGetNotes( 
   System.int NumberOfNotes
)
```

```

Note^ IGetNotes( 
   System.int NumberOfNotes
) 
```

#### Parameters

*NumberOfNotes*
:   Number of notes in this drawing view

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [notes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_methods.htm) for details about this type of method.

Remarks

Use this method to obtain the array of notes all at once instead of calling [IView::GetFirstNote](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstNote.md) and then repeatedly calling [INote::GetNext](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetNext.md) to obtain the remaining notes on this drawing view.

Call [IView::GetNoteCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetNoteCount.md) before calling this method to get NumberOfNotes.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetNotes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetNotes.md)
