# GetLineAtIndex3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetLineAtIndex3`

Gets information for the specified line.
Gets information for the specified line.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetLineAtIndex3( _
   ByVal Index As System.Integer _
) As System.Object
```

```

Dim instance As IDisplayData
Dim Index As System.Integer
Dim value As System.Object
 
value = instance.GetLineAtIndex3(Index)
```

```

System.object GetLineAtIndex3( 
   System.int Index
)
```

```

System.Object^ GetLineAtIndex3( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Index of the desired line where the index begins at 0

#### Return Value

Array of doubles (see **Remarks**)

Remarks

The return value is the following array of doubles:

[ color, lineType, lineStyle, lineWeight, startPt[3], endPt[3] ]

where:

|  |  |
| --- | --- |
| color | COLORREF returned as an integer; return value can be 0 or -1 for default color |
| lineType | Line type as defined in [swLineTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html) |
| lineStyle | Line style as defined in [swLineStyles\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineStyles_e.html) |
| lineWeight | Line thickness as defined in [swLineWeights\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineWeights_e.html) |
| startPt[3] | x, y, z  line start point |
| endPt[3] | x, y, z line end point |

Example

[Get Centerline Annotation Information (VBA)](Get_Centerline_Annotation_Information_Example_VB.htm)  
[Get Weld Bead Symbol Data (VBA)](Get_Weld_Bead_End_Treatment_Symbol_Data_Example_VB.htm)  
[Get Weld Bead Symbol Data (VB.NET)](Get_Weld_Bead_End_Treatment_Symbol_Data_Example_VBNET.htm)  
[Get Weld Bead Symbol Data (C#)](Get_Weld_Bead_End_Treatment_Symbol_Data_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData.md)  
[IDisplayData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData_members.md)  
[IDisplayData::IGetLineAtIndex3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~IGetLineAtIndex3.md)  
[IDisplayData::GetLineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetLineCount.md)
