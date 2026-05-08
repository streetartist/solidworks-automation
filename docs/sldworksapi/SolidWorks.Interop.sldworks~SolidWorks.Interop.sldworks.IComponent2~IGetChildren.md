# IGetChildren Method (IComponent2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetChildren`

Gets all of the children components of this component.
Gets all of the children components of this component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetChildren() As Component2
```

```

Dim instance As IComponent2
Dim value As Component2
 
value = instance.IGetChildren()
```

```

Component2 IGetChildren()
```

```

Component2^ IGetChildren(); 
```

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) objects

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

If this assembly component is a part document, SOLIDWORKS returns NULL. If this assembly component is the root component or a subassembly, then this method returns the child components that belong to the assembly document.

The typical order of calls needed in assembly traversal is:

1. [IConfigurationManager::ActiveConfiguration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ActiveConfiguration.md) (called only once)
2. [IConfiguration::GetRootComponent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetRootComponent.md) (called only once)
3. IComponent2::GetChildren (called recursively)

COM applications should use to [IComponent2::IGetChildrenCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetChildrenCount.md) to determine the number of component children, which is the size of the array required to IComponent2::IGetChildren. Because IComponent2::IGetChildren returns an array, this code must be used in an in-process DLL.

You must call the IComponent2::GetChildren method recursively because it returns only the immediate (one level) children. It does not get child components of the sub-assemblies. For example, if one of the child components of a component is a sub-assembly that has its own children, those children are not returned by this method. You need to call this method again from that sub-assembly component to get its children.

For a given component, this method returns all of the immediate child components. This includes suppressed, hidden, and lightweight components. Use [IComponent2::Visible](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Visible.md) and [IComponent2::GetSuppression](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetSuppression.md) to detect the component states.

Results of an assembly traversal vary based on the configuration currently displayed in your main assembly and based on the configuration referenced by the subassembly component. The list of child components that this method returns can be different depending on which configuration is referenced by the component (see IConfigurationManager::ActiveConfiguration and [IComponent2::ReferencedConfiguration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ReferencedConfiguration.md)).

For example, if one configuration of your main assembly contains a suppressed subassembly, IComponent2::GetChildren returns an empty array when you call it from that suppressed subassembly component. As another example, a subassembly document (.sldasm file) can contain several configurations, each of which has varying states of suppression for its child components. When inserted into your main assembly, this subassembly  
document can reference any of these configurations. As a result, you might find that the child component suppression states vary based on which configuration is referenced by the subassembly component.

**NOTE:** Components might not be returned in the same order from call to call.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IAssemblyDoc::GetComponentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetComponentCount.md)  
[IAssemblyDoc::IGetComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IGetComponents.md)  
[IComponent2::GetParent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetParent.md)  
[IConfigurationManager::ActiveConfiguration Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ActiveConfiguration.md)  
[IConfiguration::IGetRootComponent2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetRootComponent2.md)  
[IConfiguration::GetRootComponent3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetRootComponent3.md)
