# ISetSkippedItemArray Method (ICurveDrivenPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~ISetSkippedItemArray`

Sets the list of skipped items for this curve-driven pattern feature.
Sets the list of skipped items for this curve-driven pattern feature.

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

Dim instance As ICurveDrivenPatternFeatureData
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
:   Number of skipped features

*ArrayDataIn*
:   - in-process, unmanaged C++: Pointer to an array of skipped items of size FeatCount

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICurveDrivenPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData.md)  
[ICurveDrivenPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData_members.md)  
[ICurveDrivenPatternFeatureData::GetSkippedItemCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~GetSkippedItemCount.md)  
[ICurveDrivenPatternFeatureData::IGetSkippedItemArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~IGetSkippedItemArray.md)  
[ICurveDrivenPatternFeatureData::SkippedItemArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~SkippedItemArray.md)
