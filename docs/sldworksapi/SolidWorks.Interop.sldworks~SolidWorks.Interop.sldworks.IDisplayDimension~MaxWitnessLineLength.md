# MaxWitnessLineLength Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~MaxWitnessLineLength`

Gets or sets the maximum length of dimension extension lines.
Gets or sets the maximum length of dimension extension lines.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property MaxWitnessLineLength As System.Double
```

```

Dim instance As IDisplayDimension
Dim value As System.Double
 
instance.MaxWitnessLineLength = value
 
value = instance.MaxWitnessLineLength
```

```

System.double MaxWitnessLineLength {get; set;}
```

```

property System.double MaxWitnessLineLength {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Length

Remarks

After using this property, use [IModelDoc2::GraphicsRedraw2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GraphicsRedraw2.md) to redraw the graphics window to see your changes.

Example

[Set and Get Maximum Extension Line Length (VBA)](Set_and_Get_Maximum_Extension_Line_Length_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::SmartWitness Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SmartWitness.md)  
[IDisplayDimension::WitnessVisibility Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~WitnessVisibility.md)
