# CurrentSelection Property (IPropertyManagerPageNumberbox)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox~CurrentSelection`

Gets or sets the item that is currently selected in the number box.
Gets or sets the item that is currently selected in the number box.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CurrentSelection As System.Short
```

```

Dim instance As IPropertyManagerPageNumberbox
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

Index number of the item in the 0-based list of items

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageNumberbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox.md)  
[IPropertyManagerPageNumberbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox_members.md)
