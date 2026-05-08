# HorizontalAutoSplit Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~HorizontalAutoSplit`

Starts the automatic horizontal splitting of this table using the specified options.
Starts the automatic horizontal splitting of this table using the specified options.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function HorizontalAutoSplit( _
   ByVal MaxNumberOfRows As System.Integer, _
   ByVal Apply As System.Integer, _
   ByVal PlacementOfNewSplitTables As System.Integer _
) As System.Object
```

```

Dim instance As ITableAnnotation
Dim MaxNumberOfRows As System.Integer
Dim Apply As System.Integer
Dim PlacementOfNewSplitTables As System.Integer
Dim value As System.Object
 
value = instance.HorizontalAutoSplit(MaxNumberOfRows, Apply, PlacementOfNewSplitTables)
```

```

System.object HorizontalAutoSplit( 
   System.int MaxNumberOfRows,
   System.int Apply,
   System.int PlacementOfNewSplitTables
)
```

```

System.Object^ HorizontalAutoSplit( 
   System.int MaxNumberOfRows,
   System.int Apply,
   System.int PlacementOfNewSplitTables
) 
```

#### Parameters

*MaxNumberOfRows*
:   Maximum number of rows in the split portions

*Apply*
:   How often to horizontally split the table as defined in [swHorizontalAutoSplitApply\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swHorizontalAutoSplitApply_e.html)

*PlacementOfNewSplitTables*
:   Where to place the horizontally split table as defined in [swHorizontalAutoSplitPlacementOfSplitTable\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swHorizontalAutoSplitPlacementOfSplitTable_e.html)

#### Return Value

Array of split [ITableAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md)s

Remarks

This method horizontally splits:

- [Hole tables](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTableAnnotation.md)
- [Bill of Materials tables](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.md)
- [General tables](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralTableAnnotation.md)

If Apply is set to [swHorizontalAutoSplitApply\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swHorizontalAutoSplitApply_e.html).Continuously, in order to stop the automatic splitting of tables, you must set [ITableAnnotation::StopAutoSplitting](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~StopAutoSplitting.md) to true.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md)  
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.md)  
[ITableAnnotation::Split Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~Split.md)  
[ITableAnnotation::GetSplitInformation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetSplitInformation.md)
