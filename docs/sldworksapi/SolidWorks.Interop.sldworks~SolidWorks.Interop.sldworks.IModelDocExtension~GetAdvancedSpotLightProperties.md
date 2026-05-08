# GetAdvancedSpotLightProperties Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetAdvancedSpotLightProperties`

Gets the attenuation-related, advanced properties for the specified SOLIDWORKS spot light in this model.
Gets the attenuation-related, advanced properties for the specified SOLIDWORKS spot light in this model.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GetAdvancedSpotLightProperties( _
   ByVal Name As System.String, _
   ByRef Exponent As System.Double, _
   ByRef AttenuationConst As System.Double, _
   ByRef AttenuationLinear As System.Double, _
   ByRef AttenuationQuad As System.Double _
) 
```

```

Dim instance As IModelDocExtension
Dim Name As System.String
Dim Exponent As System.Double
Dim AttenuationConst As System.Double
Dim AttenuationLinear As System.Double
Dim AttenuationQuad As System.Double
 
instance.GetAdvancedSpotLightProperties(Name, Exponent, AttenuationConst, AttenuationLinear, AttenuationQuad)
```

```

void GetAdvancedSpotLightProperties( 
   System.string Name,
   out System.double Exponent,
   out System.double AttenuationConst,
   out System.double AttenuationLinear,
   out System.double AttenuationQuad
)
```

```

void GetAdvancedSpotLightProperties( 
   System.String^ Name,
   [Out] System.double Exponent,
   [Out] System.double AttenuationConst,
   [Out] System.double AttenuationLinear,
   [Out] System.double AttenuationQuad
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

Remarks

See the SOLIDWORKS Help for more information about the advanced properties of spot lights.

Example

[Get Advanced Properties of Spot Light (VBA)](Get_Advanced_Properties_of_Spot_Light_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)
