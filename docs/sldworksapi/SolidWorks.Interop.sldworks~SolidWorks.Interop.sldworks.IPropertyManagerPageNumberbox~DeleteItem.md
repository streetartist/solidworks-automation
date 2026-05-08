# DeleteItem Method (IPropertyManagerPageNumberbox)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox~DeleteItem`

Deletes an item from the attached drop-down list for this number box.
Deletes an item from the attached drop-down list for this number box.

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

Dim instance As IPropertyManagerPageNumberbox
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

[IPropertyManagerPageNumberbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox.md)  
[IPropertyManagerPageNumberbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox_members.md)
