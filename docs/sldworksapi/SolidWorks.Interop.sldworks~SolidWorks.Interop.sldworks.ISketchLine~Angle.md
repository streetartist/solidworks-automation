# Angle Property (ISketchLine)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine~Angle`

Gets or sets the angle of the line.
Gets or sets the angle of the line.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Angle As System.Double
```

```

Dim instance As ISketchLine
Dim value As System.Double
 
instance.Angle = value
 
value = instance.Angle
```

```

System.double Angle {get; set;}
```

```

property System.double Angle {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Angle in radians

Remarks

This property does not support lines in 3D sketches.

Example

[Make Line Infinite (VBA)](Make_Line_Infinite_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchLine Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine.md)  
[ISketchLine Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine_members.md)
