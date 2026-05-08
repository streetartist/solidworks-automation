# Tolerance Property (ISpring)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~Tolerance`

Gets or sets the precision of the helical curve.
Gets or sets the precision of the helical curve.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Tolerance As System.Double
```

```

Dim instance As ISpring
Dim value As System.Double
 
instance.Tolerance = value
 
value = instance.Tolerance
```

```

System.double Tolerance {get; set;}
```

```

property System.double Tolerance {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Tolerance

Remarks

Tolerance applies to the extension, torsion, and spiral springs only; tolerance does not apply to springs with variable pitches such as compression springs.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISpring Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring.md)  
[ISpring Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring_members.md)
