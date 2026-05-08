# EqualSpacing Property (IMagneticLine)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~EqualSpacing`

Gets and sets whether to equally space the notes on this magnetic line.
Gets and sets whether to equally space the notes on this magnetic line.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property EqualSpacing As System.Boolean
```

```

Dim instance As IMagneticLine
Dim value As System.Boolean
 
instance.EqualSpacing = value
 
value = instance.EqualSpacing
```

```

System.bool EqualSpacing {get; set;}
```

```

property System.bool EqualSpacing {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to equally space the notes, false to drag the notes to any location on the magnetic line (see **Remarks**)

Remarks

If this property is set to true, then [IMagneticLine::AddNote](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~AddNote.md) ignores any Position parameter value.

Example

[Insert Magnetic Line (VBA)](Insert_Magnetic_Line_Example_VB.htm)  
[Insert Magnetic Line (VB.NET)](Insert_Magnetic_Line_Example_VBNET.htm)  
[Insert Magnetic Line (C#)](Insert_Magnetic_Line_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMagneticLine Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine.md)  
[IMagneticLine Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine_members.md)  
[IMagneticLine::Angle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~Angle.md)  
[IMagneticLine::EndPoint Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~EndPoint.md)  
[IMagneticLine::StartPoint Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~StartPoint.md)  
[IMagneticLine::Length Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~Length.md)
