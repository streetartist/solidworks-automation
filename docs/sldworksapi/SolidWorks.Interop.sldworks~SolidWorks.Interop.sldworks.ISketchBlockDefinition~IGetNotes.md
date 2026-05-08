# IGetNotes Method (ISketchBlockDefinition)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~IGetNotes`

Gets the notes in this block definition.
Gets the notes in this block definition.

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

Dim instance As ISketchBlockDefinition
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
:   Number of notes

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [notes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Call [ISketchBlockDefinition::GetNoteCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetNoteCount.md) before calling this method to get the value for Count.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.md)  
[ISketchBlockDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition_members.md)  
[ISketchBlockDefinition::GetNotes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetNotes.md)
