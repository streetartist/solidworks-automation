# ToonShaderTextureFilename Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~ToonShaderTextureFilename`

Gets or sets the path and filename for the toon shader texture file.
Gets or sets the path and filename for the toon shader texture file.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ToonShaderTextureFilename As System.String
```

```

Dim instance As IRenderMaterial
Dim value As System.String
 
instance.ToonShaderTextureFilename = value
 
value = instance.ToonShaderTextureFilename
```

```

System.string ToonShaderTextureFilename {get; set;}
```

```

property System.String^ ToonShaderTextureFilename {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Path and filename for the toon shader texture file

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)
