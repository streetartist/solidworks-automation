# SetSelectedItem Method (IPropertyManagerPageListbox)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox~SetSelectedItem`

Sets whether an item is selected or cleared in a list box enabled for multiple selection.
Sets whether an item is selected or cleared in a list box enabled for multiple selection.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetSelectedItem( _
   ByVal Item As System.Short, _
   ByVal Selected As System.Boolean _
) As System.Boolean
```

```

Dim instance As IPropertyManagerPageListbox
Dim Item As System.Short
Dim Selected As System.Boolean
Dim value As System.Boolean
 
value = instance.SetSelectedItem(Item, Selected)
```

```

System.bool SetSelectedItem( 
   System.short Item,
   System.bool Selected
)
```

```

System.bool SetSelectedItem( 
   System.short Item,
   System.bool Selected
) 
```

#### Parameters

*Item*
:   Index of the item to select or clear

*Selected*
:   True to select the item, false to not

#### Return Value

True if the item was selected or cleared, false if not

Remarks

The value specified for Item must be a valid index number. If it is not, then this method returns false. Thus, set up your list item index before using this method.

If you use this method to set a selected item in a single-selection style list box and another item in the list box is already selected, then that item is automatically cleared. You can use this method to clear a selection in a single-selection style list box, which results in no current selection in that list box.

Example

See the [IPropertyManagerPageListbox](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageListbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox.md)  
[IPropertyManagerPageListbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox_members.md)
