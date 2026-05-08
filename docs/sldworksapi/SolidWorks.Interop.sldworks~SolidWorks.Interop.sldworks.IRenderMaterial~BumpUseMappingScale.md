# BumpUseMappingScale Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~BumpUseMappingScale`

Gets or sets whether to use the material's scale and mapping for the surface finish of this appearance.
Gets or sets whether to use the material's scale and mapping for the surface finish of this appearance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property BumpUseMappingScale As System.Boolean
```

```

Dim instance As IRenderMaterial
Dim value As System.Boolean
 
instance.BumpUseMappingScale = value
 
value = instance.BumpUseMappingScale
```

```

System.bool BumpUseMappingScale {get; set;}
```

```

property System.bool BumpUseMappingScale {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to use the material's scale and mapping, false to not

Remarks

If BumpUseMappingScale is set to FALSE, then specify the [scale](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~BumpScale.md) and mapping for this surface finish for this appearance.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)
