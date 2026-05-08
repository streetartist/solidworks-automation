# GetSelectedItems Method (IPropertyManagerPageListbox)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox~GetSelectedItems`

Gets the items selected in a list box enabled for multiple selections.
Gets the items selected in a list box enabled for multiple selections.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSelectedItems() As System.Object
```

```

Dim instance As IPropertyManagerPageListbox
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

Array of shorts of the currently selected items in this list box

Remarks

Each item is a 0-based index into the list of items.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageListbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox.md)  
[IPropertyManagerPageListbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox_members.md)  
[IPropertyManagerPageListbox::IGetSelectedItems Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox~IGetSelectedItems.md)  
[IPropertyManagerPageListbox::GetSelectedItemsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox~GetSelectedItemsCount.md)
