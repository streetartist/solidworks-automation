# GetHiddenUnloadedChildrenCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetHiddenUnloadedChildrenCount`

Gets the number of hidden children components of this component that were not loaded when an assembly was opened selectively.
Gets the number of hidden children components of this component that were not loaded when an assembly was [opened selectively](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~Selective.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetHiddenUnloadedChildrenCount() As System.Integer
```

```

Dim instance As IComponent2
Dim value As System.Integer
 
value = instance.GetHiddenUnloadedChildrenCount()
```

```

System.int GetHiddenUnloadedChildrenCount()
```

```

System.int GetHiddenUnloadedChildrenCount(); 
```

#### Return Value

Number of hidden children components of this component that were not loaded when an assembly was opened selectively

Remarks

You can open an assembly with all components hidden except those that you select. The selected components are loaded lightweight. All other components become hidden and are not loaded into memory. This method returns the number of unloaded hidden children of this component. This method does not return the number of suppressed unloaded children components. Call [IComponent2::GetUnloadedComponentNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetUnloadedComponentNames.md) for that type of related information.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[ITreeControlItem Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem.md)  
[IComponent2::HasUnloadedComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~HasUnloadedComponents.md)
