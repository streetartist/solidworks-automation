# EndPoint Property (IMagneticLine)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~EndPoint`

Gets and sets the end point of this magnetic line.
Gets and sets the end point of this magnetic line.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property EndPoint As MathPoint
```

```

Dim instance As IMagneticLine
Dim value As MathPoint
 
instance.EndPoint = value
 
value = instance.EndPoint
```

```

MathPoint EndPoint {get; set;}
```

```

property MathPoint^ EndPoint {
   MathPoint^ get();
   void set (    MathPoint^ value);
}
```

#### Property Value

[IMathPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMagneticLine Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine.md)  
[IMagneticLine Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine_members.md)  
[IMagneticLine::StartPoint Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~StartPoint.md)  
[IMagneticLine::Angle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~Angle.md)  
[IMagneticLine::EqualSpacing Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~EqualSpacing.md)  
[IMagneticLine::Length Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~Length.md)
