# VerticalJustification Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~VerticalJustification`

Gets the dimension text's vertical justification.
Gets the dimension text's vertical justification.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property VerticalJustification As System.Integer
```

```

Dim instance As IDisplayDimension
Dim value As System.Integer
 
instance.VerticalJustification = value
 
value = instance.VerticalJustification
```

```

System.int VerticalJustification {get; set;}
```

```

property System.int VerticalJustification {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Vertical justification as defined in [swVerticalJustification\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swVerticalJustification_e.html)

Remarks

After using this property, use [IModelDoc2::GraphicsRedraw2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GraphicsRedraw2.md) to redraw the graphics window to see your changes.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::HorizontalJustification Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~HorizontalJustification.md)  
[IDisplayDimension::AddDisplayText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~AddDisplayText.md)  
[IDisplayDimension::IAddDisplayText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~IAddDisplayText.md)
