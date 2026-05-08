# GetModelPathNames Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetModelPathNames`

Gets the full pathnames of all documents in the specified row of this BOM table annotation. Also gets the item and part numbers associated with the specified row.
Gets the full pathnames of all documents in the specified row of this BOM table annotation. Also gets the item and part numbers associated with the specified row.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetModelPathNames( _
   ByVal RowIndex As System.Integer, _
   ByRef ItemNumber As System.String, _
   ByRef PartNumber As System.String _
) As System.Object
```

```

Dim instance As IBomTableAnnotation
Dim RowIndex As System.Integer
Dim ItemNumber As System.String
Dim PartNumber As System.String
Dim value As System.Object
 
value = instance.GetModelPathNames(RowIndex, ItemNumber, PartNumber)
```

```

System.object GetModelPathNames( 
   System.int RowIndex,
   out System.string ItemNumber,
   out System.string PartNumber
)
```

```

System.Object^ GetModelPathNames( 
   System.int RowIndex,
   [Out] System.String^ ItemNumber,
   [Out] System.String^ PartNumber
) 
```

#### Parameters

*RowIndex*
:   Row in the BOM table; 0-based index

*ItemNumber*
:   Item number for the specified BOM table row

*PartNumber*
:   Part number for the specified BOM table row

#### Return Value

Array of full pathnames of the models in the specified BOM table row

Example

[Get Model Pathnames in BOM Table (C#)](Get_Model_Path_Names_in_BOM_Table_Example_CSharp.htm)  
[Get Model Pathnames in BOM Table (VB.NET)](Get_Model_Path_Names_in_BOM_Table_Example_VBNET.htm)  
[Get Model Pathnames in BOM Table (VBA)](Get_Model_Path_Names_in_BOM_Table_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBomTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.md)  
[IBomTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation_members.md)  
[IBomTableAnnotation::IGetModelPathNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~IGetModelPathNames.md)  
[IBomTableAnnotation::GetModelPathNamesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetModelPathNamesCount.md)
