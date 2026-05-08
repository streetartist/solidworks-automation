# UpdateScale Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator~UpdateScale`

Sets scale for the triad manipulator's x,y,z axes.
Sets scale for the triad manipulator's x,y,z axes.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub UpdateScale( _
   ByVal Scale As System.Double _
) 
```

```

Dim instance As ITriadManipulator
Dim Scale As System.Double
 
instance.UpdateScale(Scale)
```

```

void UpdateScale( 
   System.double Scale
)
```

```

void UpdateScale( 
   System.double Scale
) 
```

#### Parameters

*Scale*
:   Scale

Remarks

The initial length of an axis is 40 pixels, and the length is unrestricted. Each axis is the same length.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITriadManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator.md)  
[ITriadManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator_members.md)  
[ITriadManipulator::DoNotShow Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator~DoNotShow.md)
