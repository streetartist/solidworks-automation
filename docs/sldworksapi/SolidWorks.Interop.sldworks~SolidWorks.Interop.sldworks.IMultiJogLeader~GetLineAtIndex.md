# GetLineAtIndex Method (IMultiJogLeader)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMultiJogLeader~GetLineAtIndex`

Gets the symbol information for the specified line.
Gets the symbol information for the specified line.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetLineAtIndex( _
   ByVal Index As System.Integer _
) As System.Object
```

```

Dim instance As IMultiJogLeader
Dim Index As System.Integer
Dim value As System.Object
 
value = instance.GetLineAtIndex(Index)
```

```

System.object GetLineAtIndex( 
   System.int Index
)
```

```

System.Object^ GetLineAtIndex( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Index of the line

#### Return Value

Array of doubles (see **Remarks**)

Remarks

The return value is the following array of doubles:

[ lineType, startPt[3], endPt[3] ]

where:

- lineType = line type. See [swLineTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html).
- startPt[3] = XYZ line start point.
- endPt[3] = XYZ line end point.

Example

[Get Multi-jog Leader Data (C#)](Get_Multi-jog_Leader_Data_Example_CSharp.htm)  
[Get Multi-jog Leader Data (VB.NET)](Get_Multi-jog_Leader_Data_Example_VBNET.htm)  
[Get Multi-jog Leader Data (VBA)](Get_Multi-jog_Leader_Data_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMultiJogLeader Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMultiJogLeader.md)  
[IMultiJogLeader Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMultiJogLeader_members.md)  
[IMultiJogLeader::GetLineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMultiJogLeader~GetLineCount.md)  
[IMultiJogLeader::IGetLineAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMultiJogLeader~IGetLineAtIndex.md)
