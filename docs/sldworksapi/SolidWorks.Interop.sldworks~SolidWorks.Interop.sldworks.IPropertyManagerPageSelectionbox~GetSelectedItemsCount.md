# GetSelectedItemsCount Method (IPropertyManagerPageSelectionbox)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~GetSelectedItemsCount`

Gets the number of currently selected items in this PropertyManager selection box.
Gets the number of currently selected items in this PropertyManager selection box.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSelectedItemsCount() As System.Integer
```

```

Dim instance As IPropertyManagerPageSelectionbox
Dim value As System.Integer
 
value = instance.GetSelectedItemsCount()
```

```

System.int GetSelectedItemsCount()
```

```

System.int GetSelectedItemsCount(); 
```

#### Return Value

Number of currently selected items

Remarks

Before calling:

- this method, call [IPropertyManagerPageSelectionbox::Style](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~Style.md) and set the style to swPropMgrPageSelectionBoxStyle\_MultipleItemSelect to enable multiple selections.
- [IPropertyManagerPageSelectionbox::IGetSelectedItems](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~IGetSelectedItems.md), call this method to get the size of the array for that method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageSelectionbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox.md)  
[IPropertyManagerPageSelectionbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox_members.md)  
[IPropertyManagerPageSelectionbox::GetSelectedItems Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~GetSelectedItems.md)  
[IPropertyManagerPageSelectionbox::SetSelectedItem Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~SetSelectedItem.md)
