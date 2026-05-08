# CustomHoleMeshFile Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~CustomHoleMeshFile`

Gets or sets the custom hole mesh file.
Gets or sets the custom hole mesh file.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CustomHoleMeshFile As System.String
```

```

Dim instance As IRenderMaterial
Dim value As System.String
 
instance.CustomHoleMeshFile = value
 
value = instance.CustomHoleMeshFile
```

```

System.string CustomHoleMeshFile {get; set;}
```

```

property System.String^ CustomHoleMeshFile {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Path to custom hole mesh file

Remarks

This property is valid only if [IRenderMaterial::SurfaceFinishShaderType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SurfaceFinishShaderType.md) is set to [swAppearanceSurfaceFinishShaderTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAppearanceSurfaceFinishShaderTypes_e.html).swAppearanceSurfaceFinishShaderType\_CustomHoleMesh.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)
