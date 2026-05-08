# IGetArrowHeadAtIndex Method (IGtol)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetArrowHeadAtIndex`

Gets information on the specified arrow head in this GTol.
Gets information on the specified arrow head in this GTol.

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

Dim instance As IGtol
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
:   0-based index of the arrow head

#### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

The return value is an array of doubles in the following format:

[ arrowHeadPt[3], arrowHeadDir[3], arrowHeadWidth, arrowHeadHeight, arrowHeadStyle ]

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

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md)  
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.md)  
[IGtol::GetArrowHeadAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetArrowHeadAtIndex.md)  
[IGtol::GetArrowHeadCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetArrowHeadCount.md)  
[IGtol::GetArrowHeadInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetArrowHeadInfo.md)  
[IGtol::IGetArrowHeadInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetArrowHeadInfo.md)
