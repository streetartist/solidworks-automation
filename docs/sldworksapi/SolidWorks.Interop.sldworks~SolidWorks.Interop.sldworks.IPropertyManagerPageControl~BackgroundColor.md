# BackgroundColor Property (IPropertyManagerPageControl)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl~BackgroundColor`

Gets or sets the background color of an edit box or label on the PropertyManager page.
Gets or sets the background color of an edit box or label on the PropertyManager page.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property BackgroundColor As System.Integer
```

```

Dim instance As IPropertyManagerPageControl
Dim value As System.Integer
 
instance.BackgroundColor = value
 
value = instance.BackgroundColor
```

```

System.int BackgroundColor {get; set;}
```

```

property System.int BackgroundColor {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

RGB value for the color of an edit box, a list box, or a label on the PropertyManager page

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageControl Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl.md)  
[IPropertyManagerPageControl Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl_members.md)
