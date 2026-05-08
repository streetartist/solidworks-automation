# GroupComponentInstances Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~GroupComponentInstances`

Gets or sets whether to group the same components in the same configuration in an assembly into a folder in the FeatureManager design tree.
Gets or sets whether to group the same components in the same configuration in an assembly into a folder in the FeatureManager design tree.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property GroupComponentInstances As System.Boolean
```

```

Dim instance As IFeatureManager
Dim value As System.Boolean
 
instance.GroupComponentInstances = value
 
value = instance.GroupComponentInstances
```

```

System.bool GroupComponentInstances {get; set;}
```

```

property System.bool GroupComponentInstances {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to group the same components in the same configuration in an assembly into a folder in the FeatureManager design tree, false to ungroup them

Example

[Group and Ungroup Components (C#)](Group_Components_Example_CSharp.htm)  
[Group and Ungroup Components (VB.NET)](Group_Components_Example_VBNET.htm)  
[Group and Ungroup Components (VBA)](Group_Components_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IAssemblyDoc::UngroupComponents Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~UngroupComponents.md)  
[IAssemblyDoc::ReorderComponents Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ReorderComponents.md)  
[IAssemblyDoc::ReorganizeComponents Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ReorganizeComponents.md)
