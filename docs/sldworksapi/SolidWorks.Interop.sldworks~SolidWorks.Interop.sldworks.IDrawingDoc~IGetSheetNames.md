# IGetSheetNames Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IGetSheetNames`

Gets a list of the names of the drawing sheets in this drawing.
Gets a list of the names of the drawing sheets in this drawing.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetSheetNames( _
   ByRef Count As System.Integer _
) As System.String
```

```

Dim instance As IDrawingDoc
Dim Count As System.Integer
Dim value As System.String
 
value = instance.IGetSheetNames(Count)
```

```

System.string IGetSheetNames( 
   out System.int Count
)
```

```

System.String^ IGetSheetNames( 
   [Out] System.int Count
) 
```

#### Parameters

*Count*
:   Number of drawing sheets in this drawing (see Remarks)

#### Return Value

- in-process, unmanaged C++: Pointer to an array containing the names of the drawing sheets in this drawing of size Count

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

The argument Count is used to help prevent memory overwrites. First call [IDrawingDoc::GetSheetCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetSheetCount.md) to get the number of sheets in this drawing. Then use its return value to dimension the return value array.

This method compares the number of sheets in this part with the value passed in.

|  |  |
| --- | --- |
| **If the actual number of sheets is...** | **Then...** |
| Larger than the value passed in | no sheets are returned, and status returns S\_ERROR. |
| Smaller than this value | the names of all of the sheets in the return value is returned and changes Count to reflect the actual number of sheets. |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDrawingDoc::ActivateSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ActivateSheet.md)  
[IDrawingDoc::EditSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~EditSheet.md)  
[IDrawingDoc::GetCurrentSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetCurrentSheet.md)  
[IDrawingDoc::GetSheetNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetSheetNames.md)  
[IDrawingDoc::IGetCurrentSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IGetCurrentSheet.md)  
[IDrawingDoc::NewSheet3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~NewSheet3.md)  
[IDrawingDoc::SetupSheet4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetupSheet4.md)  
[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.md)
