# SmartWitness Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SmartWitness`

Gets or sets the smart display of extension lines.
Gets or sets the smart display of extension lines.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SmartWitness As System.Boolean
```

```

Dim instance As IDisplayDimension
Dim value As System.Boolean
 
instance.SmartWitness = value
 
value = instance.SmartWitness
```

```

System.bool SmartWitness {get; set;}
```

```

property System.bool SmartWitness {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True uses extension line smart display, false does not

Remarks

After using this property, use [IModelDoc2::GraphicsRedraw2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GraphicsRedraw2.md) to redraw the graphics window to see your changes.

Example

[Get Display Dimension Properties (VBA)](Get_Display_Dimension_Properties_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::MaxWitnessLineLength Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~MaxWitnessLineLength.md)  
[IDisplayDimension::WitnessVisibility Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~WitnessVisibility.md)
