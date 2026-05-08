# GetSelectionSetItems Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSet~GetSelectionSetItems`

Gets the selection set items in this selection set.
Gets the selection set items in this selection set.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSelectionSetItems() As System.Object
```

```

Dim instance As ISelectionSet
Dim value As System.Object
 
value = instance.GetSelectionSetItems()
```

```

System.object GetSelectionSetItems()
```

```

System.Object^ GetSelectionSetItems(); 
```

#### Return Value

Array of [selection set items](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSetItem.md)

Remarks

To get the types of entities in the selection set, call [ISelectionSet::GetSelectionSetItemTypes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSet~GetSelectionSetItemTypes.md).

Example

[Create and Delete Selection Sets (C#)](Create_and_Delete_Selection_Sets_Example_CSharp.htm)  
[Create and Delete Selection Sets (VB.NET)](Create_and_Delete_Selection_Sets_Example_VBNET.htm)  
[Create and Delete Selection Sets (VBA)](Create_and_Delete_Selection_Sets_Example_VB.htm)  
[Get Dispatch Objects for Selection Set Items (C#)](Get_Dispatch_Objects_for_Selection_Set_Items_Example_CSharp.htm)  
[Get Dispatch Objects for Selection Set Items (VB.NET)](Get_Dispatch_Objects_for_Selection_Set_Items_Example_VBNET.htm)  
[Get Dispatch Objects for Selection Set Items (VBA)](Get_Dispatch_Objects_for_Selection_Set_Items_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISelectionSet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSet.md)  
[ISelectionSet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSet_members.md)
