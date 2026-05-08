# GetArrowHeadStyle2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetArrowHeadStyle2`

Gets the arrowhead style used by this display dimension.
Gets the arrowhead style used by this display dimension.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetArrowHeadStyle2( _
   ByRef Style1 As System.Integer, _
   ByRef Style2 As System.Integer _
) As System.Boolean
```

```

Dim instance As IDisplayDimension
Dim Style1 As System.Integer
Dim Style2 As System.Integer
Dim value As System.Boolean
 
value = instance.GetArrowHeadStyle2(Style1, Style2)
```

```

System.bool GetArrowHeadStyle2( 
   out System.int Style1,
   out System.int Style2
)
```

```

System.bool GetArrowHeadStyle2( 
   [Out] System.int Style1,
   [Out] System.int Style2
) 
```

#### Parameters

*Style1*
:   Arrowhead style of first arrowhead as defined in [swArrowStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArrowStyle_e.html)

*Style2*
:   Arrowhead style of second arrowhead as defined in [swArrowStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArrowStyle_e.html)

#### Return Value

True if the styles are set, false if not

Remarks

The arrowhead style for a display dimension is controlled by a value stored in one of two places: on the owning document or on the individual display dimension.  Use this method and [IDisplayDimension::GetUseDocArrowHeadStyle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUseDocArrowHeadStyle.md) to get the current values for these settings. Use [IDisplayDimension::SetArrowHeadStyle2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetArrowHeadStyle2.md) to set the arrowhead style.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)
