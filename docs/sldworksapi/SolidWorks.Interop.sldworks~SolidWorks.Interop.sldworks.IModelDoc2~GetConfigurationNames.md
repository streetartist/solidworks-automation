# GetConfigurationNames Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetConfigurationNames`

Gets the names of the configurations in this document.
Gets the names of the configurations in this document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetConfigurationNames() As System.Object
```

```

Dim instance As IModelDoc2
Dim value As System.Object
 
value = instance.GetConfigurationNames()
```

```

System.object GetConfigurationNames()
```

```

System.Object^ GetConfigurationNames(); 
```

#### Return Value

Array of the names of the configurations in the order they are created in this document

Example

[Extract Configuration-specific Parameters (VBA)](Extract_Configuration-Specific_Parameters_Example_VB.htm)  
[Get Custom Properties (VBA)](Get_Custom_Properties_Example_VB.htm)  
[Get Dimension Values in All Configurations (VBA)](Get_Dimension_Values_in_All_Configurations_Example_VB.htm)  
[Iterate Through All Configurations (VBA)](Iterate_Through_All_Configurations_Example_VB.htm)  
[List Custom Properties (VBA)](List_Custom_Properties_Example_VB.htm)  
[Rebuild All Configurations (VBA)](Rebuild_All_Configurations_Example_VB.htm)  
[Remove Material Properties from Assembly Component (VBA)](Remove_Material_Properties_from_Assembly_Component_Example_VB.htm)  
[Save Configuration Data (C#)](Save_Configuration_Data_Example_CSharp.htm)  
[Save Configuration Data (VB.NET)](Save_Configuration_Data_Example_VBNET.htm)  
[Save Configuration Data (VBA)](Save_Configuration_Data_Example_VB.htm)  
[Get Names of Configurations Using Variant (C++)](ConfigurationTraversalCPP.htm)  
[Get List of Configurations (C#)](Get_List_Of_Configurations_Example_CSharp.htm)  
[Get List of Configurations (VB.NET)](Get_List_Of_Configurations_Example_VBNET.htm)  
[Get List of Configurations (VBA)](Get_List_Of_Configurations_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::AddConfiguration3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddConfiguration3.md)  
[IModelDoc2::DeleteConfiguration2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeleteConfiguration2.md)  
[IModelDoc2::GetConfigurationCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetConfigurationCount.md)  
[IModelDoc2::GetConfigurationByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetConfigurationByName.md)  
[IModelDoc2::IAddConfiguration3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IAddConfiguration3.md)  
[IModelDoc2::IGetConfigurationByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetConfigurationByName.md)  
[IModelDoc2::IGetConfigurationNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetConfigurationNames.md)  
[IModelDoc2::ShowConfiguration2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ShowConfiguration2.md)  
[IModelDoc2::ConfigurationManager Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ConfigurationManager.md)  
[IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.md)  
[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)
