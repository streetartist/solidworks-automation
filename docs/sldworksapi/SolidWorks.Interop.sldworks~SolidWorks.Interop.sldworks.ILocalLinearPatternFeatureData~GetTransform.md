# GetTransform Method (ILocalLinearPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~GetTransform`

Gets the transform for the specified instance of this linear component pattern feature.
Gets the transform for the specified instance of this linear component pattern feature.

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

Dim instance As ILocalLinearPatternFeatureData
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

1 <= *Instance* <= ([ILocalLinearPatternFeatureData::D1TotalInstances](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D1TotalInstances.md) + [ILocalLinearPatternFeatureData::D2TotalInstances](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D2TotalInstances.md))

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILocalLinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData.md)  
[ILocalLinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData_members.md)  
[ILocalLinearPatternFeatureData::SkippedItemArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~SkippedItemArray.md)
