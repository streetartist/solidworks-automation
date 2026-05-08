# TaperAngle Property (ISpring)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~TaperAngle`

Gets or sets the angle by which to taper a compression spring.
Gets or sets the angle by which to taper a compression spring.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TaperAngle As System.Double
```

```

Dim instance As ISpring
Dim value As System.Double
 
instance.TaperAngle = value
 
value = instance.TaperAngle
```

```

System.double TaperAngle {get; set;}
```

```

property System.double TaperAngle {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Angle by which to taper the spring

Remarks

Use [ISpring::TaperOutward](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~TaperOutward.md) to set the direction of the taper outward or inward.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISpring Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring.md)  
[ISpring Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring_members.md)
