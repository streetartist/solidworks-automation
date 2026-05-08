# ItemText Property (IPropertyManagerPageListbox)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox~ItemText`

Gets the text for the specified item in this list box.
Gets the text for the specified item in this list box.

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

Dim instance As IPropertyManagerPageListbox
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
:   Position of the item where to get the text in the 0-based list or -1 to get the text of the currently selected item

#### Property Value

Text for the specified item

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageListbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox.md)  
[IPropertyManagerPageListbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox_members.md)
