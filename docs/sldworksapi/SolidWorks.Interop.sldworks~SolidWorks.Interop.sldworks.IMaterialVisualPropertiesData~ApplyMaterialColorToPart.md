# ApplyMaterialColorToPart Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMaterialVisualPropertiesData~ApplyMaterialColorToPart`

Gets or sets whether the part color matches the material color.
Gets or sets whether the part color matches the material color.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ApplyMaterialColorToPart As System.Boolean
```

```

Dim instance As IMaterialVisualPropertiesData
Dim value As System.Boolean
 
instance.ApplyMaterialColorToPart = value
 
value = instance.ApplyMaterialColorToPart
```

```

System.bool ApplyMaterialColorToPart {get; set;}
```

```

property System.bool ApplyMaterialColorToPart {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if the part color matches the material color, false if not

Example

See [IMaterialVisualPropertiesData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMaterialVisualPropertiesData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMaterialVisualPropertiesData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMaterialVisualPropertiesData.md)  
[IMaterialVisualPropertiesData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMaterialVisualPropertiesData_members.md)
