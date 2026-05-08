# IGetSelectedItems Method (IPropertyManagerPageSelectionbox)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~IGetSelectedItems`

Gets the items selected in a PropertyManager selection box.
Gets the items selected in a PropertyManager selection box.

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

Dim instance As IPropertyManagerPageSelectionbox
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
:   Number of items selected

#### Return Value

- in-process, unmanaged C++: Pointer to an array of shorts of the indices of the currently selected items

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Each item is a 0-based index into the list of items. For example, if there are five (5) items in the selection box and the first and last items are selected, then this method will return an array containing 0, 4.

Before calling:

- this method, call [IPropertyManagerPageSelectionbox::Style](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox~Style.md) and set the style to swPropMgrPageSelectionBoxStyle\_MultipleItemSelect to enable multiple selections.
- [IPropertyManagerPageSelectionbox::GetSelectedItemsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~GetSelectedItemsCount.md) to ge the value of Count.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageSelectionbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox.md)  
[IPropertyManagerPageSelectionbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox_members.md)
