# SetSpotlightProperties Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetSpotlightProperties`

Sets the spotlight properties.
Sets the spotlight properties.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetSpotlightProperties( _
   ByVal Name As System.String, _
   ByVal Ambient As System.Double, _
   ByVal Diffuse As System.Double, _
   ByVal Specular As System.Double, _
   ByVal Colour As System.Integer, _
   ByVal Enabled As System.Boolean, _
   ByVal Fixed As System.Boolean, _
   ByVal Posx As System.Double, _
   ByVal Posy As System.Double, _
   ByVal Posz As System.Double, _
   ByVal Targetx As System.Double, _
   ByVal Targety As System.Double, _
   ByVal Targetz As System.Double, _
   ByVal ConeAngle As System.Double _
) As System.Boolean
```

```

Dim instance As IModelDoc2
Dim Name As System.String
Dim Ambient As System.Double
Dim Diffuse As System.Double
Dim Specular As System.Double
Dim Colour As System.Integer
Dim Enabled As System.Boolean
Dim Fixed As System.Boolean
Dim Posx As System.Double
Dim Posy As System.Double
Dim Posz As System.Double
Dim Targetx As System.Double
Dim Targety As System.Double
Dim Targetz As System.Double
Dim ConeAngle As System.Double
Dim value As System.Boolean
 
value = instance.SetSpotlightProperties(Name, Ambient, Diffuse, Specular, Colour, Enabled, Fixed, Posx, Posy, Posz, Targetx, Targety, Targetz, ConeAngle)
```

```

System.bool SetSpotlightProperties( 
   System.string Name,
   System.double Ambient,
   System.double Diffuse,
   System.double Specular,
   System.int Colour,
   System.bool Enabled,
   System.bool Fixed,
   System.double Posx,
   System.double Posy,
   System.double Posz,
   System.double Targetx,
   System.double Targety,
   System.double Targetz,
   System.double ConeAngle
)
```

```

System.bool SetSpotlightProperties( 
   System.String^ Name,
   System.double Ambient,
   System.double Diffuse,
   System.double Specular,
   System.int Colour,
   System.bool Enabled,
   System.bool Fixed,
   System.double Posx,
   System.double Posy,
   System.double Posz,
   System.double Targetx,
   System.double Targety,
   System.double Targetz,
   System.double ConeAngle
) 
```

#### Parameters

*Name*
:   Light name to modify

*Ambient*
:   Light source ambient value

*Diffuse*
:   Light source diffuse value

*Specular*
:   Light source specular value

*Colour*
:   COLORREF color value

*Enabled*
:   True to enable light, false to not

*Fixed*
:   True to fix light, false to not

*Posx*
:   x location of the spotlight

*Posy*
:   y location of the spotlight

*Posz*
:   z location of the spotlight

*Targetx*
:   x location of the spotlight target

*Targety*
:   y location of the spotlight target

*Targetz*
:   z location of the spotlight target

*ConeAngle*
:   Cone angle through which the beam spreads in degrees

#### Return Value

True if light properties are modified, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::GetAmbientLightProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetAmbientLightProperties.md)  
[IModelDoc2::GetDirectionLightProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetDirectionLightProperties.md)  
[IModelDoc2::GetPointLightProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetPointLightProperties.md)  
[IModelDoc2::GetSpotlightProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetSpotlightProperties.md)  
[IModelDoc2::SetAmbientLightProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetAmbientLightProperties.md)  
[IModelDoc2::SetDirectionLightProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetDirectionLightProperties.md)  
[IModelDoc2::SetPointLightProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetPointLightProperties.md)
