# HorizontalJustification Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~HorizontalJustification`

Gets or sets the dimension text's horizontal justification.
Gets or sets the dimension text's horizontal justification.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property HorizontalJustification As System.Integer
```

```

Dim instance As IDisplayDimension
Dim value As System.Integer
 
instance.HorizontalJustification = value
 
value = instance.HorizontalJustification
```

```

System.int HorizontalJustification {get; set;}
```

```

property System.int HorizontalJustification {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Horizontal justification as defined in [swTextJustification\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTextJustification_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::VerticalJustification Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~VerticalJustification.md)  
[IDisplayDimension::AddDisplayText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~AddDisplayText.md)  
[IDisplayDimension::IAddDisplayText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~IAddDisplayText.md)
