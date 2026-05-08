# SetColorRefAtIndex Method (ITriadManipulator)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator~SetColorRefAtIndex`

Sets the colors of the controls of a triad manipulator.
Sets the colors of the controls of a triad manipulator.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetColorRefAtIndex( _
   ByVal Index As System.Integer, _
   ByVal ColorRef As System.Integer _
) 
```

```

Dim instance As ITriadManipulator
Dim Index As System.Integer
Dim ColorRef As System.Integer
 
instance.SetColorRefAtIndex(Index, ColorRef)
```

```

void SetColorRefAtIndex( 
   System.int Index,
   System.int ColorRef
)
```

```

void SetColorRefAtIndex( 
   System.int Index,
   System.int ColorRef
) 
```

#### Parameters

*Index*
:   Control whose color to set as defined in [swTriadManipulatorControlPoints\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTriadManipulatorControlPoints_e.html)

*ColorRef*
:   COLORREF value

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITriadManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator.md)  
[ITriadManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator_members.md)
