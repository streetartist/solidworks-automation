# ISetPatternFeatureArray Method (ISketchPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~ISetPatternFeatureArray`

Sets the seed features for the sketch pattern feature.
Sets the seed features for the sketch pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetPatternFeatureArray( _
   ByVal FeatCount As System.Integer, _
   ByRef ArrayDataIn As System.Object _
) 
```

```

Dim instance As ISketchPatternFeatureData
Dim FeatCount As System.Integer
Dim ArrayDataIn As System.Object
 
instance.ISetPatternFeatureArray(FeatCount, ArrayDataIn)
```

```

void ISetPatternFeatureArray( 
   System.int FeatCount,
   ref System.object ArrayDataIn
)
```

```

void ISetPatternFeatureArray( 
   System.int FeatCount,
   System.Object^% ArrayDataIn
) 
```

#### Parameters

*FeatCount*
:   Number of seed features used to create this sketch pattern feature

*ArrayDataIn*
:   - in-process, unmanaged C+:: Pointer to an array of seed [features](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)
    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData.md)  
[ISketchPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData_members.md)  
[ISketchPatternFeatureData::GetPatternFeatureCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~GetPatternFeatureCount.md)  
[ISketchPatternFeatureData::IGetPatternFeatureArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~IGetPatternFeatureArray.md)  
[ISketchPatternFeatureData::PatternFeatureArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~PatternFeatureArray.md)  
[ISketchPatternFeatureData::BodyPattern Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~BodyPattern.md)
