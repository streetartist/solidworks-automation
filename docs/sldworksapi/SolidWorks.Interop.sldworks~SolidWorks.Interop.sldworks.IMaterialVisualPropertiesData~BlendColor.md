# BlendColor Property (IMaterialVisualPropertiesData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMaterialVisualPropertiesData~BlendColor`

Gets or sets whether to blend the part color with the texture.
Gets or sets whether to blend the part color with the texture.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property BlendColor As System.Boolean
```

```

Dim instance As IMaterialVisualPropertiesData
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

True to blend the color with the texture, false to not

Remarks

This property on applies to SOLIDWORKS standard textures.

Example

See [IMaterialVisualPropertiesData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMaterialVisualPropertiesData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMaterialVisualPropertiesData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMaterialVisualPropertiesData.md)  
[IMaterialVisualPropertiesData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMaterialVisualPropertiesData_members.md)
