# Length Property (IMagneticLine)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~Length`

Gets and sets the length of this magnetic line.
Gets and sets the length of this magnetic line.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Length As System.Double
```

```

Dim instance As IMagneticLine
Dim value As System.Double
 
instance.Length = value
 
value = instance.Length
```

```

System.double Length {get; set;}
```

```

property System.double Length {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Length in meters of this magnetic line

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
[IMagneticLine::Angle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~Angle.md)  
[IMagneticLine::EndPoint Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~EndPoint.md)  
[IMagneticLine::StartPoint Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~StartPoint.md)  
[IMagneticLine::EqualSpacing Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~EqualSpacing.md)
