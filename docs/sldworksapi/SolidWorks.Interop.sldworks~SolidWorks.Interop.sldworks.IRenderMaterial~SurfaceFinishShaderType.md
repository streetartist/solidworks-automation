# SurfaceFinishShaderType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SurfaceFinishShaderType`

Gets or sets the type of surface finish for the appearance.
Gets or sets the type of surface finish for the appearance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SurfaceFinishShaderType As System.Integer
```

```

Dim instance As IRenderMaterial
Dim value As System.Integer
 
instance.SurfaceFinishShaderType = value
 
value = instance.SurfaceFinishShaderType
```

```

System.int SurfaceFinishShaderType {get; set;}
```

```

property System.int SurfaceFinishShaderType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Surface finish shader type as defined by [swAppearanceSurfaceFinishShaderTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAppearanceSurfaceFinishShaderTypes_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)
