# Caption Property (IPropertyManagerPageGroup)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageGroup~Caption`

Gets or sets the title for this group box.
Gets or sets the title for this group box.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Caption As System.String
```

```

Dim instance As IPropertyManagerPageGroup
Dim value As System.String
 
instance.Caption = value
 
value = instance.Caption
```

```

System.string Caption {get; set;}
```

```

property System.String^ Caption {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Text for the title for this group box

Remarks

See [IPropertyManagerPage2::AddGroupBox](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~AddGroupBox.md) or [IPropertyManagerPage2::IAddGroupBox](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~IAddGroupBox.md) to add a group box.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageGroup.md)  
[IPropertyManagerPageGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageGroup_members.md)
