# Caption Property (IPropertyManagerPageTab)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageTab~Caption`

Gets or sets the caption for this tab.
Gets or sets the caption for this tab.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Caption As System.String
```

```

Dim instance As IPropertyManagerPageTab
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

Text for tab caption

Remarks

You can reset a tab caption regardless if the PropertyManager page is displayed or hidden.

Use [IPropertyManagerPage2::AddTab](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~AddTab.md) to add any number of tabs to your PropertyManager page.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageTab Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageTab.md)  
[IPropertyManagerPageTab Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageTab_members.md)
