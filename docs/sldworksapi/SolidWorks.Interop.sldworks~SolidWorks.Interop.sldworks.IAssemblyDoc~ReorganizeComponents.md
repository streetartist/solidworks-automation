# ReorganizeComponents Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ReorganizeComponents`

Reorganizes an assembly's structure by moving the selected components to the selected assembly or sub-assembly.
Reorganizes an assembly's structure by moving the selected components to the selected assembly or sub-assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ReorganizeComponents( _
   ByVal Source As System.Object, _
   ByVal Target As System.Object _
) As System.Boolean
```

```

Dim instance As IAssemblyDoc
Dim Source As System.Object
Dim Target As System.Object
Dim value As System.Boolean
 
value = instance.ReorganizeComponents(Source, Target)
```

```

System.bool ReorganizeComponents( 
   System.object Source,
   System.object Target
)
```

```

System.bool ReorganizeComponents( 
   System.Object^ Source,
   System.Object^ Target
) 
```

#### Parameters

*Source*
:   Array of selected [components](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) to more; all of the components must be at the same level in one parent assembly

*Target*
:   Where to move the components, which can be a top-level assembly or sub-assembly anywhere at any level of the hierarchy

#### Return Value

True if the selected components were moved to the selected assembly or sub-assembly, false if not

Remarks

See SOLIDWORKS Help for more information about reorganizing components and restructuring assemblies.

Example

[Reorganize Components (VBA)](Reorganize_Components_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::IReorganizeComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IReorganizeComponents.md)  
[IAssemblyDoc::ReorderComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ReorderComponents.md)  
[DAssemblyDocEvents\_ComponentReorganizeNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ComponentReorganizeNotifyEventHandler.md)  
[IFeatureManager::GroupComponentInstances Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~GroupComponentInstances.md)  
[IAssemblyDoc::UngroupComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~UngroupComponents.md)
