# SetArrowHeadStyle2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetArrowHeadStyle2`

Sets the arrowhead style of this display dimension.
Sets the arrowhead style of this display dimension.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetArrowHeadStyle2( _
   ByVal UseDoc As System.Boolean, _
   ByVal Style1 As System.Integer, _
   ByVal Style2 As System.Integer _
) As System.Boolean
```

```

Dim instance As IDisplayDimension
Dim UseDoc As System.Boolean
Dim Style1 As System.Integer
Dim Style2 As System.Integer
Dim value As System.Boolean
 
value = instance.SetArrowHeadStyle2(UseDoc, Style1, Style2)
```

```

System.bool SetArrowHeadStyle2( 
   System.bool UseDoc,
   System.int Style1,
   System.int Style2
)
```

```

System.bool SetArrowHeadStyle2( 
   System.bool UseDoc,
   System.int Style1,
   System.int Style2
) 
```

#### Parameters

*UseDoc*
:   True uses the document setting for arrowhead style, false uses the settings specified  
    in Style1 and Style2

*Style1*
:   Arrowhead style of first arrowhead as defined in [swArrowStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArrowStyle_e.html)

*Style2*
:   Arrowhead style of second arrowhead as defined in [swArrowStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArrowStyle_e.html)

#### Return Value

True if the arrowhead styles are set, false if not

Remarks

The arrowhead style for a display dimension is controlled by a value stored in one of two places: on the owning document or on the individual display dimension. Use [IDisplayDimension::GetUseDocArrowHeadStyle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUseDocArrowHeadStyle.md) and [IDisplayDimension::GetArrowHeadStyle2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetArrowHeadStyle2.md) to get the current values for these settings.

Setting UseDoc to True indicates that the document default setting for arrowhead style should be used, and Style1 and Style2 will be ignored.

After using this method, use [IModelDoc2::GraphicsRedraw2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GraphicsRedraw2.md) to redraw the graphics window to see your changes.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)
