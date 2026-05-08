# ShowDimensionValue Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ShowDimensionValue`

Gets or sets whether the dimension value is displayed as part of the dimension text.
Gets or sets whether the dimension value is displayed as part of the dimension text.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ShowDimensionValue As System.Boolean
```

```

Dim instance As IDisplayDimension
Dim value As System.Boolean
 
instance.ShowDimensionValue = value
 
value = instance.ShowDimensionValue
```

```

System.bool ShowDimensionValue {get; set;}
```

```

property System.bool ShowDimensionValue {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True displays the dimension value, false does not

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
[IDisplayDimension::SetText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetText.md)  
[IDisplayDimension::GetText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetText.md)
