# SetMaterialPropertyValues Method (IModelDocExtension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetMaterialPropertyValues`

Sets the material property values for this model document.
Sets the material property values for this model document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetMaterialPropertyValues( _
   ByVal Material_property_values As System.Object, _
   ByVal Config_opt As System.Integer, _
   ByVal Config_names As System.Object _
) 
```

```

Dim instance As IModelDocExtension
Dim Material_property_values As System.Object
Dim Config_opt As System.Integer
Dim Config_names As System.Object
 
instance.SetMaterialPropertyValues(Material_property_values, Config_opt, Config_names)
```

```

void SetMaterialPropertyValues( 
   System.object Material_property_values,
   System.int Config_opt,
   System.object Config_names
)
```

```

void SetMaterialPropertyValues( 
   System.Object^ Material_property_values,
   System.int Config_opt,
   System.Object^ Config_names
) 
```

#### Parameters

*Material\_property\_values*
:   Array of material property values

*Config\_opt*
:   Configuration option as defined in [swInConfigurationOpts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)

*Config\_names*
:   Array of configuration names

Remarks

The material property values include color (R,G,B), reflectivity (ambient, diffuse, specular, shininess), transparency, and emission.

The format of Material\_property\_values is an array of doubles:

> [ R, G, B, Ambient, Diffuse, Specular, Shininess, Transparency, Emission ]

To see a color change, you must:

1. Specify *R*, *G*, and *B*, each with a value between 0.0 and 1.0, inclusive. (These values are internally multiplied by 255.0 to determine the RGB color.)
2. Specify the reflectivity properties (*Diffuse*, *Specular*, *Shininess* (1.0 - Specular spread/Blurriness)), each with a value greater than 0.0 and less than or equal to 1.0.
3. Specify *Ambient*, *Transparency* and *Emission*, each with a value between 0.0 and 1.0, inclusive.
4. Refresh the graphics area after calling this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::GetMaterialPropertyValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetMaterialPropertyValues.md)  
[IModelDocExtension::IGetMaterialPropertyValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetMaterialPropertyValues.md)  
[IModelDocExtension::IRemoveMaterialProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IRemoveMaterialProperty.md)  
[IModelDocExtension::RemoveMaterialProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RemoveMaterialProperty.md)  
[IModelDocExtension::ISetMaterialPropertyValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ISetMaterialPropertyValues.md)  
[IModelDocExtension::HasMaterialPropertyValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~HasMaterialPropertyValues.md)
