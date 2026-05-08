# ShowLowerParenthesis Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ShowLowerParenthesis`

Gets or sets whether to enclose the text below the dimension line of the display dimension in parentheses.
Gets or sets whether to enclose the text below the dimension line of the display dimension in parentheses.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ShowLowerParenthesis As System.Boolean
```

```

Dim instance As IDisplayDimension
Dim value As System.Boolean
 
instance.ShowLowerParenthesis = value
 
value = instance.ShowLowerParenthesis
```

```

System.bool ShowLowerParenthesis {get; set;}
```

```

property System.bool ShowLowerParenthesis {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to enclose the text below the dimension line of the display dimension in parentheses, false to not

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
[IDisplayDimension::ShowParenthesis Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ShowParenthesis.md)
