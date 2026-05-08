# CurrentSelection Property (IPropertyManagerPageSelectionbox)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~CurrentSelection`

Gets or sets the index number of the currently selected item in this selection box.
Gets or sets the index number of the currently selected item in this selection box.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CurrentSelection As System.Integer
```

```

Dim instance As IPropertyManagerPageSelectionbox
Dim value As System.Integer
 
instance.CurrentSelection = value
 
value = instance.CurrentSelection
```

```

System.int CurrentSelection {get; set;}
```

```

property System.int CurrentSelection {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

0-based index of the currently selected item in this selection box

Remarks

The return value Item is the item in the selection box that is selected. Only the active selection box can have a current selection. If you use this property with an inactive selection box, -1 is returned. See [IPropertyManagerPageSelectionbox::GetSelectionFocus](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~GetSelectionFocus.md) to determine if a selection box is active or not.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageSelectionbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox.md)  
[IPropertyManagerPageSelectionbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox_members.md)
