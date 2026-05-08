# GetAdvancedSelection Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetAdvancedSelection`

Gets the advanced component selection criteria object for this assembly.
Gets the advanced component selection criteria object for this assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetAdvancedSelection() As AdvancedSelectionCriteria
```

```

Dim instance As IAssemblyDoc
Dim value As AdvancedSelectionCriteria
 
value = instance.GetAdvancedSelection()
```

```

AdvancedSelectionCriteria GetAdvancedSelection()
```

```

AdvancedSelectionCriteria^ GetAdvancedSelection(); 
```

#### Return Value

[IAdvancedSelectionCriteria](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria.md)

Remarks

For more information, see the **Assemblies > Basic Component Operations > Selecting Components > Advanced Component Selection** topic in the SOLIDWORKS user-interface help.

Example

See the [IAdvancedSelectionCriteria](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)
