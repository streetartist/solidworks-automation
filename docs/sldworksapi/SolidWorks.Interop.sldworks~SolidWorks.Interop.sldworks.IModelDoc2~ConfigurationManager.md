# ConfigurationManager Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ConfigurationManager`

Gets the IConfigurationManager object, which allows access to a configuration in a model.
Gets the [IConfigurationManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.md) object, which allows access to a configuration in a model.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property ConfigurationManager As ConfigurationManager
```

```

Dim instance As IModelDoc2
Dim value As ConfigurationManager
 
value = instance.ConfigurationManager
```

```

ConfigurationManager ConfigurationManager {get;}
```

```

property ConfigurationManager^ ConfigurationManager {
   ConfigurationManager^ get();
}
```

#### Property Value

[IConfigurationManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.md) object

Example

[Get Configuration Parameters (C++)](Get_Configuration_Parameters_Example_CPlusPlus_COM.htm)  
[Add Derived Configurations (VBA)](Add_Derived_Configurations_Example_VB.htm)  
[Extract Configuration-specific Parameters (VBA)](Extract_Configuration-Specific_Parameters_Example_VB.htm)  
[Get Dimension Values in All Configurations (VBA)](Get_Dimension_Values_in_All_Configurations_Example_VB.htm)  
[Get Display Dimensions, GTols, and Surface-finish Symbols (VBA)](Get_Display_Dimensions,_Gtols,_and_Surface-Finish_Symbols_Example_VB.htm)  
[Get Names of Bodies in Multibody Part (VBA)](Get_Names_of_Bodies_in_MultiBody_Part_Example_VB.htm)  
[Select Bodies (VBA)](Select_Bodies_Example_VB.htm)  
[Set All Assembly Components Lightweight or Resolved (VBA)](Set_All_Assembly_Components_Lightweight_or_Resolved_Example_VB.htm)  
[Traverse Assembly at Component and Feature Levels Using Recursion (VBA)](Traverse_Assembly_at_Component_and_Feature_Levels_Using_Recursion_Example_VB.htm)  
[Traverse Assembly at Component and Feature Levels Using Recursion (VB.NET)](Traverse_Assembly_at_Component_and_Feature_Levels_Using_Recursion_Example_VBNET.htm)  
[Traverse Assembly at Component and Feature Levels Using Recursion (C#)](Traverse_Assembly_at_Component_and_Feature_Levels_Using_Recursion_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)
