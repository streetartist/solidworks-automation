# ISetMaterialPropertyValues2 Method (IComponent2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ISetMaterialPropertyValues2`

Sets the material properties for this component.
Sets the material properties for this component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetMaterialPropertyValues2( _
   ByRef Material_values As System.Double, _
   ByVal Config_opt As System.Integer, _
   ByVal Config_count As System.Integer, _
   ByRef Config_names As System.String _
) 
```

```

Dim instance As IComponent2
Dim Material_values As System.Double
Dim Config_opt As System.Integer
Dim Config_count As System.Integer
Dim Config_names As System.String
 
instance.ISetMaterialPropertyValues2(Material_values, Config_opt, Config_count, Config_names)
```

```

void ISetMaterialPropertyValues2( 
   ref System.double Material_values,
   System.int Config_opt,
   System.int Config_count,
   ref System.string Config_names
)
```

```

void ISetMaterialPropertyValues2( 
   System.double% Material_values,
   System.int Config_opt,
   System.int Config_count,
   System.String^% Config_names
) 
```

#### Parameters

*Material\_values*
:   Array of doubles of size 9 (see **Remarks**)

*Config\_opt*
:   Configuration option as defined in [swInConfigurationOpts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)

*Config\_count*
:   Number of configurations for this component

*Config\_names*
:   - in-process, unmanaged C++: Pointer to an array of configuration names of size Config\_count

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

The material property values include the color (R,G,B values), reflectivity (ambient, diffuse, specular, shininess), transparency, and emission.

The format of Material\_values is an array of doubles:

> **[** *R, G, B, Ambient, Diffuse, Specular, Shininess, Transparency, Emission* **]**

To see a color change, you must:

1. Specify *R*, *G*, and *B*, each with a value between 0.0 and 1.0, inclusive. (These values are internally multiplied by 255.0 to determine the RGB color.)
2. Specify the reflectivity properties (*Diffuse*, *Specular*, *Shininess* (1.0 - Specular spread/Blurriness)), each with a value greater than 0.0 and less than or equal to 1.0.
3. Specify *Ambient*, *Transparency* and *Emission*, each with a value between 0.0 and 1.0, inclusive.
4. Refresh the graphics area after calling this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IComponent2::SetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetMaterialPropertyValues2.md)  
[IComponent2::IGetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetMaterialPropertyValues2.md)  
[IComponent2::GetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetMaterialPropertyValues2.md)  
[IComponent2::RemoveMaterialProperty2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~RemoveMaterialProperty2.md)  
[IComponent2::IRemoveMaterialProperty2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IRemoveMaterialProperty2.md)  
[IComponent2::IMaterialPropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IMaterialPropertyValues.md)  
[IComponent2::MaterialPropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~MaterialPropertyValues.md)
