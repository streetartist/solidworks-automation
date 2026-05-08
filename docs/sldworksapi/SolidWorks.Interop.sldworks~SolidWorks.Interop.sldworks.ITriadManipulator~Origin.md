# Origin Property (ITriadManipulator)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator~Origin`

Gets or sets the origin for this triad manipulator.
Gets or sets the origin for this triad manipulator.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Origin As MathPoint
```

```

Dim instance As ITriadManipulator
Dim value As MathPoint
 
instance.Origin = value
 
value = instance.Origin
```

```

MathPoint Origin {get; set;}
```

```

property MathPoint^ Origin {
   MathPoint^ get();
   void set (    MathPoint^ value);
}
```

#### Property Value

[IMathPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md)

Remarks

To update the position of the manipulator, call [ITriadManipulator::UpdatePosition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator~UpdatePosition.md). Moving the triad manipulator to the location set by this property is done by the [handler](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwManipulatorHandler2.md).

Example

See the [ITriadManipulator](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITriadManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator.md)  
[ITriadManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator_members.md)  
[ITriadManipulator::UpdatePosition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator~UpdatePosition.md)  
[ITriadManipulator::XAxis Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator~XAxis.md)  
[ITriadManipulator::YAxis Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator~YAxis.md)  
[ITriadManipulator::ZAxis Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator~ZAxis.md)
