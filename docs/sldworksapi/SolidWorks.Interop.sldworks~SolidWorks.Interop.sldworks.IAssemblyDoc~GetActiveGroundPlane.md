# GetActiveGroundPlane Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetActiveGroundPlane`

Gets the active ground plane for the specified configurations.
Gets the active ground plane for the specified configurations.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetActiveGroundPlane( _
   ByVal Config_opt As System.Integer, _
   ByVal Config_names As System.Object _
) As System.Object
```

```

Dim instance As IAssemblyDoc
Dim Config_opt As System.Integer
Dim Config_names As System.Object
Dim value As System.Object
 
value = instance.GetActiveGroundPlane(Config_opt, Config_names)
```

```

System.object GetActiveGroundPlane( 
   System.int Config_opt,
   System.object Config_names
)
```

```

System.Object^ GetActiveGroundPlane( 
   System.int Config_opt,
   System.Object^ Config_names
) 
```

#### Parameters

*Config\_opt*
:   Configurations from which to retrieve active ground planes as defined in [swInConfigurationOpts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swInConfigurationOpts_e.html):

    - swThisConfiguration
    - swAllConfigurations
    - swSpecifyConfiguration

    (see **Remarks**)

*Config\_names*
:   Array of the names of configurations from which to retrieve active ground planes; valid only if Config\_opt is set to swInConfiguration\_e.swSpecifyConfiguration (see **Remarks**)

#### Return Value

Array of ground plane [features](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

| If Config\_opt is set to swInConfiguration\_e... | Then the returned array contains one active ground plane or null for... |
| --- | --- |
| swAllConfigurations | Each configuration in the assembly. |
| swSpecifyConfiguration | Each configuration in Config\_names. |
| swThisConfiguration | The current configuration. |

To populate config\_names, use [IModelDoc2::GetConfigurationNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetConfigurationNames.md).

Example

[Insert and Activate Ground Plane (VBA)](Insert_Ground_Plane_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::ActivateGroundPlane Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ActivateGroundPlane.md)  
[IFeatureManager::InsertGroundPlane Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertGroundPlane.md)
