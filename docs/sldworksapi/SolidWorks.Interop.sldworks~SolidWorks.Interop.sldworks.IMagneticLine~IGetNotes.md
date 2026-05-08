# IGetNotes Method (IMagneticLine)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~IGetNotes`

Gets the notes attached to this magnetic line.
Gets the notes attached to this magnetic line.

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

Dim instance As IMagneticLine
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
:   Number of notes returned by this method (see **Remarks**)

#### Return Value

- In-process, unmanaged C++: Pointer to an array of [INote](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)s
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Call [IMagneticLine::GetNotesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~GetNotesCount.md) to get the value of Count.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMagneticLine Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine.md)  
[IMagneticLine Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine_members.md)  
[IMagneticLine::GetNotes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~GetNotes.md)  
[IMagneticLine::AddNote Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~AddNote.md)  
[IMagneticLine::RemoveNote Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~RemoveNote.md)
