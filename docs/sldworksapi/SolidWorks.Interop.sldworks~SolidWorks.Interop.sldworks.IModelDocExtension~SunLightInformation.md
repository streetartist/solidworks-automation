# SunLightInformation Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SunLightInformation`

Gets the specified sunlight information.
Gets the specified sunlight information.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property SunLightInformation( _
   ByVal Type As System.Integer _
) As System.Double
```

```

Dim instance As IModelDocExtension
Dim Type As System.Integer
Dim value As System.Double
 
value = instance.SunLightInformation(Type)
```

```

System.double SunLightInformation( 
   System.int Type
) {get;}
```

```

property System.double SunLightInformation {
   System.double get(System.int Type);
}
```

#### Parameters

*Type*
:   Sunlight information as defined by [swSunlightInfoType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSunlightInfoType_e.html)

#### Property Value

Sunlight information

Example

[Get and Set Sunlight Source Property Values (VBA)](Get_and_Set_Sunlight_Source_Property_Values_Example_VB.htm)  
[Get and Set Sunlight Source Property Values (VB.NET)](Get_and_Set_Sunlight_Source_Property_Values_Example_VBNET.htm)  
[Get and Set Sunlight Source Property Values (C#)](Get_and_Set_Sunlight_Source_Property_Values_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::UpdateSunLight Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UpdateSunLight.md)  
[IModelDocExtension::GetSunLightAdvancedPropertyValues Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSunLightAdvancedPropertyValues.md)  
[IModelDocExtension::SetSunLightAdvancedPropertyValues Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetSunLightAdvancedPropertyValues.md)
