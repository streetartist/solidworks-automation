# Name2 Property (IComponent2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Name2`

Gets or sets the name of the selected component. }}-->
Gets or sets the name of the selected component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Name2 As System.String
```

```

Dim instance As IComponent2
Dim value As System.String
 
instance.Name2 = value
 
value = instance.Name2
```

```

System.string Name2 {get; set;}
```

```

property System.String^ Name2 {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Name of this component

Remarks

This property returns a name that includes an instance number. For example:

Part1-1

indicates that this is the first instance of the Part1 Component2. If you are examining a component that is within a subassembly, then this property returns a name that includes the full hierarchical path of component names. For example:

subAssem1-2/Part1-1

indicates that this component (Part1) is the first instance within the subAssem1 Component2. It also shows that the second instance of subAssem1 is referenced.

If you are setting the name of a component:

- Before executing a name change, this property checks the swExtRefUpdateCompNames setting. If swExtRefUpdateCompNames is true, then the name change fails; if swExtRefUpdateCompNames is false, then the name change succeeds. Use [ISldWorks::GetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserPreferenceToggle.md) to change the swExtRefUpdateCompNames setting. Also, remember that some special characters are reserved by SOLIDWORKS, so be sure to use valid characters in the new name.
- The component must be selected.

Example

[Add Component and Mate (C++)](Add_Component_and_Mate_Example_CPlusPlus_COM.htm)  
[Change Material Properties (VBA)](Change_Material_Properties_Example_VB.htm)  
[Check Interference Using AssemblyDoc::ToolsCheckInterference2 (VBA)](Check_Interference_using_AssemblyDoc_ToolsCheckInterference2_Example_VB.htm)  
[Get Component Names and Types for Inplace Mate (VBA)](Get_Component_Names_and_Types_for_Inplace_Mate_Example_VB.htm)  
[Get Component via Display Dimension (VBA)](Get_Component_Via_Display_Dimension_Example_VB.htm)  
[Traverse Assembly at Component Level (VBA)](Traverse_Assembly_at_Component_Level_Example_VB.htm)  
[Traverse Assembly at Component and Feature Levels Using Recursion (VBA)](Traverse_Assembly_at_Component_and_Feature_Levels_Using_Recursion_Example_VB.htm)  
[Traverse Assembly at Component and Feature Levels Using Recursion (VB.NET)](Traverse_Assembly_at_Component_and_Feature_Levels_Using_Recursion_Example_VBNET.htm)  
[Traverse Assembly at Component and Feature Levels Using Recursion (C#)](Traverse_Assembly_at_Component_and_Feature_Levels_Using_Recursion_Example_CSharp.htm)  
[Change Name of Component (C#)](Change_Name_of_Component_Example_CSharp.htm)  
[Change Name of Component (VB.NET)](Change_Name_of_Component_Example_VBNET.htm)  
[Change Name of Component (VBA)](Change_Name_of_Component_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IComponent2::GetSelectByIDString Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetSelectByIDString.md)  
[IAssemblyDoc::GetComponentByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetComponentByName.md)  
[IAssemblyDoc::GetUnloadedComponentNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetUnloadedComponentNames.md)
