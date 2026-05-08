# ZAxis Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator~ZAxis`

Gets or sets the z axis for this triad manipulator.
Gets or sets the z axis for this triad manipulator.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ZAxis As MathVector
```

```

Dim instance As ITriadManipulator
Dim value As MathVector
 
instance.ZAxis = value
 
value = instance.ZAxis
```

```

MathVector ZAxis {get; set;}
```

```

property MathVector^ ZAxis {
   MathVector^ get();
   void set (    MathVector^ value);
}
```

#### Property Value

[IMathVector](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md)

Remarks

To update the position of the manipulator, call [ITriadManipulator::UpdatePosition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator~UpdatePosition.md). Moving the triad manipulator to the location set by this property is done by the [handler](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwManipulatorHandler2.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITriadManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator.md)  
[ITriadManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator_members.md)  
[ITriadManipulator::UpdatePosition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator~UpdatePosition.md)  
[ITriadManipulator::Origin Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator~Origin.md)  
[ITriadManipulator::XAxis Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator~XAxis.md)  
[ITriadManipulator::YAxis Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator~YAxis.md)
