# AddNote Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~AddNote`

Attaches to this magnetic line the specified note at the specified position.
Attaches to this magnetic line the specified note at the specified position.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddNote( _
   ByVal Note As Note, _
   ByVal Position As System.Double _
) As System.Boolean
```

```

Dim instance As IMagneticLine
Dim Note As Note
Dim Position As System.Double
Dim value As System.Boolean
 
value = instance.AddNote(Note, Position)
```

```

System.bool AddNote( 
   Note Note,
   System.double Position
)
```

```

System.bool AddNote( 
   Note^ Note,
   System.double Position
) 
```

#### Parameters

*Note*
:   [INote](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md) to attach to this magnetic line

*Position*
:   0.0 <= Attachment position on magnetic line <= 1.0; valid only if [IMagneticLine::EqualSpacing](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~EqualSpacing.md) is false

#### Return Value

True if successful, false if not (see **Remarks**)

Remarks

All notes attached to a magnetic line must be from the same view.

Example

[Insert Magnetic Line (C#)](Insert_Magnetic_Line_Example_CSharp.htm)  
[Insert Magnetic Line (VB.NET)](Insert_Magnetic_Line_Example_VBNET.htm)  
[Insert Magnetic Line (VBA)](Insert_Magnetic_Line_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMagneticLine Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine.md)  
[IMagneticLine Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine_members.md)  
[IMagneticLine::RemoveNote Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~RemoveNote.md)  
[IMagneticLine::GetNotes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~GetNotes.md)  
[IMagneticLine::IGetNotes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~IGetNotes.md)
