# IGetLineAtIndex Method (IMultiJogLeader)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMultiJogLeader~IGetLineAtIndex`

Gets the symbol information for the specified line.
Gets the symbol information for the specified line.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetLineAtIndex( _
   ByVal Index As System.Integer _
) As System.Double
```

```

Dim instance As IMultiJogLeader
Dim Index As System.Integer
Dim value As System.Double
 
value = instance.IGetLineAtIndex(Index)
```

```

System.double IGetLineAtIndex( 
   System.int Index
)
```

```

System.double IGetLineAtIndex( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Index of the line where the index begins at 0

#### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

The return value is the following array of doubles:

[ lineType, startPt[3], endPt[3] ]

where:

- lineType = line type. See [swLineTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html).
- startPt[3] = XYZ line start point.
- endPt[3] = XYZ line end point.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMultiJogLeader Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMultiJogLeader.md)  
[IMultiJogLeader Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMultiJogLeader_members.md)  
[IMultiJogLeader::GetLineAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMultiJogLeader~GetLineAtIndex.md)  
[IMultiJogLeader::GetLineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMultiJogLeader~GetLineCount.md)
