# SelectedFaceProperties Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SelectedFaceProperties`

Sets the material property values of the selected face.
Sets the material property values of the selected face.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SelectedFaceProperties( _
   ByVal RgbColor As System.Integer, _
   ByVal Ambient As System.Double, _
   ByVal Diffuse As System.Double, _
   ByVal Specular As System.Double, _
   ByVal Shininess As System.Double, _
   ByVal Transparency As System.Double, _
   ByVal Emission As System.Double, _
   ByVal UsePartProps As System.Boolean, _
   ByVal FaceName As System.String _
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
Dim FaceName As System.String
Dim value As System.Boolean
 
value = instance.SelectedFaceProperties(RgbColor, Ambient, Diffuse, Specular, Shininess, Transparency, Emission, UsePartProps, FaceName)
```

```

System.bool SelectedFaceProperties( 
   System.int RgbColor,
   System.double Ambient,
   System.double Diffuse,
   System.double Specular,
   System.double Shininess,
   System.double Transparency,
   System.double Emission,
   System.bool UsePartProps,
   System.string FaceName
)
```

```

System.bool SelectedFaceProperties( 
   System.int RgbColor,
   System.double Ambient,
   System.double Diffuse,
   System.double Specular,
   System.double Shininess,
   System.double Transparency,
   System.double Emission,
   System.bool UsePartProps,
   System.String^ FaceName
) 
```

#### Parameters

*RgbColor*
:   Face color (see **Remarks**)

*Ambient*
:   0.0 <= Face ambient light value <= 1.0

*Diffuse*
:   0.0 < Face diffuse value <= 1.0

*Specular*
:   0.0 < Face specular value <= 1.0

*Shininess*
:   0.0 < Face shininess value <= 1.0

*Transparency*
:   0.0 <= Face transparency value <= 1.0

*Emission*
:   0.0 <= Face emission value <= 1.0

*UsePartProps*
:   True if the face inherits the Part properties, false if not

*FaceName*
:   Name of the face

#### Return Value

True if face properties successfully changed, false if not

Remarks

To see a color change, you must:

1. Specify the reflectivity properties (*Diffuse*, *Specular*, *Shininess* (1.0 - Specular spread/Blurriness)), each with a value greater than 0.0 and less than or equal to 1.0.
2. Specify *Ambient*, *Transparency* and *Emission*, each with a value between 0.0 and 1.0, inclusive.
3. Refresh the graphics area after calling this method.

You can use the FaceName argument to set the name for this face.

If the face has a name, then this method does not change the name and returns false. This behavior is intended to prevent a program from renaming a face that is referenced in some other location.

For example, if an assembly contains a mate to a face on a part, then a name is automatically assigned to that face. If you change that name, then there is no guarantee that the mate will still be valid. Therefore, when using entity names, you should first check to see if the entity is already named, and, if so, use the existing name. If no name exists for the face, then you can assign the face a name.

Example

[Change Color of Face (VBA)](Change_Color_of_Face_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::SelectedEdgeProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SelectedEdgeProperties.md)  
[IModelDoc2::SelectedFeatureProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SelectedFeatureProperties.md)  
[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)  
[IModelDoc2::EntityProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EntityProperties.md)
