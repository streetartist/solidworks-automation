# SaveSelection Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SaveSelection`

Creates a new selection set containing the selected entities.
Creates a new selection set containing the selected entities.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SaveSelection( _
   ByRef Status As System.Integer _
) As System.Object
```

```

Dim instance As IModelDocExtension
Dim Status As System.Integer
Dim value As System.Object
 
value = instance.SaveSelection(Status)
```

```

System.object SaveSelection( 
   out System.int Status
)
```

```

System.Object^ SaveSelection( 
   [Out] System.int Status
) 
```

#### Parameters

*Status*
:   1 if a selection set is created, 0 if not

#### Return Value

[Selection set](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSet.md)

Example

[Create and Delete Selection Sets (C#)](Create_and_Delete_Selection_Sets_Example_CSharp.htm)  
[Create and Delete Selection Sets (VB.NET)](Create_and_Delete_Selection_Sets_Example_VBNET.htm)  
[Create and Delete Selection Sets (VBA)](Create_and_Delete_Selection_Sets_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[ISelectionSetFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSetFolder.md)  
[ISelectionSetItem Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSetItem.md)  
[ISelectionSet::RemoveSelectionSet Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSet~RemoveSelectionSet.md)
