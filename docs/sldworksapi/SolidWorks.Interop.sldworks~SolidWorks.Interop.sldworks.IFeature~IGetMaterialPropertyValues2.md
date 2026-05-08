# IGetMaterialPropertyValues2 Method (IFeature)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetMaterialPropertyValues2`

Gets the material property values for this feature in the specified configurations.
Gets the material property values for this feature in the specified configurations.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetMaterialPropertyValues2( _
   ByVal Config_opt As System.Integer, _
   ByVal Config_count As System.Integer, _
   ByRef Config_names As System.String _
) As System.Double
```

```

Dim instance As IFeature
Dim Config_opt As System.Integer
Dim Config_count As System.Integer
Dim Config_names As System.String
Dim value As System.Double
 
value = instance.IGetMaterialPropertyValues2(Config_opt, Config_count, Config_names)
```

```

System.double IGetMaterialPropertyValues2( 
   System.int Config_opt,
   System.int Config_count,
   ref System.string Config_names
)
```

```

System.double IGetMaterialPropertyValues2( 
   System.int Config_opt,
   System.int Config_count,
   System.String^% Config_names
) 
```

#### Parameters

*Config\_opt*
:   Configuration options as defined by [swInConfigurationOpts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)

*Config\_count*
:   Number of configurations

*Config\_names*
:   Array of configuration names of size Config\_count

#### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

The material values returned include the face color (R,G,B values), reflectivity (ambient, diffuse, specular, shininess), transparency, and emission. Valid values are between 0.0 and 1.0, inclusive, for all material properties. If a return value is -1, then that material property was not set for this feature.

If you set Config\_opt to swThisConfiguration or swAllConfiguration, then Config\_names is ignored.

The format of the returned array:

[ R, G, B, Ambient, Diffuse, Specular, Shininess, Transparency, Emission ] \* Config\_count

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)  
[IFeature::GetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetMaterialPropertyValues2.md)  
[IFeature::IRemoveMaterialProperty2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IRemoveMaterialProperty2.md)  
[IFeature::ISetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ISetMaterialPropertyValues2.md)  
[IFeature::RemoveMaterialProperty2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~RemoveMaterialProperty2.md)  
[IFeature::SetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetMaterialPropertyValues2.md)
