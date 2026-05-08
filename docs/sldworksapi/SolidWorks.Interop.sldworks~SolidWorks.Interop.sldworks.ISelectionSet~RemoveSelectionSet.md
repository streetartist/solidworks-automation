# RemoveSelectionSet Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSet~RemoveSelectionSet`

Deletes this selection set from the Selection Sets folder.
Deletes this selection set from the [Selection Sets folder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSetFolder.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function RemoveSelectionSet() As System.Boolean
```

```

Dim instance As ISelectionSet
Dim value As System.Boolean
 
value = instance.RemoveSelectionSet()
```

```

System.bool RemoveSelectionSet()
```

```

System.bool RemoveSelectionSet(); 
```

#### Return Value

True if this selection set is deleted from the Selection Sets folder, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISelectionSet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSet.md)  
[ISelectionSet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSet_members.md)  
[IModelDocExtension::SaveSelection Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SaveSelection.md)
