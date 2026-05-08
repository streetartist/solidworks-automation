# ItemCount Property (IPropertyManagerPageSelectionbox)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~ItemCount`

Gets the number of items currently in this selection box.
Gets the number of items currently in this selection box.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property ItemCount As System.Integer
```

```

Dim instance As IPropertyManagerPageSelectionbox
Dim value As System.Integer
 
value = instance.ItemCount
```

```

System.int ItemCount {get;}
```

```

property System.int ItemCount {
   System.int get();
}
```

#### Property Value

Number of items currently in this selection box

Remarks

Use this property before using [IPropertyManagerPageSelectionBox::SelectionIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~SelectionIndex.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageSelectionbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox.md)  
[IPropertyManagerPageSelectionbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox_members.md)
