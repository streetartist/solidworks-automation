# InsertItem Method (IPropertyManagerPageNumberbox)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox~InsertItem`

Inserts an item in the attached drop-down list for this number box.
Inserts an item in the attached drop-down list for this number box.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertItem( _
   ByVal Item As System.Short, _
   ByVal Text As System.String _
) As System.Short
```

```

Dim instance As IPropertyManagerPageNumberbox
Dim Item As System.Short
Dim Text As System.String
Dim value As System.Short
 
value = instance.InsertItem(Item, Text)
```

```

System.short InsertItem( 
   System.short Item,
   System.string Text
)
```

```

System.short InsertItem( 
   System.short Item,
   System.String^ Text
) 
```

#### Parameters

*Item*
:   Position where to add the item in the 0-based list or -1 to put the item at the end of the list

*Text*
:   Text for item

#### Return Value

Position in the 0-based list where the item is added or -1 if the item is not added to the list

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageNumberbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox.md)  
[IPropertyManagerPageNumberbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox_members.md)
