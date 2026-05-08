# UpdateSunLight Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UpdateSunLight`

Updates sunlight position, color, and background image.
Updates sunlight position, color, and background image.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function UpdateSunLight() As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim value As System.Boolean
 
value = instance.UpdateSunLight()
```

```

System.bool UpdateSunLight()
```

```

System.bool UpdateSunLight(); 
```

#### Return Value

True if the update is successful, false if not

Remarks

Before calling this method, call [IModelDocExtension::SetSunLightAdvancedPropertyValues](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetSunLightAdvancedPropertyValues.md) to set sunlight advanced properties.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::GetSunLightAdvancedPropertyValues Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSunLightAdvancedPropertyValues.md)  
[IModelDocExtension::SunLightInformation Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SunLightInformation.md)
