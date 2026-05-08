# IsCheckable Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageBitmapButton~IsCheckable`

Gets whether the bitmap button is clickable.
Gets whether the bitmap button is clickable.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property IsCheckable As System.Boolean
```

```

Dim instance As IPropertyManagerPageBitmapButton
Dim value As System.Boolean
 
instance.IsCheckable = value
 
value = instance.IsCheckable
```

```

System.bool IsCheckable {get; set;}
```

```

property System.bool IsCheckable {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if bitmap button is clickable, false if not

Remarks

This property is only meaningful and used by the SOLIDWORKS application when the bitmap button control is of type swControlType\_CheckableBitmapButton.

You can create a bitmap button control using either of these methods:

- [IPropertyManagerPage2::AddControl](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~AddControl.md) or [IPropertyManagerPage2::IAddControl](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~IAddControl.md)
- [IPropertyManagerPageGroup::AddControl](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageGroup~AddControl.md) or [IPropertyManagerPageGroup::IAddControl](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageGroup~IAddControl.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageBitmapButton Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageBitmapButton.md)  
[IPropertyManagerPageBitmapButton Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageBitmapButton_members.md)  
[IPropertyManagerPageBitmapButton::Checked Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageBitmapButton~Checked.md)
