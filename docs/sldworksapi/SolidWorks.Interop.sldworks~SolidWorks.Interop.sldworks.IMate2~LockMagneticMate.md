# LockMagneticMate Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~LockMagneticMate`

Gets or sets whether to lock this magnetic mate.
Gets or sets whether to lock this magnetic mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property LockMagneticMate As System.Boolean
```

```

Dim instance As IMate2
Dim value As System.Boolean
 
instance.LockMagneticMate = value
 
value = instance.LockMagneticMate
```

```

System.bool LockMagneticMate {get; set;}
```

```

property System.bool LockMagneticMate {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to lock, false to not

Remarks

This property is valid only if [IMate2::Type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~Type.md) is set to [swMateType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMateType_e.html).swMateMAGNETIC.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.md)  
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.md)
