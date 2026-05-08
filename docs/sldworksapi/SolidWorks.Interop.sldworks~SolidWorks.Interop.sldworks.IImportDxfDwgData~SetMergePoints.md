# SetMergePoints Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~SetMergePoints`

Sets whether near-identical points within the specified distance are merged in the part sketch after entities are imported.
Sets whether near-identical points within the specified distance are merged in the part sketch after entities are imported.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetMergePoints( _
   ByVal Sheet As System.String, _
   ByVal Merge As System.Boolean, _
   ByVal Distance As System.Double _
) As System.Boolean
```

```

Dim instance As IImportDxfDwgData
Dim Sheet As System.String
Dim Merge As System.Boolean
Dim Distance As System.Double
Dim value As System.Boolean
 
value = instance.SetMergePoints(Sheet, Merge, Distance)
```

```

System.bool SetMergePoints( 
   System.string Sheet,
   System.bool Merge,
   System.double Distance
)
```

```

System.bool SetMergePoints( 
   System.String^ Sheet,
   System.bool Merge,
   System.double Distance
) 
```

#### Parameters

*Sheet*
:   Sheet (layout) name of the input file or an empty string for all sheets

*Merge*
:   True to merge near-identical points, false to not

*Distance*
:   Distance to determine whether two points should be merged

#### Return Value

True if near-identical points within the specified distance are merged, false if not

Remarks

This property only supports importing to a part sketch; it does not support importing to a drawing.

By default, points within 0.001mm are merged.

Example

[Import DXF file into Part Sketch (VBA)](Import_DXF_File_into_Part_Sketch_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IImportDxfDwgData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData.md)  
[IImportDxfDwgData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData_members.md)  
[IImportDxfDwgData::GetMergePoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~GetMergePoints.md)  
[IImportDxfDwgData::GetMergeDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~GetMergeDistance.md)
