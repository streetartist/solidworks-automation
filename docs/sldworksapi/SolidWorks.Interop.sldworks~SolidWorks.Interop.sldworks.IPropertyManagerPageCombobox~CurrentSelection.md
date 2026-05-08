# CurrentSelection Property (IPropertyManagerPageCombobox)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCombobox~CurrentSelection`

Gets and sets the item that is currently selected for this combo box.
Gets and sets the item that is currently selected for this combo box.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CurrentSelection As System.Short
```

```

Dim instance As IPropertyManagerPageCombobox
Dim value As System.Short
 
instance.CurrentSelection = value
 
value = instance.CurrentSelection
```

```

System.short CurrentSelection {get; set;}
```

```

property System.short CurrentSelection {
   System.short get();
   void set (    System.short value);
}
```

#### Property Value

Index number of the currently selected item in the 0-based list of items

Example

See the [IPropertyManagerPageCombobox](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCombobox.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageCombobox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCombobox.md)  
[IPropertyManagerPageCombobox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCombobox_members.md)
