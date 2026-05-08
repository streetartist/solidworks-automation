# ISetTrimmingBoundary Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~ISetTrimmingBoundary`

Gets the entities used to define the trimming boundaries.
Gets the entities used to define the trimming boundaries.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetTrimmingBoundary( _
   ByVal Count As System.Integer, _
   ByRef TrimBoundArr As System.Object _
) 
```

```

Dim instance As IWeldmentTrimExtendFeatureData
Dim Count As System.Integer
Dim TrimBoundArr As System.Object
 
instance.ISetTrimmingBoundary(Count, TrimBoundArr)
```

```

void ISetTrimmingBoundary( 
   System.int Count,
   ref System.object TrimBoundArr
)
```

```

void ISetTrimmingBoundary( 
   System.int Count,
   System.Object^% TrimBoundArr
) 
```

#### Parameters

*Count*
:   Number of trimming boundaries

*TrimBoundArr*
:   - in-process, unmanaged C++: Pointer to an array of entities that define the trimming boundaries (see **Remarks**)

      - Solid bodies created by weldment members  
          
        - or -
      - Planar faces on non-weldment members, or planar faces on weldment members, or both

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

#### Return Value

Entities that define the trimming boundaries

Remarks

Faces are valid for end-trim corner types only. You can only specify multiple trimming boundaries for end-trim corner types. Use [IWeldmentTrimExtendFeatureData::CornerType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~CornerType.md) to determine the type of corner.

You must set the [bodies to trim](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~BodiesToBeTrimmed.md) and set the trimming boundary if changing a corner type.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWeldmentTrimExtendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData.md)  
[IWeldmentTrimExtendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData_members.md)  
[IWeldmentTrimExtendFeatureData::SetTrimmingBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~SetTrimmingBoundary.md)  
[IWeldmentTrimExtendFeatureData::IGetTrimmingBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~IGetTrimmingBoundary.md)  
[IWeldmentTrimExtendFeatureData::GetTrimmingBoundaryCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~GetTrimmingBoundaryCount.md)  
[IWeldmentTrimExtendFeatureData::GetTrimmingBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~GetTrimmingBoundary.md)
