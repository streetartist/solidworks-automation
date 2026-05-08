# GetDirectionLightProperties Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~GetDirectionLightProperties`

Obsolete. Superseded by IModelDoc2::GetDirectionLightProperties.
Obsolete. Superseded by [IModelDoc2::GetDirectionLightProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetDirectionLightProperties.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDirectionLightProperties( _
   ByVal Name As System.String, _
   ByRef Ambient As System.Double, _
   ByRef Diffuse As System.Double, _
   ByRef Specular As System.Double, _
   ByRef Colour As System.Integer, _
   ByRef Enabled As System.Boolean, _
   ByRef Fixed As System.Boolean, _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
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
Dim value As System.Boolean
 
value = instance.GetDirectionLightProperties(Name, Ambient, Diffuse, Specular, Colour, Enabled, Fixed, X, Y, Z)
```

```

System.bool GetDirectionLightProperties( 
   System.string Name,
   ref System.double Ambient,
   ref System.double Diffuse,
   ref System.double Specular,
   ref System.int Colour,
   ref System.bool Enabled,
   ref System.bool Fixed,
   ref System.double X,
   ref System.double Y,
   ref System.double Z
)
```

```

System.bool GetDirectionLightProperties( 
   System.String^ Name,
   System.double% Ambient,
   System.double% Diffuse,
   System.double% Specular,
   System.int% Colour,
   System.bool% Enabled,
   System.bool% Fixed,
   System.double% X,
   System.double% Y,
   System.double% Z
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

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
