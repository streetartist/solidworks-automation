# SetConcentricAlignmentType Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~SetConcentricAlignmentType`

Sets the alignment type of this mate.
Sets the alignment type of this mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetConcentricAlignmentType( _
   ByVal PositionType As System.Integer _
) 
```

```

Dim instance As IMate2
Dim PositionType As System.Integer
 
instance.SetConcentricAlignmentType(PositionType)
```

```

void SetConcentricAlignmentType( 
   System.int PositionType
)
```

```

void SetConcentricAlignmentType( 
   System.int PositionType
) 
```

#### Parameters

*PositionType*
:   Alignment type as defined in [swConcentricAlignmentType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swConcentricAlignmentType_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.md)  
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.md)  
[IMate2::GetConcentricAlignmentType Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetConcentricAlignmentType.md)
