# TextColor Property (IPropertyManagerPageControl)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl~TextColor`

Gets or sets color of the text of a label on a PropertyManager page.
Gets or sets color of the text of a label on a PropertyManager page.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TextColor As System.Integer
```

```

Dim instance As IPropertyManagerPageControl
Dim value As System.Integer
 
instance.TextColor = value
 
value = instance.TextColor
```

```

System.int TextColor {get; set;}
```

```

property System.int TextColor {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

RGB color value for the text of a label on a PropertyManager page

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageControl Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl.md)  
[IPropertyManagerPageControl Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl_members.md)
