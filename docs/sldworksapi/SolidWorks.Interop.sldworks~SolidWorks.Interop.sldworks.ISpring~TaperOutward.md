# TaperOutward Property (ISpring)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~TaperOutward`

Gets or sets the direction by which to taper the helix of a compression spring.
Gets or sets the direction by which to taper the helix of a compression spring.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TaperOutward As System.Boolean
```

```

Dim instance As ISpring
Dim value As System.Boolean
 
instance.TaperOutward = value
 
value = instance.TaperOutward
```

```

System.bool TaperOutward {get; set;}
```

```

property System.bool TaperOutward {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to taper the helix outward, false to tape inward

Remarks

Use [ISpring::TaperAngle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~TaperAngle.md) to set the angle by which to taper a spring.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISpring Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring.md)  
[ISpring Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring_members.md)
