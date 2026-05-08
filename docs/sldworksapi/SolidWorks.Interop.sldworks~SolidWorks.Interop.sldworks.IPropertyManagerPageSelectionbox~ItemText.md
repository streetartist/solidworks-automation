# ItemText Property (IPropertyManagerPageSelectionbox)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~ItemText`

Gets the specified item in this selection box.
Gets the specified item in this selection box.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property ItemText( _
   ByVal Item As System.Short _
) As System.String
```

```

Dim instance As IPropertyManagerPageSelectionbox
Dim Item As System.Short
Dim value As System.String
 
value = instance.ItemText(Item)
```

```

System.string ItemText( 
   System.short Item
) {get;}
```

```

property System.String^ ItemText {
   System.String^ get(System.short Item);
}
```

#### Parameters

*Item*
:   Position of the item in the 0-based list; -1 to get the currently selected item

#### Property Value

Text of the specified item

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageSelectionbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox.md)  
[IPropertyManagerPageSelectionbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox_members.md)
