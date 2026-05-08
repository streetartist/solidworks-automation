# Width Property (IPropertyManagerPageControl)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl~Width`

Gets or sets the width of the control on a PropertyManager page.
Gets or sets the width of the control on a PropertyManager page.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Width As System.Short
```

```

Dim instance As IPropertyManagerPageControl
Dim value As System.Short
 
instance.Width = value
 
value = instance.Width
```

```

System.short Width {get; set;}
```

```

property System.short Width {
   System.short get();
   void set (    System.short value);
}
```

#### Property Value

Width of the control

Remarks

This property must be set before the control is displayed.

If you do not specify the position and size of the controls on the PropertyManager page, the controls are created using a default size and placed in a computed default position so that your page matches the look-and-feel of a SOLIDWORKS page. This is generally the best way to go, whenever possible. However, while there are no limitations on how you create the layout of your page, it is recommended that you only use this API if you want to explicitly place controls on the page.

By default, the width of the control is usually set so that it extends to the right edge of its group box. Using this API overrides that default. The value is in dialog units relative to the group box that the control is in. The width of the group box is 100.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageControl Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl.md)  
[IPropertyManagerPageControl Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl_members.md)
