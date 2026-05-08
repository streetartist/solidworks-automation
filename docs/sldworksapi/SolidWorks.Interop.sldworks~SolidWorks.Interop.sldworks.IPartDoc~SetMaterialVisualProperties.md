# SetMaterialVisualProperties Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SetMaterialVisualProperties`

Sets the material visual properties for the active configuration and any specified configurations of this part.
Sets the material visual properties for the active configuration and any specified configurations of this part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetMaterialVisualProperties( _
   ByVal Properties As MaterialVisualPropertiesData, _
   ByVal ConfigOption As System.Integer, _
   ByVal ConfigNames As System.Object _
) As System.Integer
```

```

Dim instance As IPartDoc
Dim Properties As MaterialVisualPropertiesData
Dim ConfigOption As System.Integer
Dim ConfigNames As System.Object
Dim value As System.Integer
 
value = instance.SetMaterialVisualProperties(Properties, ConfigOption, ConfigNames)
```

```

System.int SetMaterialVisualProperties( 
   MaterialVisualPropertiesData Properties,
   System.int ConfigOption,
   System.object ConfigNames
)
```

```

System.int SetMaterialVisualProperties( 
   MaterialVisualPropertiesData^ Properties,
   System.int ConfigOption,
   System.Object^ ConfigNames
) 
```

#### Parameters

*Properties*
:   [Material visual properties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMaterialVisualPropertiesData.md)

*ConfigOption*
:   Configurations as defined in [swInConfigurationOpts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)

*ConfigNames*
:   Array of strings of the names of the configurations whose material visual properties to set

#### Return Value

0 on success, non-0 on failure

Remarks

ConfigNames is used only when ConfigOption is set to swSpecifyConfiguration. If a different value is specified for ConfigOption, then ConfigNames is ignored.

This method always affects the active configuration, regardless of the value specified for ConfigNames.

Example

[Get and Set Material Visual Properties (VBA)](Get_and_Set_Material_Visual_Properties_Example_VB.htm)  
[Get and Set Material Visual Properties (VB.NET)](Get_and_Set_Material_Visual_Properties_Example_VBNET.htm)  
[Get and Set Material Visual Properties (C#)](Get_and_Set_Material_Visual_Properties_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)  
[IPartDoc::GetMaterialPropertyName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetMaterialPropertyName2.md)  
[IPartDoc::GetMaterialVisualProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetMaterialVisualProperties.md)  
[IPartDoc::SetMaterialPropertyName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SetMaterialPropertyName2.md)  
[IPartDoc::IMaterialPropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IMaterialPropertyValues.md)  
[IPartDoc::MaterialIdName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~MaterialIdName.md)  
[IPartDoc::MaterialPropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~MaterialPropertyValues.md)  
[IPartDoc::MaterialUserName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~MaterialUserName.md)
