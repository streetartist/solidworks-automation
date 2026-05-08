# SetTrimmingBoundary Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~SetTrimmingBoundary`

Sets the trimming boundaries for this weldment trim extend feature.
Sets the trimming boundaries for this weldment trim extend feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetTrimmingBoundary( _
   ByVal TrimBoundVar As System.Object _
) 
```

```

Dim instance As IWeldmentTrimExtendFeatureData
Dim TrimBoundVar As System.Object
 
instance.SetTrimmingBoundary(TrimBoundVar)
```

```

void SetTrimmingBoundary( 
   System.object TrimBoundVar
)
```

```

void SetTrimmingBoundary( 
   System.Object^ TrimBoundVar
) 
```

#### Parameters

*TrimBoundVar*
:   Number of trimming boundaries

#### Return Value

Array of trimming boundaries:

- Solid bodies created by weldment members  
    
  - or -
- Planar faces on non-weldment members, or planar faces on weldment members, or both

See Remarks.

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
[IWeldmentTrimExtendFeatureData::GetTrimmingBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~GetTrimmingBoundary.md)  
[IWeldmentTrimExtendFeatureData::GetTrimmingBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~GetTrimmingBoundary.md)  
[IWeldmentTrimExtendFeatureData::IGetTrimmingBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~IGetTrimmingBoundary.md)  
[IWeldmentTrimExtendFeatureData::GetTrimmingBoundaryCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~GetTrimmingBoundaryCount.md)
