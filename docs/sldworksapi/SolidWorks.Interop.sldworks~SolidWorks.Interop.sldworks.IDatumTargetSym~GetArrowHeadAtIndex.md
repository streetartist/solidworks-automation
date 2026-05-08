# GetArrowHeadAtIndex Method (IDatumTargetSym)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetArrowHeadAtIndex`

Gets information on the specified arrow head in this datum target symbol.
Gets information on the specified arrow head in this datum target symbol.

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

Dim instance As IDatumTargetSym
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
:   Index of the arrow head; index begins at 0

#### Return Value

Array of doubles (see **Remarks**)

Remarks

The return value is the following array of doubles:

> **[** *arrowHeadPt[3], arrowHeadDir[3], arrowHeadWidth, arrowHeadHeight, arrowHeadStyle* **]**

where:

|  |  |
| --- | --- |
| arrowHeadPt[3] | XYZ arrow head tip location |
| arrowHeadDir[3] | XYZ arrow head direction |
| arrowHeadWidth | Arrow head width where the width is measured along the arrow head direction |
| arrowHeadHeight | Arrow head height |
| arrowHeadStyle | Arrow head style as defined in [swArrowStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArrowStyle_e.html) |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDatumTargetSym Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym.md)  
[IDatumTargetSym Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym_members.md)  
[IDatumTargetSym::GetArrowHeadCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetArrowHeadCount.md)  
[IDatumTargetSym::IGetArrowHeadAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~IGetArrowHeadAtIndex.md)
