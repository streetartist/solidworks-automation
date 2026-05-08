# DeleteItem Method (IPropertyManagerPageCombobox)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCombobox~DeleteItem`

Deletes an item from the attached drop-down list of this combo box.
Deletes an item from the attached drop-down list of this combo box.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function DeleteItem( _
   ByVal Item As System.Short _
) As System.Short
```

```

Dim instance As IPropertyManagerPageCombobox
Dim Item As System.Short
Dim value As System.Short
 
value = instance.DeleteItem(Item)
```

```

System.short DeleteItem( 
   System.short Item
)
```

```

System.short DeleteItem( 
   System.short Item
) 
```

#### Parameters

*Item*
:   Index number of the item to delete from the 0-based list of items

#### Return Value

Number of items remaining in the list or -1 if the item is not deleted

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageCombobox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCombobox.md)  
[IPropertyManagerPageCombobox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCombobox_members.md)
