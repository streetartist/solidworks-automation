# IGetNotes Method (ITitleBlock)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlock~IGetNotes`

Gets the notes in this title block.
Gets the notes in this title block.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetNotes( _
   ByVal Count As System.Integer _
) As Note
```

```

Dim instance As ITitleBlock
Dim Count As System.Integer
Dim value As Note
 
value = instance.IGetNotes(Count)
```

```

Note IGetNotes( 
   System.int Count
)
```

```

Note^ IGetNotes( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of notes in this title block

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [notes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md) in this title block

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Call [ITitleBlock::GetNoteCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlock~GetNoteCount.md) before calling this method to get Count.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITitleBlock Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlock.md)  
[ITitleBlock Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlock_members.md)
