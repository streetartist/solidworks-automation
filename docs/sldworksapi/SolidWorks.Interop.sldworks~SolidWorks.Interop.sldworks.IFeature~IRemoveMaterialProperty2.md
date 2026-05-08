# IRemoveMaterialProperty2 Method (IFeature)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IRemoveMaterialProperty2`

Removes material property values from this feature.
Removes material property values from this feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IRemoveMaterialProperty2( _
   ByVal Config_opt As System.Integer, _
   ByVal Config_count As System.Integer, _
   ByRef Config_names As System.String _
) As System.Boolean
```

```

Dim instance As IFeature
Dim Config_opt As System.Integer
Dim Config_count As System.Integer
Dim Config_names As System.String
Dim value As System.Boolean
 
value = instance.IRemoveMaterialProperty2(Config_opt, Config_count, Config_names)
```

```

System.bool IRemoveMaterialProperty2( 
   System.int Config_opt,
   System.int Config_count,
   ref System.string Config_names
)
```

```

System.bool IRemoveMaterialProperty2( 
   System.int Config_opt,
   System.int Config_count,
   System.String^% Config_names
) 
```

#### Parameters

*Config\_opt*
:   Configuration option as defined in [swInConfigurationOpts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)

*Config\_count*
:   Number of configurations

*Config\_names*
:   - in-process, unmanaged C++: Pointer to an array of configuration names

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

#### Return Value

True if material property values are removed, false if not

Remarks

This method is intended to be used on features that have a changed material property value; for example, color.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)  
[IFeature::GetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetMaterialPropertyValues2.md)  
[IFeature::IGetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetMaterialPropertyValues2.md)  
[IFeature::IRemoveMaterialProperty2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IRemoveMaterialProperty2.md)  
[IFeature::RemoveMaterialProperty2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~RemoveMaterialProperty2.md)  
[IFeature::SetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetMaterialPropertyValues2.md)
