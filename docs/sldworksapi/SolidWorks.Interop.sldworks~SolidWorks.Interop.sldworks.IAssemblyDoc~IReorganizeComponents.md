# IReorganizeComponents Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IReorganizeComponents`

Reorganizes an assembly's structure by moving the selected components to the selected assembly or sub-assembly.
Reorganizes an assembly's structure by moving the selected components to the selected assembly or sub-assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IReorganizeComponents( _
   ByVal Count As System.Integer, _
   ByRef Source As Component2, _
   ByVal Target As System.Object _
) As System.Boolean
```

```

Dim instance As IAssemblyDoc
Dim Count As System.Integer
Dim Source As Component2
Dim Target As System.Object
Dim value As System.Boolean
 
value = instance.IReorganizeComponents(Count, Source, Target)
```

```

System.bool IReorganizeComponents( 
   System.int Count,
   ref Component2 Source,
   System.object Target
)
```

```

System.bool IReorganizeComponents( 
   System.int Count,
   Component2^% Source,
   System.Object^ Target
) 
```

#### Parameters

*Count*
:   Number of components to reorganize

*Source*
:   Array of selected components to more; all of the components must be at the same level in one parent assembly

*Target*
:   Where to move the components, which can be a top-level assembly or sub-assembly anywhere at any level of the hierarchy

#### Return Value

True if the selected components were moved to the selected assembly or sub-assembly, false if not

Remarks

See the SOLIDWORKS Help for more information about reorganizing components.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::ReorganizeComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ReorganizeComponents.md)  
[IAssemblyDoc::ReorderComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ReorderComponents.md)  
[DAssemblyDocEvents\_ComponentReorganizeNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ComponentReorganizeNotifyEventHandler.md)
