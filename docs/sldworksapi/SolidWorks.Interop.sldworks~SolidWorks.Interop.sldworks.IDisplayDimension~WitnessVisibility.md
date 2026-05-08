# WitnessVisibility Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~WitnessVisibility`

Gets or sets which extension lines are visible.
Gets or sets which extension lines are visible.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property WitnessVisibility As System.Integer
```

```

Dim instance As IDisplayDimension
Dim value As System.Integer
 
instance.WitnessVisibility = value
 
value = instance.WitnessVisibility
```

```

System.int WitnessVisibility {get; set;}
```

```

property System.int WitnessVisibility {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Extension-line visibility state as defined in [swWitnessLineVisibility\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWitnessLineVisibility_e.html)

Remarks

After using this property, use [IModelDoc2::GraphicsRedraw2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GraphicsRedraw2.md) to redraw the graphics window to see your changes.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::SmartWitness Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SmartWitness.md)  
[IDisplayDimension::MaxWitnessLineLength Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~MaxWitnessLineLength.md)
