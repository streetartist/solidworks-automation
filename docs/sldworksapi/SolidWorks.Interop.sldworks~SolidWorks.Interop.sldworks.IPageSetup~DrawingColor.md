# DrawingColor Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~DrawingColor`

Sets the color of the drawing for printing.
Sets the color of the drawing for printing.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DrawingColor As System.Integer
```

```

Dim instance As IPageSetup
Dim value As System.Integer
 
instance.DrawingColor = value
 
value = instance.DrawingColor
```

```

System.int DrawingColor {get; set;}
```

```

property System.int DrawingColor {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Color of drawing for printing as defined in [swPageSetupDrawingColor\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPageSetupDrawingColor_e.html)

Remarks

This method can only be set with an application-level ([IModelDocExtension::AppPageSetup](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AppPageSetup.md)) or document-level ([IModelDoc2::PageSetup](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~PageSetup.md) or [IModelDoc2::IPageSetup](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IPageSetup.md)) object. This method is not available at the sheet level.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPageSetup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup.md)  
[IPageSetup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup_members.md)
