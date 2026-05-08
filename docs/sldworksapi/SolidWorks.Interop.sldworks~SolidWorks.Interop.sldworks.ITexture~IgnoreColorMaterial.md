# IgnoreColorMaterial Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture~IgnoreColorMaterial`

Gets whether to ignore the color texture-based appearance.
Gets whether to ignore the color texture-based appearance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property IgnoreColorMaterial As System.Boolean
```

```

Dim instance As ITexture
Dim value As System.Boolean
 
value = instance.IgnoreColorMaterial
```

```

System.bool IgnoreColorMaterial {get;}
```

```

property System.bool IgnoreColorMaterial {
   System.bool get();
}
```

#### Property Value

True to ignore the color of this texture-based appearance, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITexture Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture.md)  
[ITexture Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture_members.md)
