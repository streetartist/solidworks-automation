# GroundType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~GroundType`

Gets or sets whether the ends of compression spring are ground to a flat surface or have the same pitch as the coil.
Gets or sets whether the ends of compression spring are ground to a flat surface or have the same pitch as the coil.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property GroundType As System.Integer
```

```

Dim instance As ISpring
Dim value As System.Integer
 
instance.GroundType = value
 
value = instance.GroundType
```

```

System.int GroundType {get; set;}
```

```

property System.int GroundType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

0 for ends to be ground to a flat surface, 1 for ends to have same pitch as the coil

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISpring Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring.md)  
[ISpring Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring_members.md)
