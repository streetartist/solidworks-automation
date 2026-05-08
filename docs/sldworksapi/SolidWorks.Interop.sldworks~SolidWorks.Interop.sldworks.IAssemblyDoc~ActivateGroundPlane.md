# ActivateGroundPlane Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ActivateGroundPlane`

Activates the ground plane for the specified configurations.
Activates the ground plane for the specified configurations.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ActivateGroundPlane( _
   ByVal Config_opt As System.Integer, _
   ByVal Config_names As System.Object _
) As System.Boolean
```

```

Dim instance As IAssemblyDoc
Dim Config_opt As System.Integer
Dim Config_names As System.Object
Dim value As System.Boolean
 
value = instance.ActivateGroundPlane(Config_opt, Config_names)
```

```

System.bool ActivateGroundPlane( 
   System.int Config_opt,
   System.object Config_names
)
```

```

System.bool ActivateGroundPlane( 
   System.int Config_opt,
   System.Object^ Config_names
) 
```

#### Parameters

*Config\_opt*
:   Configurations in which to activate a ground plane as defined in [swInConfigurationOpts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swInConfigurationOpts_e.html):

    - swThisConfiguration
    - swAllConfigurations
    - swSpecifyConfiguration

*Config\_names*
:   Array of configurations in which to activate a ground plane; valid only if Config\_opt is set to swInConfiguration\_e.swSpecifyConfiguration (see **Remarks**)

#### Return Value

True if ground plane successfully activated in the specified configurations, false if not

Remarks

To populate config\_names, use [IModelDoc2::GetConfigurationNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetConfigurationNames.md).

Before calling this method, use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to select the ground plane to activate in the specified configurations.

Only one ground plane can be active at a given time in each assembly configuration.

Example

[Insert and Activate Ground Plane (VBA)](Insert_Ground_Plane_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::GetActiveGroundPlane Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetActiveGroundPlane.md)  
[IFeatureManager::InsertGroundPlane Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertGroundPlane.md)
