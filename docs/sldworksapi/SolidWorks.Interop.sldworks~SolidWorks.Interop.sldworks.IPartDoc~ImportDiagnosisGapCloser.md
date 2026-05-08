# ImportDiagnosisGapCloser Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ImportDiagnosisGapCloser`

Allows you to repair a gap by moving the vertices on the edges surrounding the gap to new positions to close the gap on the imported model.
Allows you to repair a gap by moving the vertices on the edges surrounding the gap to new positions to close the gap on the imported model.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ImportDiagnosisGapCloser( _
   ByVal OldX As System.Double, _
   ByVal OldY As System.Double, _
   ByVal OldZ As System.Double, _
   ByVal NewX As System.Double, _
   ByVal NewY As System.Double, _
   ByVal NewZ As System.Double, _
   ByVal LastMove As System.Boolean _
) 
```

```

Dim instance As IPartDoc
Dim OldX As System.Double
Dim OldY As System.Double
Dim OldZ As System.Double
Dim NewX As System.Double
Dim NewY As System.Double
Dim NewZ As System.Double
Dim LastMove As System.Boolean
 
instance.ImportDiagnosisGapCloser(OldX, OldY, OldZ, NewX, NewY, NewZ, LastMove)
```

```

void ImportDiagnosisGapCloser( 
   System.double OldX,
   System.double OldY,
   System.double OldZ,
   System.double NewX,
   System.double NewY,
   System.double NewZ,
   System.bool LastMove
)
```

```

void ImportDiagnosisGapCloser( 
   System.double OldX,
   System.double OldY,
   System.double OldZ,
   System.double NewX,
   System.double NewY,
   System.double NewZ,
   System.bool LastMove
) 
```

#### Parameters

*OldX*
:   x coordinate of vertex to move

*OldY*
:   y coordinate of vertex to move

*OldZ*
:   z coordinate of vertex to move

*NewX*
:   x coordinate where to move the vertex

*NewY*
:   y coordinate where to move the vertex

*NewZ*
:   z coordinate where to move the vertex

*LastMove*
:   True if this move is the last move in a series of moves to close the gap, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)  
[IPartDoc::ImportDiagnosis Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ImportDiagnosis.md)  
[IBody2::Diagnose Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Diagnose.md)  
[IDiagnoseResult Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDiagnoseResult.md)
