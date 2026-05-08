# GetArrowHeadAtIndex Method (IDisplayData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetArrowHeadAtIndex`

Obsolete. Superseded by IDisplayData::GetArrowheadAtIndex2.
Obsolete. Superseded by [IDisplayData::GetArrowheadAtIndex2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetArrowHeadAtIndex2.md).

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

Dim instance As IDisplayData
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
:   Index of the desired arrow head where the index begins at zero

#### Return Value

Array of doubles (see **Remarks**)

Remarks

The return value is the following array of doubles:

**[** *arrowHeadPt[3], arrowHeadDir[3], arrowHeadWidth, arrowHeadHeight, arrowHeadStyle* **]**

where:

|  |  |
| --- | --- |
| arrowHeadPt[3] | XYZ arrow head tip location |
| arrowHeadDir[3] | XYZ arrow head direction |
| arrowHeadWidth | Arrow head width measured along the arrow head direction |
| arrowHeadHeight | Arrow head height |
| arrowHeadStyle | Arrow head style as defined in [swArrowStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArrowStyle_e.html) |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData.md)  
[IDisplayData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData_members.md)  
[IDisplayData::IGetArrowHeadAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~IGetArrowHeadAtIndex.md)  
[IDisplayData::GetArrowHeadCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetArrowHeadCount.md)
