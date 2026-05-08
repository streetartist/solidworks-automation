# ApplyMaterialHatchToSection Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMaterialVisualPropertiesData~ApplyMaterialHatchToSection`

Gets or sets whether the drawing section views use the material hatch.
Gets or sets whether the drawing section views use the material hatch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ApplyMaterialHatchToSection As System.Boolean
```

```

Dim instance As IMaterialVisualPropertiesData
Dim value As System.Boolean
 
instance.ApplyMaterialHatchToSection = value
 
value = instance.ApplyMaterialHatchToSection
```

```

System.bool ApplyMaterialHatchToSection {get; set;}
```

```

property System.bool ApplyMaterialHatchToSection {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if the [drawing section views](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.md) use the material hatch, false if not

Example

See [IMaterialVisualPropertiesData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMaterialVisualPropertiesData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMaterialVisualPropertiesData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMaterialVisualPropertiesData.md)  
[IMaterialVisualPropertiesData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMaterialVisualPropertiesData_members.md)
