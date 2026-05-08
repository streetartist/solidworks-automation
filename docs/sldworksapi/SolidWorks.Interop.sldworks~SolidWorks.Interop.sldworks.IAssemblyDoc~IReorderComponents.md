# IReorderComponents Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IReorderComponents`

Moves components to a different location in the FeatureManager tree.
Moves components to a different location in the FeatureManager tree.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IReorderComponents( _
   ByVal Count As System.Integer, _
   ByRef Source As Component2, _
   ByVal Target As System.Object, _
   ByVal Where As System.Integer _
) As System.Boolean
```

```

Dim instance As IAssemblyDoc
Dim Count As System.Integer
Dim Source As Component2
Dim Target As System.Object
Dim Where As System.Integer
Dim value As System.Boolean
 
value = instance.IReorderComponents(Count, Source, Target, Where)
```

```

System.bool IReorderComponents( 
   System.int Count,
   ref Component2 Source,
   System.object Target,
   System.int Where
)
```

```

System.bool IReorderComponents( 
   System.int Count,
   Component2^% Source,
   System.Object^ Target,
   System.int Where
) 
```

#### Parameters

*Count*
:   Number of items in the Source array

*Source*
:   Array of the [components](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) to move

*Target*
:   Target component or folder feature to which to move the components

*Where*
:   Where to move the components as defined in [swReorderComponentsWhere\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swReorderComponentsWhere_e.html)

#### Return Value

True if the components were moved, false if not

Remarks

The Source argument contains the components to reorder in the FeatureManager tree.

The order of the items in the array will be the order that the components appear after the reorder occurs. The components can only be moved within the same component of the model; you cannot move a component from a subassembly into the top level assembly.

The Where argument indicates where the Source should be moved relative to the Target as defined by [swReorderComponentsWhere\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swReorderComponentsWhere_e.html). If the target is a feature, but not a folder feature, this method takes no action and returns false. Only folders that occur within the components section of the Assembly FeatureManager tree can be used; a folder that is among the body features will not be accepted. If the Where argument is specified as one of the two folder-related values, but the Target is a component, the method uses swReorderComponents\_After.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::ReorderComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ReorderComponents.md)  
[IPartDoc::ReorderFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ReorderFeature.md)
