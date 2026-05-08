# SetSpotlightProperties Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SetSpotlightProperties`

Obsolete. Superseded by IModelDoc2::SetSpotlightProperties.
Obsolete. Superseded by [IModelDoc2::SetSpotlightProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetSpotlightProperties.md).

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

Dim instance As IModelDoc
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

*Ambient*

*Diffuse*

*Specular*

*Colour*

*Enabled*

*Fixed*

*Posx*

*Posy*

*Posz*

*Targetx*

*Targety*

*Targetz*

*ConeAngle*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
