# GetNoteCount Method (ITitleBlock)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlock~GetNoteCount`

Gets the number of notes in this title block.
Gets the number of notes in this title block.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetNoteCount() As System.Integer
```

```

Dim instance As ITitleBlock
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

Number of notes in this title block

Remarks

Call this method before calling [ITitleBlock::IGetNotes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlock~IGetNotes.md) to get the size of the array for that method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITitleBlock Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlock.md)  
[ITitleBlock Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlock_members.md)  
[ITitleBlock::GetNotes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlock~GetNotes.md)
