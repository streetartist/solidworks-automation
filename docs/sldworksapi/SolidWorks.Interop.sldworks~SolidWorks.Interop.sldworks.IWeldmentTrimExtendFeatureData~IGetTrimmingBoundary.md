# IGetTrimmingBoundary Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~IGetTrimmingBoundary`

Gets the entities used to define the trimming boundaries.
Gets the entities used to define the trimming boundaries.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetTrimmingBoundary( _
   ByVal Count As System.Integer, _
   ByRef Type As System.Integer _
) As System.Object
```

```

Dim instance As IWeldmentTrimExtendFeatureData
Dim Count As System.Integer
Dim Type As System.Integer
Dim value As System.Object
 
value = instance.IGetTrimmingBoundary(Count, Type)
```

```

System.object IGetTrimmingBoundary( 
   System.int Count,
   out System.int Type
)
```

```

System.Object^ IGetTrimmingBoundary( 
   System.int Count,
   [Out] System.int Type
) 
```

#### Parameters

*Count*
:   Number of trimming boundaries

*Type*
:   Type of trimming boundary:

    - swSelSOLIDBODIES
    - SwSelFACES

#### Return Value

- in-process, unmanaged C++: Pointer to an array of entities that define the trimming boundaries
- VBA, VB.NET, C#, and C++/CLI: Not supported
- See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Only end-trim corner types (swEndConditionTrim) can have multiple boundaries. Use [IWeldmentTrimExtendFeatureData::CornerType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~CornerType.md) to determine the type of corner.

Before calling this method, call [IWeldmentTrimExtendFeatureData::GetTrimmingBoundaryCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~GetTrimmingBoundaryCount.md) to get Count.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWeldmentTrimExtendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData.md)  
[IWeldmentTrimExtendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData_members.md)  
[IWeldmentTrimExtendFeatureData::GetTrimmingBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~GetTrimmingBoundary.md)  
[IWeldmentTrimExtendFeatureData::ISetTrimmingBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~ISetTrimmingBoundary.md)  
[IWeldmentTrimExtendFeatureData::SetTrimmingBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~SetTrimmingBoundary.md)
