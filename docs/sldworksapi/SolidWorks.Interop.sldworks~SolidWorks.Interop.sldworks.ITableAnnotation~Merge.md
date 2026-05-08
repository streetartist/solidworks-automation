# Merge Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~Merge`

Merges the display of this table.
Merges the display of this table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Merge( _
   ByVal Where As System.Integer _
) As System.Boolean
```

```

Dim instance As ITableAnnotation
Dim Where As System.Integer
Dim value As System.Boolean
 
value = instance.Merge(Where)
```

```

System.bool Merge( 
   System.int Where
)
```

```

System.bool Merge( 
   System.int Where
) 
```

#### Parameters

*Where*
:   Merge the display of this table as defined in [swTableMergeLocations\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTableMergeLocations_e.html)

#### Return Value

True if the merge is successful, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md)  
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.md)  
[ITableAnnotation::IsCellMerged Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~IsCellMerged.md)  
[ITableAnnotation::MergeCells Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~MergeCells.md)  
[ITableAnnotation::GetSplitInformation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetSplitInformation.md)  
[ITableAnnotation::Split Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~Split.md)  
[ITableAnnotation::UnmergeCells Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~UnmergeCells.md)
