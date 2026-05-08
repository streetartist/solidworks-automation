# GetChildren Method (IComponent2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetChildren`

Gets all of the children components of this component.
Gets all of the children components of this component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetChildren() As System.Object
```

```

Dim instance As IComponent2
Dim value As System.Object
 
value = instance.GetChildren()
```

```

System.object GetChildren()
```

```

System.Object^ GetChildren(); 
```

#### Return Value

Array of [components](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)

Remarks

If this assembly component is a part document, SOLIDWORKS returns NULL. If this assembly component is the root component or a subassembly, then this method returns the child components that belong to the assembly document.

The typical order of calls needed in assembly traversal is:

1. [IConfigurationManager::ActiveConfiguration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ActiveConfiguration.md) (called only once)
2. [IConfiguration::GetRootComponent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetRootComponent.md) (called only once)
3. IComponent2::GetChildren (called recursively)

You must call the IComponent2::GetChildren method recursively because it returns only the immediate (one level) children. It does not get child components of the sub-assemblies. For example, if one of the child components of a component is a sub-assembly that has its own children, those children are not returned by this method. You need to call this method again from that sub-assembly component to get its children.

For a given component, this method returns all of the immediate child components. This includes suppressed, hidden, and lightweight components. Use [IComponent2::Visible](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Visible.md) and [IComponent2::GetSuppression](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetSuppression.md) to detect the component states.

Results of an assembly traversal vary based on the configuration currently displayed in your main assembly and based on the configuration referenced by the subassembly component. The list of child components that this method returns can be different depending on which configuration is referenced by the component (see IConfigurationManager::ActiveConfiguration and [IComponent2::ReferencedConfiguration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ReferencedConfiguration.md)).

For example, if one configuration of your main assembly contains a suppressed subassembly, IComponent2::GetChildren returns an empty array when you call it from that suppressed subassembly component. As another example, a subassembly document (.sldasm file) can contain several configurations, each of which has varying states of suppression for its child components. When inserted into your main assembly, this subassembly  
document can reference any of these configurations. As a result, you might find that the child component suppression states vary based on which configuration is referenced by the subassembly component.

**NOTE:** Components might not be returned in the same order from call to call.

Example

[Get Display Dimensions, GTols, and Surface-finish Symbols (VBA)](Get_Display_Dimensions,_Gtols,_and_Surface-Finish_Symbols_Example_VB.htm)  
[Get Names of Bodies in Multibody Part (VBA)](Get_Names_of_Bodies_in_MultiBody_Part_Example_VB.htm)  
[Get Transforms of Assembly Components (VBA)](Get_Transforms_of_Assembly_Components_Example_VB.htm)  
[Make All Assembly Components Visible (VBA)](Make_All_Assembly_Components_Visible_Example_VB.htm)  
[Traverse Assembly at Component and Feature Levels (VBA)](Traverse_Assembly_at_Component_and_Feature_Level_Example_VB.htm)  
[Traverse Assembly at Component and Feature Levels Using Recursion (VBA)](Traverse_Assembly_at_Component_and_Feature_Levels_Using_Recursion_Example_VB.htm)  
[Traverse Assembly at Component and Feature Levels Using Recursion (VB.NET)](Traverse_Assembly_at_Component_and_Feature_Levels_Using_Recursion_Example_VBNET.htm)  
[Traverse Assembly at Component and Feature Levels Using Recursion (C#)](Traverse_Assembly_at_Component_and_Feature_Levels_Using_Recursion_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[Component2::IGetChildren Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetChildren.md)  
[IAssemblyDoc::GetComponentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetComponentCount.md)  
[IAssemblyDoc::GetComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetComponents.md)  
[IComponent2::GetParent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetParent.md)  
[IConfiguration::GetRootComponent3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetRootComponent3.md)
