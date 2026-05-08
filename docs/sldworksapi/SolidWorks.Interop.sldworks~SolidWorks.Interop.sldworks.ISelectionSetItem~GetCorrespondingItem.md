# GetCorrespondingItem Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSetItem~GetCorrespondingItem`

Gets the Dispatch object for this selection set item.
Gets the Dispatch object for this selection set item.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCorrespondingItem() As System.Object
```

```

Dim instance As ISelectionSetItem
Dim value As System.Object
 
value = instance.GetCorrespondingItem()
```

```

System.object GetCorrespondingItem()
```

```

System.Object^ GetCorrespondingItem(); 
```

#### Return Value

Pointer to the Dispatch object for this selection set item (see **Remarks**)

Remarks

You can use this method to:

- pass the Dispatch object to [ISelectionMgr::AddSelectionListObject](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~AddSelectionListObject.md) or [ISelectionMgr::AddSelectionListObjects](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~AddSelectionListObjects.md).
- typecast each element in [an array containing selection set item types](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSet~GetSelectionSetItemTypes.md). See the examples.

Example

[Get Dispatch Objects for Selection Set Items (C#)](Get_Dispatch_Objects_for_Selection_Set_Items_Example_CSharp.htm)  
[Get Dispatch Objects for Selection Set Items (VB.NET)](Get_Dispatch_Objects_for_Selection_Set_Items_Example_VBNET.htm)  
[Get Dispatch Objects for Selection Set Items (VBA)](Get_Dispatch_Objects_for_Selection_Set_Items_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISelectionSetItem Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSetItem.md)  
[ISelectionSetItem Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSetItem_members.md)
