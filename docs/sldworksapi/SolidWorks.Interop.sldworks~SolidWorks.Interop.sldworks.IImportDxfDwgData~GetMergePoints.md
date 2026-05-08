# GetMergePoints Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~GetMergePoints`

Gets whether near-identical points are merged in the part sketch after entities are imported.
Gets whether near-identical points are merged in the part sketch after entities are imported.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetMergePoints( _
   ByVal Sheet As System.String _
) As System.Boolean
```

```

Dim instance As IImportDxfDwgData
Dim Sheet As System.String
Dim value As System.Boolean
 
value = instance.GetMergePoints(Sheet)
```

```

System.bool GetMergePoints( 
   System.string Sheet
)
```

```

System.bool GetMergePoints( 
   System.String^ Sheet
) 
```

#### Parameters

*Sheet*
:   Sheet (layout) name of the input file or an empty string for all sheets

#### Return Value

True to merge near-identical points, false to not

Remarks

This property only supports importing to a part sketch; it does not support importing to a drawing.

By default, points within 0.001mm are merged.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IImportDxfDwgData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData.md)  
[IImportDxfDwgData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData_members.md)  
[IImportDxfDwgData::GetMergeDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~GetMergeDistance.md)  
[IImportDxfDwgData::SetMergePoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData~SetMergePoints.md)
