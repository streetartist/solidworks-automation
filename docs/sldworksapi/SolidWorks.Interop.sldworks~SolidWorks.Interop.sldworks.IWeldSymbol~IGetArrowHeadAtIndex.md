# IGetArrowHeadAtIndex Method (IWeldSymbol)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~IGetArrowHeadAtIndex`

Gets information on the specified arrowhead in this weld symbol.
Gets information on the specified arrowhead in this weld symbol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetArrowHeadAtIndex( _
   ByVal Index As System.Integer _
) As System.Double
```

```

Dim instance As IWeldSymbol
Dim Index As System.Integer
Dim value As System.Double
 
value = instance.IGetArrowHeadAtIndex(Index)
```

```

System.double IGetArrowHeadAtIndex( 
   System.int Index
)
```

```

System.double IGetArrowHeadAtIndex( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Index of the arrow head where the index begins at

#### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see Remarks)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

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
[IWeldSymbol::GetArrowHeadAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetArrowHeadAtIndex.md)  
[IWeldSymbol::GetArrowHeadCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetArrowHeadCount.md)  
[IWeldSymbol::GetArrowHeadInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetArrowHeadInfo.md)  
[IWeldSymbol::IGetArrowHeadInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~IGetArrowHeadInfo.md)
