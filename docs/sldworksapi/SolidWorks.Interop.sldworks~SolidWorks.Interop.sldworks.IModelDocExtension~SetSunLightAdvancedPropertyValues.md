# SetSunLightAdvancedPropertyValues Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetSunLightAdvancedPropertyValues`

Sets the specified sunlight advanced properties.
Sets the specified sunlight advanced properties.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetSunLightAdvancedPropertyValues( _
   ByVal Haze As System.Double, _
   ByVal SunDiameter As System.Double, _
   ByVal GroundAlbedo As System.Integer, _
   ByVal SkyGamma As System.Double _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim Haze As System.Double
Dim SunDiameter As System.Double
Dim GroundAlbedo As System.Integer
Dim SkyGamma As System.Double
Dim value As System.Boolean
 
value = instance.SetSunLightAdvancedPropertyValues(Haze, SunDiameter, GroundAlbedo, SkyGamma)
```

```

System.bool SetSunLightAdvancedPropertyValues( 
   System.double Haze,
   System.double SunDiameter,
   System.int GroundAlbedo,
   System.double SkyGamma
)
```

```

System.bool SetSunLightAdvancedPropertyValues( 
   System.double Haze,
   System.double SunDiameter,
   System.int GroundAlbedo,
   System.double SkyGamma
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

Remarks

After calling this method, call [IModelDocExtension::UpdateSunLight](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UpdateSunLight.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::GetSunLightAdvancedPropertyValues Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSunLightAdvancedPropertyValues.md)  
[IModelDocExtension::SetSunLightSourcePropertyValues Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetSunLightSourcePropertyValues.md)  
[IModelDocExtension::SunLightInformation Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SunLightInformation.md)
