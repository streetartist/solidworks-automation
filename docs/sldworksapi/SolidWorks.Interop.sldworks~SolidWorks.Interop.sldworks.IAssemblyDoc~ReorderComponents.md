# ReorderComponents Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ReorderComponents`

Moves components to a different location in the FeatureManager design tree.
Moves components to a different location in the FeatureManager design tree.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ReorderComponents( _
   ByVal Source As System.Object, _
   ByVal Target As System.Object, _
   ByVal Where As System.Integer _
) As System.Boolean
```

```

Dim instance As IAssemblyDoc
Dim Source As System.Object
Dim Target As System.Object
Dim Where As System.Integer
Dim value As System.Boolean
 
value = instance.ReorderComponents(Source, Target, Where)
```

```

System.bool ReorderComponents( 
   System.object Source,
   System.object Target,
   System.int Where
)
```

```

System.bool ReorderComponents( 
   System.Object^ Source,
   System.Object^ Target,
   System.int Where
) 
```

#### Parameters

*Source*
:   Array of [components](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) to move

*Target*
:   Target component or folder to which to move the components

*Where*
:   Where to move the components as defined in [swReorderComponentsWhere\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swReorderComponentsWhere_e.html)

#### Return Value

True if the components are moved, false if not

Remarks

The Source argument contains the components to reorder in the FeatureManager design tree.

The order of the elements in the array will be the order that the components appear after the reorder occurs. The components can only be moved within the same component of the model; you cannot move a component from a subassembly into the top-level assembly.

The Where argument indicates where the Source should be moved relative to the Target as defined by swReorderComponentsWhere\_e. If the target is not a folder feature, then this method takes no action and returns false. Only folders that occur within the components section of the assembly FeatureManager design tree can be used; a folder that is among the body features will not be accepted. If the Where argument is specified as one of the two folder-related values, but the Target is a component, the method uses swReorderCompentsWhere\_e.swReorderComponents\_After.

Example

[Move Assembly Components to New Folder (C#)](Move_Assembly_Components_to_New_Folder_Example_CSharp.htm)  
[Move Assembly Components to New Folder (VB.NET)](Move_Assembly_Components_to_New_Folder_Example_VBNET.htm)  
[Move Assembly Components to New Folder (VBA)](Move_Assembly_Components_to_New_Folder_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::IReorderComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IReorderComponents.md)  
[IFeatureManager::InsertFeatureTreeFolder2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertFeatureTreeFolder2.md)  
[IFeatureManager::GroupComponentInstances Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~GroupComponentInstances.md)  
[IAssemblyDoc::UngroupComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~UngroupComponents.md)  
[IPartDoc::ReorderFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ReorderFeature.md)  
[IModelDocExtension::ReorderFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ReorderFeature.md)
