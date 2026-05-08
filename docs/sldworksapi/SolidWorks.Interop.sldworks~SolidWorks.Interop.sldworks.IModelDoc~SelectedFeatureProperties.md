# SelectedFeatureProperties Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SelectedFeatureProperties`

Obsolete. Superseded by IModelDoc2::SelectedFeatureProperties.
Obsolete. Superseded by [IModelDoc2::SelectedFeatureProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SelectedFeatureProperties.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SelectedFeatureProperties( _
   ByVal RgbColor As System.Integer, _
   ByVal Ambient As System.Double, _
   ByVal Diffuse As System.Double, _
   ByVal Specular As System.Double, _
   ByVal Shininess As System.Double, _
   ByVal Transparency As System.Double, _
   ByVal Emission As System.Double, _
   ByVal UsePartProps As System.Boolean, _
   ByVal Suppressed As System.Boolean, _
   ByVal FeatureName As System.String _
) As System.Boolean
```

```

Dim instance As IModelDoc
Dim RgbColor As System.Integer
Dim Ambient As System.Double
Dim Diffuse As System.Double
Dim Specular As System.Double
Dim Shininess As System.Double
Dim Transparency As System.Double
Dim Emission As System.Double
Dim UsePartProps As System.Boolean
Dim Suppressed As System.Boolean
Dim FeatureName As System.String
Dim value As System.Boolean
 
value = instance.SelectedFeatureProperties(RgbColor, Ambient, Diffuse, Specular, Shininess, Transparency, Emission, UsePartProps, Suppressed, FeatureName)
```

```

System.bool SelectedFeatureProperties( 
   System.int RgbColor,
   System.double Ambient,
   System.double Diffuse,
   System.double Specular,
   System.double Shininess,
   System.double Transparency,
   System.double Emission,
   System.bool UsePartProps,
   System.bool Suppressed,
   System.string FeatureName
)
```

```

System.bool SelectedFeatureProperties( 
   System.int RgbColor,
   System.double Ambient,
   System.double Diffuse,
   System.double Specular,
   System.double Shininess,
   System.double Transparency,
   System.double Emission,
   System.bool UsePartProps,
   System.bool Suppressed,
   System.String^ FeatureName
) 
```

#### Parameters

*RgbColor*

*Ambient*

*Diffuse*

*Specular*

*Shininess*

*Transparency*

*Emission*

*UsePartProps*

*Suppressed*

*FeatureName*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
