# GetSunLightAdvancedPropertyValues Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSunLightAdvancedPropertyValues`

Gets the specified sunlight advanced properties.
Gets the specified sunlight advanced properties.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSunLightAdvancedPropertyValues( _
   ByRef Haze As System.Double, _
   ByRef SunDiameter As System.Double, _
   ByRef GroundAlbedo As System.Integer, _
   ByRef SkyGamma As System.Double _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim Haze As System.Double
Dim SunDiameter As System.Double
Dim GroundAlbedo As System.Integer
Dim SkyGamma As System.Double
Dim value As System.Boolean
 
value = instance.GetSunLightAdvancedPropertyValues(Haze, SunDiameter, GroundAlbedo, SkyGamma)
```

```

System.bool GetSunLightAdvancedPropertyValues( 
   out System.double Haze,
   out System.double SunDiameter,
   out System.int GroundAlbedo,
   out System.double SkyGamma
)
```

```

System.bool GetSunLightAdvancedPropertyValues( 
   [Out] System.double Haze,
   [Out] System.double SunDiameter,
   [Out] System.int GroundAlbedo,
   [Out] System.double SkyGamma
) 
```

#### Parameters

*Haze*
:   0.0 <= Haze setting < = 1.0

*SunDiameter*
:   0.01 < = sun diameter visible in the scene <= 21474836.47

*GroundAlbedo*
:   RGB color reflected from the ground upwards

*SkyGamma*
:   0.1 <= visible sky Output Gamma <= 100.0

#### Return Value

True if successful, false if not

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
[IModelDocExtension::SetSunLightAdvancedPropertyValues Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetSunLightAdvancedPropertyValues.md)  
[IModelDocExtension::UpdateSunLight Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UpdateSunLight.md)  
[IModelDocExtension::GetSunLightSourcePropertyValues Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSunLightSourcePropertyValues.md)  
[IModelDocExtension::SunLightInformation Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SunLightInformation.md)
