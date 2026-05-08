# Height Property (IPropertyManagerPageCombobox)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCombobox~Height`

Gets and sets the maximum height of the attached drop-down combo box.
Gets and sets the maximum height of the attached drop-down combo box.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Height As System.Short
```

```

Dim instance As IPropertyManagerPageCombobox
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

Maximum drop-down height

Remarks

Only use this method to set properties on the PropertyManager page before it is displayed or while it is closed. See [IPropertyManagerPage2::Show2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~Show2.md) and [IPropertyManagerPage2::Close](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~Close.md).

The height is in dialog-box units. You can convert these values to screen units (pixels) by using the MapDialogRect function.

Example

See the [IPropertyManagerPageCombobox](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCombobox.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageCombobox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCombobox.md)  
[IPropertyManagerPageCombobox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCombobox_members.md)
