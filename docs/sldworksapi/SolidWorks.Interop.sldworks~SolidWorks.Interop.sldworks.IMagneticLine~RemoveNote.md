# RemoveNote Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~RemoveNote`

Detaches the specified note from this magnetic line and moves it to the specified location.
Detaches the specified note from this magnetic line and moves it to the specified location.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function RemoveNote( _
   ByVal Note As Note, _
   ByVal Location As MathPoint _
) As System.Boolean
```

```

Dim instance As IMagneticLine
Dim Note As Note
Dim Location As MathPoint
Dim value As System.Boolean
 
value = instance.RemoveNote(Note, Location)
```

```

System.bool RemoveNote( 
   Note Note,
   MathPoint Location
)
```

```

System.bool RemoveNote( 
   Note^ Note,
   MathPoint^ Location
) 
```

#### Parameters

*Note*
:   [INote](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md) to detach from this magnetic line

*Location*
:   [IMathPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md) where to move the note specified by Note

#### Return Value

True if successful, false if not

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
[IMagneticLine::AddNote Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~AddNote.md)  
[IMagneticLine::GetNotes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~GetNotes.md)  
[IMagneticLine::IGetNotes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~IGetNotes.md)
