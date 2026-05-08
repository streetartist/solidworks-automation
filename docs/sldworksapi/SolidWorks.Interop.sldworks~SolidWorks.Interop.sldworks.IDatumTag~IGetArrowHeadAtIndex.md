# IGetArrowHeadAtIndex Method (IDatumTag)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~IGetArrowHeadAtIndex`

Gets information for the specified arrow head in this datum tag.
Gets information for the specified arrow head in this datum tag.

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

Dim instance As IDatumTag
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
:   Index of the arrow head; index begins at 0

#### Return Value

Pointer to an array of doubles (see **Remarks**)

Remarks

The return value is the following array of doubles :

> **[** *arrowHeadPt[3], arrowHeadDir[3], arrowHeadWidth, arrowHeadHeight, arrowHeadStyle* **]**

where:

|  |  |
| --- | --- |
| *arrowHeadPt[3]* | XYZ arrow head tip location |
| *arrowHeadDir[3]* | XYZ arrow head direction |
| *arrowHeadWidth* | Arrow head width where the width is measured along the arrow head direction |
| *arrowHeadHeight* | Arrow head height |
| *arrowHeadStyle* | Arrow head style as defined in [swArrowStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArrowStyle_e.html) |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDatumTag Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag.md)  
[IDatumTag Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag_members.md)  
[IDatumTag::GetArrowHeadAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetArrowHeadAtIndex.md)  
[IDatumTag::GetArrowHeadCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetArrowHeadCount.md)
