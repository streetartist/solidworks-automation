# IGetSelectedItems Method (IPropertyManagerPageListbox)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox~IGetSelectedItems`

Gets the items selected in a list box enabled for multiple selections.
Gets the items selected in a list box enabled for multiple selections.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetSelectedItems( _
   ByVal Count As System.Integer _
) As System.Short
```

```

Dim instance As IPropertyManagerPageListbox
Dim Count As System.Integer
Dim value As System.Short
 
value = instance.IGetSelectedItems(Count)
```

```

System.short IGetSelectedItems( 
   System.int Count
)
```

```

System.short IGetSelectedItems( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of selected items

#### Return Value

- in-process, unmanaged C++: Pointer to an array of shorts of the currently selected items in this list box

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Each item is a 0-based index into the list of items.

Call [IPropertyManagerPageListbox::GetSelectedItemsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox~GetSelectedItemsCount.md) to size the returned array.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageListbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox.md)  
[IPropertyManagerPageListbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox_members.md)  
[IPropertyManagerPageListbox::GetSelectedItems Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox~GetSelectedItems.md)
