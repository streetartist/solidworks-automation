# UngroupComponents Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~UngroupComponents`

Ungroups the grouped components in the selected folder in the FeatureManager design tree.
Ungroups the grouped components in the selected folder in the FeatureManager design tree.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function UngroupComponents() As System.Boolean
```

```

Dim instance As IAssemblyDoc
Dim value As System.Boolean
 
value = instance.UngroupComponents()
```

```

System.bool UngroupComponents()
```

```

System.bool UngroupComponents(); 
```

#### Return Value

True if the grouped components in the selected folder in the FeatureManager design tree are ungrouped, false if not

Example

[Group and Ungroup Components (C#)](Group_Components_Example_CSharp.htm)  
[Group and Ungroup Components (VB.NET)](Group_Components_Example_VBNET.htm)  
[Group and Ungroup Components (VBA)](Group_Components_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IFeatureManager::GroupComponentInstances Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~GroupComponentInstances.md)  
[IAssemblyDoc::ReorderComponents Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ReorderComponents.md)  
[IAssemblyDoc::ReorganizeComponents Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ReorganizeComponents.md)
