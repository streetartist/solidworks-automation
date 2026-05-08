# GetAmbientLightProperties Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~GetAmbientLightProperties`

Obsolete. Superseded by IModelDoc2::GetAmbientLightProperties.
Obsolete. Superseded by [IModelDoc2::GetAmbientLightProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetAmbientLightProperties.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetAmbientLightProperties( _
   ByVal Name As System.String, _
   ByRef Ambient As System.Double, _
   ByRef Diffuse As System.Double, _
   ByRef Specular As System.Double, _
   ByRef Colour As System.Integer, _
   ByRef Enabled As System.Boolean, _
   ByRef Fixed As System.Boolean _
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
Dim value As System.Boolean
 
value = instance.GetAmbientLightProperties(Name, Ambient, Diffuse, Specular, Colour, Enabled, Fixed)
```

```

System.bool GetAmbientLightProperties( 
   System.string Name,
   ref System.double Ambient,
   ref System.double Diffuse,
   ref System.double Specular,
   ref System.int Colour,
   ref System.bool Enabled,
   ref System.bool Fixed
)
```

```

System.bool GetAmbientLightProperties( 
   System.String^ Name,
   System.double% Ambient,
   System.double% Diffuse,
   System.double% Specular,
   System.int% Colour,
   System.bool% Enabled,
   System.bool% Fixed
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

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
