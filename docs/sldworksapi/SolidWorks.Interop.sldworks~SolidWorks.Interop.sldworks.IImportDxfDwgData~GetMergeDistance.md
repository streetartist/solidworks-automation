# GetMergeDistance Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~GetMergeDistance`

Gets whether points that are within the specified distance are merged in the part sketch after entities are imported.
Gets whether points that are within the specified distance are merged in the part sketch after entities are imported.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetMergeDistance( _
   ByVal Sheet As System.String _
) As System.Double
```

```

Dim instance As IImportDxfDwgData
Dim Sheet As System.String
Dim value As System.Double
 
value = instance.GetMergeDistance(Sheet)
```

```

System.double GetMergeDistance( 
   System.string Sheet
)
```

```

System.double GetMergeDistance( 
   System.String^ Sheet
) 
```

#### Parameters

*Sheet*
:   Sheet (layout) name of the input file or an empty string for all sheets

#### Return Value

Distance to determine whether two points should be merged

Remarks

This property only supports importing to a part sketch; it does not support importing to a drawing.

By default, points within 0.001mm are merged.

Example

[Import DXF File into Part Sketch (VBA)](Import_DXF_File_into_Part_Sketch_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IImportDxfDwgData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData.md)  
[IImportDxfDwgData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData_members.md)  
[IImportDxfDwgData::GetMergePoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~GetMergePoints.md)  
[IImportDxfDwgData::SetMergePoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~SetMergePoints.md)
