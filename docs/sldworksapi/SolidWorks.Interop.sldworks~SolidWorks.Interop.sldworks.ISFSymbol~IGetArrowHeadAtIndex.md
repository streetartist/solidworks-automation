# IGetArrowHeadAtIndex Method (ISFSymbol)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~IGetArrowHeadAtIndex`

Gets information on the specified arrow head in this surface finish symbol.
Gets information on the specified arrow head in this surface finish symbol.

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

Dim instance As ISFSymbol
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
:   Index of the arrow head where the index begins at 0

#### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Call [ISFSymbol::GetArrowHeadCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetArrowHeadCount.md) before calling this method to get the number of arrow heads for this surface finish symbol.

The return value is the following array of doubles :

[ arrowHeadPt[3], arrowHeadDir[3], arrowHeadWidth, arrowHeadHeight, arrowHeadStyle ]

where:

|  |  |
| --- | --- |
| arrowHeadPt[3] | = XYZ arrow head tip location |
| arrowHeadDir[3] | = XYZ arrow head direction |
| arrowHeadWidth | = Arrow head width where the width is measured along the arrow head direction |
| arrowHeadHeight | = Arrow head height |
| arrowHeadStyle | = Arrow head style (for example, open or closed) as defined in  [swArrowStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArrowStyle_e.html) |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISFSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.md)  
[ISFSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol_members.md)  
[ISFSymbol::GetArrowHeadAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetArrowHeadAtIndex.md)  
[ISFSymbol::GetArrowHeadInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetArrowHeadInfo.md)  
[ISFSymbol::IGetArrowHeadInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~IGetArrowHeadInfo.md)
