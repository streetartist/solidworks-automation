# GetMaterialPropertyValues2 Method (IFeature)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetMaterialPropertyValues2`

Gets the material property values for this feature in the specified configurations.
Gets the material property values for this feature in the specified configurations.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetMaterialPropertyValues2( _
   ByVal Config_opt As System.Integer, _
   ByVal Config_names As System.Object _
) As System.Object
```

```

Dim instance As IFeature
Dim Config_opt As System.Integer
Dim Config_names As System.Object
Dim value As System.Object
 
value = instance.GetMaterialPropertyValues2(Config_opt, Config_names)
```

```

System.object GetMaterialPropertyValues2( 
   System.int Config_opt,
   System.object Config_names
)
```

```

System.Object^ GetMaterialPropertyValues2( 
   System.int Config_opt,
   System.Object^ Config_names
) 
```

#### Parameters

*Config\_opt*
:   Configuration options as defined by [swInConfigurationOpts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)

*Config\_names*
:   Array of configuration names for this component (see **Remarks**)

#### Return Value

Array of material property values for this component

Remarks

The material property values returned include the face color (R,G,B values), reflectivity (ambient, diffuse, specular, shininess), transparency, and emission. Valid values are between 0.0 and 1.0, inclusive, for all material properties. If a return value is -1, then that material property was not set for this feature.

If you set Config\_opt to swThisConfiguration or swAllConfiguration, then Config\_names is ignored. The size of the returned array depends on how you specify Config\_opt and Config\_names. See the example.

The format of the returned array:

[ R, G, B, Ambient, Diffuse, Specular, Shininess, Transparency, Emission ] \* *number\_of\_configurations*

where:

*number\_of\_configurations* = number of configurations specified by Config\_opt and Config\_names

Example

[Get Material Properties (VBA)](Get_Material_Properties_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)  
[IFeature::IGetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetMaterialPropertyValues2.md)  
[IFeature::ISetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ISetMaterialPropertyValues2.md)  
[IFeature::IRemoveMaterialProperty2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IRemoveMaterialProperty2.md)  
[IFeature::RemoveMaterialProperty2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~RemoveMaterialProperty2.md)  
[IFeature::SetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetMaterialPropertyValues2.md)  
[IFeature::HasMaterialPropertyValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~HasMaterialPropertyValues.md)
