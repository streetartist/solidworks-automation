# IGetArrowHeadAtIndex Method (IMultiJogLeader)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMultiJogLeader~IGetArrowHeadAtIndex`

Gets the information for the specified arrow head.
Gets the information for the specified arrow head.

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

Dim instance As IMultiJogLeader
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
:   Index of the arrow head where the index begins at 0

#### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

The return value is the following array of doubles :

[ arrowHeadPt[3], arrowHeadDir[3], arrowHeadWidth, arrowHeadHeight, arrowHeadStyle ]

where:

- arrowHeadPt[3] = XYZ arrow head tip location.
- arrowHeadDir[3] = XYZ arrow head direction.
- arrowHeadWidth = arrow head width where the width is measured along the arrow head direction.
- arrowHeadHeight = arrow head height.
- arrowHeadStyle = arrow head style; for example, open, closed, and so on. See [swArrowStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArrowStyle_e.html).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMultiJogLeader Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMultiJogLeader.md)  
[IMultiJogLeader Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMultiJogLeader_members.md)  
[IMultiJogLeader::GetArrowHeadAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMultiJogLeader~GetArrowHeadAtIndex.md)  
[IMultiJogLeader::GetArrowHeadCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMultiJogLeader~GetArrowHeadCount.md)
