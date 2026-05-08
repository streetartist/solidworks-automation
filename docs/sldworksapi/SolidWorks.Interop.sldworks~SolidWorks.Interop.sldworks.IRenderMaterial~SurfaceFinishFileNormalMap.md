# SurfaceFinishFileNormalMap Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SurfaceFinishFileNormalMap`

Gets or sets whether to map the surface finish file image to the normal.
Gets or sets whether to map the surface finish file image to the normal.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SurfaceFinishFileNormalMap As System.Boolean
```

```

Dim instance As IRenderMaterial
Dim value As System.Boolean
 
instance.SurfaceFinishFileNormalMap = value
 
value = instance.SurfaceFinishFileNormalMap
```

```

System.bool SurfaceFinishFileNormalMap {get; set;}
```

```

property System.bool SurfaceFinishFileNormalMap {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to map the image to the normal, false to not

Remarks

This property is valid only if [IRenderMaterial::SurfaceFinishShaderType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SurfaceFinishShaderType.md) is set to [swAppearanceSurfaceFinishShaderTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAppearanceSurfaceFinishShaderTypes_e.html).swAppearanceSurfaceFinishShaderType\_FromFile.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)
