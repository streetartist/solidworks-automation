# Split Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~Split`

Splits the table at the specified location.
Splits the table at the specified location.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Split( _
   ByVal Where As System.Integer, _
   ByVal Index As System.Integer _
) As TableAnnotation
```

```

Dim instance As ITableAnnotation
Dim Where As System.Integer
Dim Index As System.Integer
Dim value As TableAnnotation
 
value = instance.Split(Where, Index)
```

```

TableAnnotation Split( 
   System.int Where,
   System.int Index
)
```

```

TableAnnotation^ Split( 
   System.int Where,
   System.int Index
) 
```

#### Parameters

*Where*
:   Where to split the table as defined in [swTableSplitLocations\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTableSplitLocations_e.html)

*Index*
:   Index of the row or column as specified in Where to split the table (see **Remarks**)

#### Return Value

Newly created [ITableAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md) object

Remarks

The index for both rows and columns is 0-based.

The indexes for the rows and columns always correspond to the rows and columns of the table from which the split table originates.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md)  
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.md)  
[ITableAnnotation::IsCellMerged Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~IsCellMerged.md)  
[ITableAnnotation::Merge Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~Merge.md)  
[ITableAnnotation::MergeCells Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~MergeCells.md)  
[ITableAnnotation::UnmergeCells Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~UnmergeCells.md)  
[ITableAnnotation::GetSplitInformation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetSplitInformation.md)  
[ITableAnnotation::HorizontalAutoSplit Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~HorizontalAutoSplit.md)  
[ITableAnnotation::StopAutoSplitting Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~StopAutoSplitting.md)
