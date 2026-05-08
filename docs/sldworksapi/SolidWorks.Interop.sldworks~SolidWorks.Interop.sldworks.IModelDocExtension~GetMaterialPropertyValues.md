# GetMaterialPropertyValues Method (IModelDocExtension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetMaterialPropertyValues`

Gets the material properties for this model document.
Gets the material properties for this model document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetMaterialPropertyValues( _
   ByVal Config_opt As System.Integer, _
   ByVal Config_names As System.Object _
) As System.Object
```

```

Dim instance As IModelDocExtension
Dim Config_opt As System.Integer
Dim Config_names As System.Object
Dim value As System.Object
 
value = instance.GetMaterialPropertyValues(Config_opt, Config_names)
```

```

System.object GetMaterialPropertyValues( 
   System.int Config_opt,
   System.object Config_names
)
```

```

System.Object^ GetMaterialPropertyValues( 
   System.int Config_opt,
   System.Object^ Config_names
) 
```

#### Parameters

*Config\_opt*
:   Configuration options as defined by [swInConfigurationOpts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)

*Config\_names*
:   Array of configuration names for this component

#### Return Value

Array of material values for this component (see **Remarks**)

Remarks

The material values returned include the face color (R,G,B values), reflectivity (ambient, diffuse, specular, shininess), transparency, and emission.

The format of material\_values is an array of doubles:

[ R, G, B, Ambient, Diffuse, Specular, Shininess, Transparency, Emission ]

Valid values are from 0 to 1 for all variables. If material\_values is all -1 values, then material property values were not assigned to the feature. Therefore, the feature will have the default properties in the user interface.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::IGetMaterialPropertyValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetMaterialPropertyValues.md)  
[IModelDocExtension::RemoveMaterialProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RemoveMaterialProperty.md)  
[IModelDocExtension::IRemoveMaterialProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IRemoveMaterialProperty.md)  
[IModelDocExtension::SetMaterialPropertyValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetMaterialPropertyValues.md)  
[IModelDocExtension::ISetMaterialPropertyValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ISetMaterialPropertyValues.md)  
[IModelDocExtension::HasMaterialPropertyValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~HasMaterialPropertyValues.md)
