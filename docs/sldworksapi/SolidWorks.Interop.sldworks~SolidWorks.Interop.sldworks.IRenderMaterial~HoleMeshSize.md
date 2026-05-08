# HoleMeshSize Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~HoleMeshSize`

Gets or sets the hole mesh size.
Gets or sets the hole mesh size.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property HoleMeshSize As System.Double
```

```

Dim instance As IRenderMaterial
Dim value As System.Double
 
instance.HoleMeshSize = value
 
value = instance.HoleMeshSize
```

```

System.double HoleMeshSize {get; set;}
```

```

property System.double HoleMeshSize {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Hole mesh size

Remarks

This property is valid only if [IRenderMaterial::SurfaceFinishShaderType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SurfaceFinishShaderType.md) is set to:

- [swAppearanceSurfaceFinishShaderTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAppearanceSurfaceFinishShaderTypes_e.html).swAppearanceSurfaceFinishShaderType\_DiamondHoleMesh

    - or -

- swAppearanceSurfaceFinishShaderTypes\_e.swAppearanceSurfaceFinishShaderType\_CircularHoleMesh.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)
