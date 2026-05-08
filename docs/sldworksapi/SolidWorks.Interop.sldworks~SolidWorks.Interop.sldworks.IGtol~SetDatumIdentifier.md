# SetDatumIdentifier Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetDatumIdentifier`

Sets the name of the datum being defined.
Sets the name of the datum being defined.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetDatumIdentifier( _
   ByVal DatumIdentifier As System.String _
) 
```

```

Dim instance As IGtol
Dim DatumIdentifier As System.String
 
instance.SetDatumIdentifier(DatumIdentifier)
```

```

void SetDatumIdentifier( 
   System.string DatumIdentifier
)
```

```

void SetDatumIdentifier( 
   System.String^ DatumIdentifier
) 
```

#### Parameters

*DatumIdentifier*
:   Name of datum

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md)  
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.md)  
[IGtol::GetDatumIdentifier Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetDatumIdentifier.md)
