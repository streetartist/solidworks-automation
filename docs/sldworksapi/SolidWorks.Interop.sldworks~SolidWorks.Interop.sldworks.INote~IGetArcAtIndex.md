# IGetArcAtIndex Method (INote)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetArcAtIndex`

Gets information for the specified arc in this note.
Gets information for the specified arc in this note.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetArcAtIndex( _
   ByVal Index As System.Integer _
) As System.Double
```

```

Dim instance As INote
Dim Index As System.Integer
Dim value As System.Double
 
value = instance.IGetArcAtIndex(Index)
```

```

System.double IGetArcAtIndex( 
   System.int Index
)
```

```

System.double IGetArcAtIndex( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Index of the desired arc where the index begins at 0

#### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Call [INote::GetArcCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetArcCount.md) before calling this method to determine the size of the return array.

Return value is an array of doubles:

 [ LineType, StartPt[3], EndPt[3], CenterPt[3], RotDir ]

where :

|  |  |
| --- | --- |
| LineType | Line type. Valid returns are defined in [swLineTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html). A LineType is a combination of a line style and line weight. |
| StartPt[3] | Array of 3 doubles (X,Y,Z) describing the start point. |
| EndPt[3] | Array of 3 doubles (X,Y,Z) describing the end point. If the arc is closed, then this is the same point as the StartPt. |
| CenterPt[3] | Array of 3 doubles (X,Y,Z) describing the center point. |
| RotDir | Rotational direction (CW = -1, CCW = 1) |

The data returned from this method is in terms of document apace.

|  |  |
| --- | --- |
| **If the document containing this note is...** | **Then the coordinates returned are based on the...** |
| Drawing | Sheet origin |
| Part or assembly | Model origin |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)  
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.md)  
[INote::GetArcAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetArcAtIndex.md)
