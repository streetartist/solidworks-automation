# GetArrowHeadAtIndex Method (IWeldSymbol)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetArrowHeadAtIndex`

Gets information on the specified arrowhead in this weld symbol.
Gets information on the specified arrowhead in this weld symbol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetArrowHeadAtIndex( _
   ByVal Index As System.Integer _
) As System.Object
```

```

Dim instance As IWeldSymbol
Dim Index As System.Integer
Dim value As System.Object
 
value = instance.GetArrowHeadAtIndex(Index)
```

```

System.object GetArrowHeadAtIndex( 
   System.int Index
)
```

```

System.Object^ GetArrowHeadAtIndex( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Index of the arrow head where the index begins at 0

#### Return Value

Array of doubles (see Remarks)

Remarks

The return value is the following array of doubles :

[ arrowHeadPt[3], arrowHeadDir[3], arrowHeadWidth, arrowHeadHeight, arrowHeadStyle ]

where:

|  |  |
| --- | --- |
| arrowHeadPt[3] | = XYZ arrow head tip location. |
| arrowHeadDir[3] | = XYZ arrow head direction. |
| arrowHeadWidth | = arrow head width where the width is measured along the arrow head direction. |
| arrowHeadHeight | = arrow head height. |
| arrowHeadStyle | = arrow head style (that is, open, closed, and so on) as defined in [swArrowStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArrowStyle_e.html). |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWeldSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.md)  
[IWeldSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol_members.md)  
[IWeldSymbol::GetArrowHeadCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetArrowHeadCount.md)  
[IWeldSymbol::GetArrowHeadInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetArrowHeadInfo.md)  
[IWeldSymbol::IGetArrowHeadAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~IGetArrowHeadAtIndex.md)  
[IWeldSymbol::IGetArrowHeadInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~IGetArrowHeadInfo.md)
