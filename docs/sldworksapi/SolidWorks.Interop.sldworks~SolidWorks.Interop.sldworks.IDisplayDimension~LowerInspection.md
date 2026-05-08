# LowerInspection Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~LowerInspection`

Gets or sets whether a display dimension below the dimension line is displayed as an inspection dimension.
Gets or sets whether a display dimension below the dimension line is displayed as an inspection dimension.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property LowerInspection As System.Boolean
```

```

Dim instance As IDisplayDimension
Dim value As System.Boolean
 
instance.LowerInspection = value
 
value = instance.LowerInspection
```

```

System.bool LowerInspection {get; set;}
```

```

property System.bool LowerInspection {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if the display dimension below the dimension is displayed as an inspection dimension, false if not

Remarks

An inspection dimension is contained within an oval.

Example

[Get Chamfer Display Dimension (C#)](Get_Chamfer_Display_Dimension_Example_CSharp.htm)  
[Get Chamfer Display Dimension (VB.NET)](Get_Chamfer_Display_Dimension_Example_VBNET.htm)  
[Get Chamfer Display Dimension (VBA)](Get_Chamfer_Display_Dimension_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::GetLowerText Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetLowerText.md)  
[IDisplayDimension::SetLowerText Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetLowerText.md)  
[IDisplayDimension::Inspection Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Inspection.md)
