# ShowConfiguration2 Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ShowConfiguration2`

Shows the named configuration by switching to that configuration and making it the active configuration.
Shows the named configuration by switching to that configuration and making it the active configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ShowConfiguration2( _
   ByVal ConfigurationName As System.String _
) As System.Boolean
```

```

Dim instance As IModelDoc2
Dim ConfigurationName As System.String
Dim value As System.Boolean
 
value = instance.ShowConfiguration2(ConfigurationName)
```

```

System.bool ShowConfiguration2( 
   System.string ConfigurationName
)
```

```

System.bool ShowConfiguration2( 
   System.String^ ConfigurationName
) 
```

#### Parameters

*ConfigurationName*
:   Name of the configuration to display

#### Return Value

True if the configuration is activated successfully, false if not

Remarks

Configurations allow you to save certain display characteristics with each of the assembly components. This method allows you to retrieve a previously saved configuration.

If you made changes to the model and the configuration to which you are switching needs to be updated to reflect those changes, then you must rebuild the model using [IModelDoc2::EditRebuild3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRebuild3.md). Otherwise, the FeatureManager design tree will show the model as needing to be rebuilt.

Example

[Get Custom Property Values on Cut List Folders (VBA)](Get_Custom_Property_Values_On_Cut_List_Folders_Example_VB.htm)  
[Iterate Through All Configurations (VBA)](Iterate_Through_All_Configurations_Example_VB.htm)  
[Rebuild All Configurations (VBA)](Rebuild_All_Configurations_Example_VB.htm)  
[Work With Configurations (VBA)](Work_with_Configurations_Example_VB.htm)  
[Save Configuration Data (C#)](Save_Configuration_Data_Example_CSharp.htm)  
[Save Configuration Data (VB.NET)](Save_Configuration_Data_Example_VBNET.htm)  
[Save Configuration Data (VBA)](Save_Configuration_Data_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::EditConfiguration3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditConfiguration3.md)  
[IModelDoc2::AddConfiguration3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddConfiguration3.md)  
[IConfigurationManager::AddConfiguration Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~AddConfiguration.md)
