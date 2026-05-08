# TextureFilename Property (IRenderMaterial)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~TextureFilename`

Gets or sets the path and filename of the texture for this appearance.
Gets or sets the path and filename of the texture for this appearance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TextureFilename As System.String
```

```

Dim instance As IRenderMaterial
Dim value As System.String
 
instance.TextureFilename = value
 
value = instance.TextureFilename
```

```

System.string TextureFilename {get; set;}
```

```

property System.String^ TextureFilename {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Path and filename of the texture

Example

See the "Add Decal" examples in [IRenderMaterial::FileName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~FileName.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)
