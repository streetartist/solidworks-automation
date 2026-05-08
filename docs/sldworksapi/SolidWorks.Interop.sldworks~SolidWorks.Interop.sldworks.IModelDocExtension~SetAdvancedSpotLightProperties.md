# SetAdvancedSpotLightProperties Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetAdvancedSpotLightProperties`

Sets the attenuation-related, advanced properties for the specified SOLIDWORKS spot light in this model.
Sets the attenuation-related, advanced properties for the specified SOLIDWORKS spot light in this model.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetAdvancedSpotLightProperties( _
   ByVal Name As System.String, _
   ByVal Exponent As System.Double, _
   ByVal AttenuationConst As System.Double, _
   ByVal AttenuationLinear As System.Double, _
   ByVal AttenuationQuad As System.Double _
) 
```

```

Dim instance As IModelDocExtension
Dim Name As System.String
Dim Exponent As System.Double
Dim AttenuationConst As System.Double
Dim AttenuationLinear As System.Double
Dim AttenuationQuad As System.Double
 
instance.SetAdvancedSpotLightProperties(Name, Exponent, AttenuationConst, AttenuationLinear, AttenuationQuad)
```

```

void SetAdvancedSpotLightProperties( 
   System.string Name,
   System.double Exponent,
   System.double AttenuationConst,
   System.double AttenuationLinear,
   System.double AttenuationQuad
)
```

```

void SetAdvancedSpotLightProperties( 
   System.String^ Name,
   System.double Exponent,
   System.double AttenuationConst,
   System.double AttenuationLinear,
   System.double AttenuationQuad
) 
```

#### Parameters

*Name*
:   SOLIDWORKS light source name

*Exponent*
:   Attenuation exponent

*AttenuationConst*
:   Constant attenuation factor

*AttenuationLinear*
:   Linear attenuation factor

*AttenuationQuad*
:   Quadratic attenuation factor

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)
