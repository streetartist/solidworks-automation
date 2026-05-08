# ShowParenthesis Property (IDisplayDimension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ShowParenthesis`

Gets or sets whether to enclose the text above the dimension line of the display dimension in parentheses.
Gets or sets whether to enclose the text above the dimension line of the display dimension in parentheses.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ShowParenthesis As System.Boolean
```

```

Dim instance As IDisplayDimension
Dim value As System.Boolean
 
instance.ShowParenthesis = value
 
value = instance.ShowParenthesis
```

```

System.bool ShowParenthesis {get; set;}
```

```

property System.bool ShowParenthesis {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to enclose the text above the dimension line of the display dimension in parentheses, false to not

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
[IDisplayDimension::ShowLowerParenthesis Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ShowLowerParenthesis.md)
