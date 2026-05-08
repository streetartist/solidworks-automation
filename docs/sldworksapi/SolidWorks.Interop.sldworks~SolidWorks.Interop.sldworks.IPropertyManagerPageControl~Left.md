# Left Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl~Left`

Gets or sets the left edge of the control on a PropertyManager page.
Gets or sets the left edge of the control on a PropertyManager page.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Left As System.Short
```

```

Dim instance As IPropertyManagerPageControl
Dim value As System.Short
 
instance.Left = value
 
value = instance.Left
```

```

System.short Left {get; set;}
```

```

property System.short Left {
   System.short get();
   void set (    System.short value);
}
```

#### Property Value

Left edge of the control

Remarks

This property must be set before the control is displayed.

If you do not specify the position and size of the controls on the PropertyManager page, the controls are created using a default size and placed in a computed default position so that your page matches the look-and-feel of a SOLIDWORKS PropertyManager page. This is generally the best way to go, whenever possible. However, while there are no limitations on how you create the layout of your page, it is recommended that you only use this method if you want to place controls on the page.

By default, the left edge of a control is either the left edge of its group box or indented a certain distance. This is determined by the LeftAlign argument of the [IPropertyManagerPage2::AddControl](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~AddControl.md) or [IPropertyManagerPage2::IAddControl](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~IAddControl.md) method. Using IPropertyManagerPage2::AddControl  or IPropertyManagerPage2::IAddControl overrides that default. The value is in dialog units relative to the group box that the control is in. The left edge of the group box is 0; the right edge of the group box is 100.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageControl Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl.md)  
[IPropertyManagerPageControl Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl_members.md)
