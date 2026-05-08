# UpdatePosition Method (ITriadManipulator)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator~UpdatePosition`

Updates the position of this triad manipulator.
Updates the position of this triad manipulator.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function UpdatePosition() As System.Boolean
```

```

Dim instance As ITriadManipulator
Dim value As System.Boolean
 
value = instance.UpdatePosition()
```

```

System.bool UpdatePosition()
```

```

System.bool UpdatePosition(); 
```

#### Return Value

True if the position of the triad manipulator is updated, false if not

Remarks

After setting any of these properties, call this method to update the position of the triad manipulator:

- [ITriadManipulator::Origin](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator~Origin.md)
- [ITriadManipulator::XAxis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator~XAxis.md)
- [ITriadManipulator::YAxis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator~YAxis.md)
- [ITriadManipulator::ZAxis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator~ZAxis.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITriadManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator.md)  
[ITriadManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator_members.md)  
[ITriadManipulator::DoNotShow Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator~DoNotShow.md)
