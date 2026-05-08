# SelectionIndex Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~SelectionIndex`

Gets the index number of the currently selected item in the selection box.
Gets the index number of the currently selected item in the selection box.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property SelectionIndex( _
   ByVal Item As System.Integer _
) As System.Integer
```

```

Dim instance As IPropertyManagerPageSelectionbox
Dim Item As System.Integer
Dim value As System.Integer
 
value = instance.SelectionIndex(Item)
```

```

System.int SelectionIndex( 
   System.int Item
) {get;}
```

```

property System.int SelectionIndex {
   System.int get(System.int Item);
}
```

#### Parameters

*Item*
:   0-based index number of the currently selected item (see **Remarks**)

#### Property Value

1-based index number to use with [ISelectionMgr](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.md) APIs (see Remarks)

Remarks

Use:

- [IPropertyManagerPageSelectionbox::ItemCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~ItemCount.md) to get the number of items in the selection box.
- the return value Index with such ISelectionMgr APIs as [ISelectionMgr::GetSelectedObject6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject6.md) and [ISelectionMgr::GetSelectedObjectType3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectType3.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageSelectionbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox.md)  
[IPropertyManagerPageSelectionbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox_members.md)
