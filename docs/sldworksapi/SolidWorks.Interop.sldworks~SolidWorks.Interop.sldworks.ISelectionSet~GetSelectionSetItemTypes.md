# GetSelectionSetItemTypes Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSet~GetSelectionSetItemTypes`

Gets the types of entities in this selection set.
Gets the types of entities in this selection set.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSelectionSetItemTypes() As System.Object
```

```

Dim instance As ISelectionSet
Dim value As System.Object
 
value = instance.GetSelectionSetItemTypes()
```

```

System.object GetSelectionSetItemTypes()
```

```

System.Object^ GetSelectionSetItemTypes(); 
```

#### Return Value

Array of longs or integers of the types of entities in this selection set as defined in [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSelectType_e.html) (see **Remarks**)

Remarks

The order of the array of the types of entities returned by this method matches the order of the array of selection set items returned by [ISelectionSet::GetSelectionSetItems](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSet~GetSelectionSetItems.md).

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
[ISelectionSetItem::GetCorrespondingItem Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSetItem~GetCorrespondingItem.md)
