# BumpDetail Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~BumpDetail`

Gets or sets the level of granularity for any surface finish for this appearance.
Gets or sets the level of granularity for any surface finish for this appearance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property BumpDetail As System.Integer
```

```

Dim instance As IRenderMaterial
Dim value As System.Integer
 
instance.BumpDetail = value
 
value = instance.BumpDetail
```

```

System.int BumpDetail {get; set;}
```

```

property System.int BumpDetail {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Level of granularity

Remarks

This property is only available when Casting, Rough, Chips, Circular or Rough/Smooth is selected for the [surface finish](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~BumpMap.md).

When set to high detail, individual surface elements appear in sharp focus; when set to low detail, surface elements appear in soft focus.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)
