# GetSelectedItemsCount Method (IPropertyManagerPageListbox)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox~GetSelectedItemsCount`

Gets the number of items currently selected in a list box enabled for multiple selection.
Gets the number of items currently selected in a list box enabled for multiple selection.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSelectedItemsCount() As System.Integer
```

```

Dim instance As IPropertyManagerPageListbox
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

Number of items currently selected in this list box

Remarks

Call this method before calling [IPropertyManagerPageListbox::IGetSelectedItems](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox~IGetSelectedItems.md) to size the array of selected items.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageListbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox.md)  
[IPropertyManagerPageListbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox_members.md)  
[IPropertyManagerPageListbox::GetSelectedItems Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox~GetSelectedItems.md)
