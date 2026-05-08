# GetTransform Method (IDerivedPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData~GetTransform`

Gets the transform for the specified instance of this derived-pattern feature.
Gets the transform for the specified instance of this derived-pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTransform( _
   ByVal Instance As System.Integer _
) As MathTransform
```

```

Dim instance As IDerivedPatternFeatureData
Dim Instance As System.Integer
Dim value As MathTransform
 
value = instance.GetTransform(Instance)
```

```

MathTransform GetTransform( 
   System.int Instance
)
```

```

MathTransform^ GetTransform( 
   System.int Instance
) 
```

#### Parameters

*Instance*
:   Index of one repeating element in this pattern (see **Remarks**)

#### Return Value

[Transform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md)

Remarks

To get the number of instances in this pattern, get the number of subfeatures of the pattern by traversing the FeatureManager design tree, getting the derived-pattern feature, getting the derived-pattern feature's subfeatures, and keeping count of the number of subfeatures. You can use [IModelDoc2::FirstFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FirstFeature.md), [IFeature::GetFirstSubFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetFirstSubFeature.md), and [IFeature::GetNextSubFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetNextSubFeature.md) to traverse the FeatureManager design tree and get the derived-pattern feature's subfeatures.

Transform each instance by calling this method, setting its parameter *Instance* as follows:

        1 <= *Instance* <= total number of instances in this pattern

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDerivedPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData.md)  
[IDerivedPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData_members.md)  
[IDerivedPatternFeatureData::SkippedItemArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~SkippedItemArray.md)
