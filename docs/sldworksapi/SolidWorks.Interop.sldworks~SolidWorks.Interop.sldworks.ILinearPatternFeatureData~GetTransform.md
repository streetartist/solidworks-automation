# GetTransform Method (ILinearPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~GetTransform`

Gets the transform for the specified instance of this linear pattern feature.
Gets the transform for the specified instance of this linear pattern feature.

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

Dim instance As ILinearPatternFeatureData
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

1 <= *Instance* <= ([ILinearPatternFeatureData::D1TotalInstances](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1TotalInstances.md) + [ILinearPatternFeatureData::D2TotalInstances](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D2TotalInstances.md))

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.md)  
[ILinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData_members.md)  
[ILinearPatternFeatureData::SkippedItemArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~SkippedItemArray.md)
