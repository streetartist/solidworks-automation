# SetName Method (INote)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetName`

Sets the name for this note.
Sets the name for this note.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetName( _
   ByVal NameIn As System.String _
) As System.Boolean
```

```

Dim instance As INote
Dim NameIn As System.String
Dim value As System.Boolean
 
value = instance.SetName(NameIn)
```

```

System.bool SetName( 
   System.string NameIn
)
```

```

System.bool SetName( 
   System.String^ NameIn
) 
```

#### Parameters

*NameIn*
:   Note name

#### Return Value

True if the note name is changed successfully, false if not

Example

[Set Note Name (VBA)](Set_Note_Name_Example.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)  
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.md)  
[INote::GetName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetName.md)
