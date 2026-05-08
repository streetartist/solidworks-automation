# IGetLineAtIndex Method (INote)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetLineAtIndex`

Gets information for the specified line.
Gets information for the specified line.

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

Dim instance As INote
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
:   Index of the desired line where the index begins at 0

#### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

The return value is the following array of doubles :

[ lineType, startPt[3], endPt[3]

  where:

|  |  |
| --- | --- |
| lineType | = the line type. Refer to the [swLineTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html) enumeration. |
| startPt[3] | = the XYZ line start point |
| endPt[3] | = the XYZ line end point |

The data returned from this method is in terms of document space. If the document containing this note is a drawing, then the coordinates returned are based on the sheet origin. If the document is a part or assembly, then the coordinates are based on the model origin.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)  
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.md)  
[INote::GetLineAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetLineAtIndex.md)  
[INote::GetLineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetLineCount.md)
