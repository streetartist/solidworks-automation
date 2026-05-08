# SelectedFeatureProperties Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SelectedFeatureProperties`

Sets the property values of the selected feature.
Sets the property values of the selected feature.

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

Dim instance As IModelDoc2
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
:   Color of feature (see **Remarks**)

*Ambient*
:   0.0 <= Ambient value <= 1.0

*Diffuse*
:   0.0 < Diffuse value <= 1.0

*Specular*
:   0.0 < Specular value <= 1.0

*Shininess*
:   0.0 < Shininess value <= 1.0

*Transparency*
:   0.0 <= Transparency value <= 1.0

*Emission*
:   0.0 <= Emission value <= 1.0

*UsePartProps*
:   True if the feature inherits the properties from the part, false if not

*Suppressed*
:   True if the feature is suppressed, false if not

*FeatureName*
:   Name of the feature

#### Return Value

True if feature's properties are successfully set, false if not

Remarks

To see a color change, you must:

1. Specify the reflectivity properties (*Diffuse*, *Specular*, *Shininess* (1.0 - Specular spread/Blurriness)), each with a value greater than 0.0 and less than or equal to 1.0.
2. Specify *Ambient*, *Transparency* and *Emission*, each with a value between 0.0 and 1.0, inclusive.
3. Refresh the graphics area after calling this method.

This method is different from [IModelDodc2::SelectedEdgeProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SelectedEdgeProperties.md) and [IModelDoc2::SelectedFaceProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SelectedFaceProperties.md) in that it allows you to change the name of this feature. All features have names; however, a face or edge typically has a name only if it is being referenced. Because it is dangerous to change the name of a referenced object, you cannot programmatically change the names of faces or edges. See [IFeature::Name](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Name.md) and [IPartDoc::SetEntityName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SetEntityName.md) for additional information.

This method requires that the feature to be selected. To select the feature programmatically, you can use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) and pass in the feature name and the appropriate object type (for example, "BODYFEATURE", "ATTRIBUTE", "PLANE", "SKETCH", and so on) and the selection coordinates 0,0,0. To determine the feature name and object type, use the [IFeature::Name](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Name.md) and [IFeature::GetTypeName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetTypeName.md) methods, respectively.

Example

[Create Thicken Feature (VBA)](Create_Thicken_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)
