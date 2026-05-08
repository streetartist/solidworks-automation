# Style Property (IBreakLine)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine~Style`

Gets or sets the style of the break line in the drawing view.
Gets or sets the style of the break line in the drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Style As System.Integer
```

```

Dim instance As IBreakLine
Dim value As System.Integer
 
instance.Style = value
 
value = instance.Style
```

```

System.int Style {get; set;}
```

```

property System.int Style {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Break line style as defined in [swBreakLineStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBreakLineStyle_e.html)

Remarks

This property might automatically load the model in the view.

To get or set the shape intensity of a jagged cut break line, call [IBreakLine::ShapeIntensity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine~ShapeIntensity.md).

Example

[Create Break View (C#)](Create_Broken_View_Example_CSharp.htm)  
[Create Break View (VB.NET)](Create_Broken_View_Example_VBNET.htm)  
[Create Break View (VBA)](Create_Broken_View_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBreakLine Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine.md)  
[IBreakLine Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine_members.md)
