# ApplyAppearance Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMaterialVisualPropertiesData~ApplyAppearance`

Gets or sets whether to apply the appearance of material.
Gets or sets whether to apply the appearance of material.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ApplyAppearance As System.Boolean
```

```

Dim instance As IMaterialVisualPropertiesData
Dim value As System.Boolean
 
instance.ApplyAppearance = value
 
value = instance.ApplyAppearance
```

```

System.bool ApplyAppearance {get; set;}
```

```

property System.bool ApplyAppearance {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to apply the appearance of material, false to not (see **Remarks**)

Remarks

| If this property is... | Then... |
| --- | --- |
| False | There is no change in the appearance of the body when material is changed. |
| True | The appearance of the body changes when material is changed. |

Example

See [IMaterialVisualPropertiesData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMaterialVisualPropertiesData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMaterialVisualPropertiesData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMaterialVisualPropertiesData.md)  
[IMaterialVisualPropertiesData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMaterialVisualPropertiesData_members.md)
