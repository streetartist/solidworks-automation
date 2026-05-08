# Angle Property (IGtol)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~Angle`

Gets or sets the rotation angle of this Gtol symbol.
Gets or sets the rotation angle of this Gtol symbol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Angle As System.Double
```

```

Dim instance As IGtol
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

Rotation angle in radians

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md)  
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.md)
