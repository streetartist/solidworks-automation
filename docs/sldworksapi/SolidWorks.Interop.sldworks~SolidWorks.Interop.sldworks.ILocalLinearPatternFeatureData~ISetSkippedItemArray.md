# ISetSkippedItemArray Method (ILocalLinearPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~ISetSkippedItemArray`

Sets the skipped components in this linear component pattern feature.
Sets the skipped components in this linear component pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetSkippedItemArray( _
   ByVal FeatCount As System.Integer, _
   ByRef ArrayDataIn As System.Integer _
) 
```

```

Dim instance As ILocalLinearPatternFeatureData
Dim FeatCount As System.Integer
Dim ArrayDataIn As System.Integer
 
instance.ISetSkippedItemArray(FeatCount, ArrayDataIn)
```

```

void ISetSkippedItemArray( 
   System.int FeatCount,
   ref System.int ArrayDataIn
)
```

```

void ISetSkippedItemArray( 
   System.int FeatCount,
   System.int% ArrayDataIn
) 
```

#### Parameters

*FeatCount*
:   Number of components to skip

*ArrayDataIn*
:   - in-process, unmanaged C++: Pointer to an array of skipped components

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

ArrayDataIn is 0-based. If you skip the 3rd and 5th components in the pattern, the array looks like ArrayDataIn[0] = 3 and ArrayDataIn[1] = 5.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILocalLinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData.md)  
[ILocalLinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData_members.md)  
[ILocalLinearPatternFeatureData::GetSkippedItemCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~GetSkippedItemCount.md)  
[ILocalLinearPatternFeatureData::IGetSkippedItemArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~IGetSkippedItemArray.md)  
[ILocalLinearPatternFeatureData::SkippedItemArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~SkippedItemArray.md)
