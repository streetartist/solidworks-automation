# GetSelectedItems Method (IPropertyManagerPageSelectionbox)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~GetSelectedItems`

Gets the items selected in a PropertyManager selection box.
Gets the items selected in a PropertyManager selection box.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSelectedItems() As System.Object
```

```

Dim instance As IPropertyManagerPageSelectionbox
Dim value As System.Object
 
value = instance.GetSelectedItems()
```

```

System.object GetSelectedItems()
```

```

System.Object^ GetSelectedItems(); 
```

#### Return Value

Array of shorts of the indices of the currently selected items

Remarks

Each item is a 0-based index into the list of items. For example, if there are five (5) items in the selection box and the first and last items are selected, then this method will return an array containing 0, 4.

Before calling this method, call [IPropertyManagerPageSelectionbox::Style](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox~Style.md) and set the style to swPropMgrPageSelectionBoxStyle\_MultipleItemSelect to enable multiple selections.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageSelectionbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox.md)  
[IPropertyManagerPageSelectionbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox_members.md)  
[IPropertyManagerPageSelectionbox::IGetSelectedItems Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~IGetSelectedItems.md)  
[IPropertyManagerPageSelectionbox::GetSelectedItemsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~GetSelectedItemsCount.md)  
[IPropertyManagerPageSelectionbox::SetSelectedItem Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~SetSelectedItem.md)  
[IPropertyManagerPageSelectionbox::Style Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~Style.md)
