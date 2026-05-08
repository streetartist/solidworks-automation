# BlendColor Property (ITexture)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture~BlendColor`

Gets or sets whether to blend the part color with the texture color.
Gets or sets whether to blend the part color with the texture color.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property BlendColor As System.Boolean
```

```

Dim instance As ITexture
Dim value As System.Boolean
 
instance.BlendColor = value
 
value = instance.BlendColor
```

```

System.bool BlendColor {get; set;}
```

```

property System.bool BlendColor {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to blend the colors of the part and texture, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITexture Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture.md)  
[ITexture Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture_members.md)
