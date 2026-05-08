# CurrentSelection Property (IPropertyManagerPageListbox)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox~CurrentSelection`

Gets and sets the item that is currently selected in this list box.
Gets and sets the item that is currently selected in this list box.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CurrentSelection As System.Short
```

```

Dim instance As IPropertyManagerPageListbox
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

Index number of the item in the 0-based list

Remarks

If you use this property with a list box enabled for [multiple selections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox~Style.md), then this method returns -1 and does not affect the list box.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageListbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox.md)  
[IPropertyManagerPageListbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox_members.md)
