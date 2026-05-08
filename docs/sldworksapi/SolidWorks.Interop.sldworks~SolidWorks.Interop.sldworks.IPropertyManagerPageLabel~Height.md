# Height Property (IPropertyManagerPageLabel)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel~Height`

Gets or sets the height of this label.
Gets or sets the height of this label.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Height As System.Short
```

```

Dim instance As IPropertyManagerPageLabel
Dim value As System.Short
 
instance.Height = value
 
value = instance.Height
```

```

System.short Height {get; set;}
```

```

property System.short Height {
   System.short get();
   void set (    System.short value);
}
```

#### Property Value

Height of label in dialog box units; defaults to 8

Remarks

You can only set this property before the PropertyManager page is displayed.

Because SOLIDWORKS sizes the label appropriately based on the text it contains, you should not have to use this property. However, if the label does not contain text, then using this property might be useful.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageLabel Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel.md)  
[IPropertyManagerPageLabel Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel_members.md)
