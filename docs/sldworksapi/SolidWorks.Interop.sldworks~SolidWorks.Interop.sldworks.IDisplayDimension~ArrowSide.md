# ArrowSide Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ArrowSide`

Gets or sets the position of the dimension arrows.
Gets or sets the position of the dimension arrows.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ArrowSide As System.Integer
```

```

Dim instance As IDisplayDimension
Dim value As System.Integer
 
instance.ArrowSide = value
 
value = instance.ArrowSide
```

```

System.int ArrowSide {get; set;}
```

```

property System.int ArrowSide {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Dimension arrow side state as defined in [swDimensionArrowsSide\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDimensionArrowsSide_e.html)

Remarks

By specifying one of the following values in the Dimension Arrow Side state, the location of the dimension arrow with respect to the extension lines can be controlled. Valid values are listed in the [swDimensionArrowsSide\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDimensionArrowsSide_e.html) enumeration.

The graphics of the drawing change when you change this property. After you finish changing the drawing, use [IModelDoc2::WindowRedraw](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~WindowRedraw.md) to regenerate the drawing and display your changes.

Example

[Get Dimension Values in Drawing (VBA)](Get_Dimension_Values_in_Drawing_Example_VB.htm)  
[Get Display Dimension Properties (VBA)](Get_Display_Dimension_Properties_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::GetSecondArrow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetSecondArrow.md)  
[IDisplayDimension::GetUseDocSecondArrow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUseDocSecondArrow.md)  
[IDisplayDimension::SetSecondArrow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetSecondArrow.md)
