# SetExcludeFromBOM2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetExcludeFromBOM2`

Sets whether to exclude this component from the bills of materials (BOMs) in the specified configurations.
Sets whether to exclude this component from the bills of materials (BOMs) in the specified configurations.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetExcludeFromBOM2( _
   ByVal Exclude As System.Boolean, _
   ByVal Config_opt As System.Integer, _
   ByVal Config_names As System.Object _
) As System.Integer
```

```

Dim instance As IComponent2
Dim Exclude As System.Boolean
Dim Config_opt As System.Integer
Dim Config_names As System.Object
Dim value As System.Integer
 
value = instance.SetExcludeFromBOM2(Exclude, Config_opt, Config_names)
```

```

System.int SetExcludeFromBOM2( 
   System.bool Exclude,
   System.int Config_opt,
   System.object Config_names
)
```

```

System.int SetExcludeFromBOM2( 
   System.bool Exclude,
   System.int Config_opt,
   System.Object^ Config_names
) 
```

#### Parameters

*Exclude*
:   True to exclude it, false to not

*Config\_opt*
:   Configuration option as defined in [swInConfigurationOpts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swInConfigurationOpts_e.html)

*Config\_names*
:   Array of the names of configurations for which to set Exclude; null or Nothing if Config\_opt is set to swInConfigurationOpts.swAllConfiguration or swInConfigurationOpts.swThisConfiguration

#### Return Value

Return code as defined in [swExcludeFromBOMError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swExcludeFromBOMError_e.html)

Remarks

This method is valid only for [table-based bills of materials](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.md); it does not work for Microsoft Excel-based bills of materials.

If you set Exclude to true, the name of the component changes in the FeatureManager design tree of the specified configuration; (Excluded from BOM) is appended. To update the FeatureManager design tree, call [IFeatureManager::UpdateFeatureTree](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~UpdateFeatureTree.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IAssemblyDoc::CompConfigProperties6 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CompConfigProperties6.md)  
[IComponent2::GetExcludeFromBOM2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetExcludeFromBOM2.md)
