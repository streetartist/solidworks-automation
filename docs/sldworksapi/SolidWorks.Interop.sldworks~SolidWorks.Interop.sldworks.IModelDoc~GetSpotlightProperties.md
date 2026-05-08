# GetSpotlightProperties Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~GetSpotlightProperties`

Obsolete. Superseded by IModelDoc2::GetSpotlightProperties.
Obsolete. Superseded by [IModelDoc2::GetSpotlightProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetSpotlightProperties.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSpotlightProperties( _
   ByVal Name As System.String, _
   ByRef Ambient As System.Double, _
   ByRef Diffuse As System.Double, _
   ByRef Specular As System.Double, _
   ByRef Colour As System.Integer, _
   ByRef Enabled As System.Boolean, _
   ByRef Fixed As System.Boolean, _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double, _
   ByRef Targetx As System.Double, _
   ByRef Targety As System.Double, _
   ByRef Targetz As System.Double, _
   ByRef ConeAngle As System.Double _
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
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim Targetx As System.Double
Dim Targety As System.Double
Dim Targetz As System.Double
Dim ConeAngle As System.Double
Dim value As System.Boolean
 
value = instance.GetSpotlightProperties(Name, Ambient, Diffuse, Specular, Colour, Enabled, Fixed, X, Y, Z, Targetx, Targety, Targetz, ConeAngle)
```

```

System.bool GetSpotlightProperties( 
   System.string Name,
   ref System.double Ambient,
   ref System.double Diffuse,
   ref System.double Specular,
   ref System.int Colour,
   ref System.bool Enabled,
   ref System.bool Fixed,
   ref System.double X,
   ref System.double Y,
   ref System.double Z,
   ref System.double Targetx,
   ref System.double Targety,
   ref System.double Targetz,
   ref System.double ConeAngle
)
```

```

System.bool GetSpotlightProperties( 
   System.String^ Name,
   System.double% Ambient,
   System.double% Diffuse,
   System.double% Specular,
   System.int% Colour,
   System.bool% Enabled,
   System.bool% Fixed,
   System.double% X,
   System.double% Y,
   System.double% Z,
   System.double% Targetx,
   System.double% Targety,
   System.double% Targetz,
   System.double% ConeAngle
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

*X*

*Y*

*Z*

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
