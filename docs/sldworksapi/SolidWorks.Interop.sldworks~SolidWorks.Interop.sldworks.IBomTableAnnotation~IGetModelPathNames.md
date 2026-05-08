# IGetModelPathNames Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~IGetModelPathNames`

Gets the full pathnames of all documents in the specified row of this BOM table annotation. Also gets the item and part numbers associated with the specified row.
Gets the full pathnames of all documents in the specified row of this BOM table annotation. Also gets the item and part numbers associated with the specified row.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetModelPathNames( _
   ByVal RowIndex As System.Integer, _
   ByVal Count As System.Integer, _
   ByRef ItemNumber As System.String, _
   ByRef PartNumber As System.String _
) As System.String
```

```

Dim instance As IBomTableAnnotation
Dim RowIndex As System.Integer
Dim Count As System.Integer
Dim ItemNumber As System.String
Dim PartNumber As System.String
Dim value As System.String
 
value = instance.IGetModelPathNames(RowIndex, Count, ItemNumber, PartNumber)
```

```

System.string IGetModelPathNames( 
   System.int RowIndex,
   System.int Count,
   out System.string ItemNumber,
   out System.string PartNumber
)
```

```

System.String^ IGetModelPathNames( 
   System.int RowIndex,
   System.int Count,
   [Out] System.String^ ItemNumber,
   [Out] System.String^ PartNumber
) 
```

#### Parameters

*RowIndex*
:   Row in the BOM table; 0-based index

*Count*
:   Number of model pathnames

*ItemNumber*
:   Item number for the specified BOM table row

*PartNumber*
:   Part number for the specified BOM table row

#### Return Value

- in-process, unmanaged C++: Pointer to an array of model pathnames in the specified row

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [IBomTableAnnotation::GetModelPathNamesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetModelPathNamesCount.md) to get the value of Count.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBomTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.md)  
[IBomTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation_members.md)  
[IBomTableAnnotation::GetModelPathNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetModelPathNames.md)
