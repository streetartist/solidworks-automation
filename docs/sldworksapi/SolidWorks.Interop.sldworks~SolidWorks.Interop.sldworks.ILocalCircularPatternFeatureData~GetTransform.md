# GetTransform Method (ILocalCircularPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~GetTransform`

Gets the transform for the specified instance of this circular component pattern feature.
Gets the transform for the specified instance of this circular component pattern feature.

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

Dim instance As ILocalCircularPatternFeatureData
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

1 <= *Instance* <= [ILocalCircularPatternFeatureData::TotalInstances](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~TotalInstances.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILocalCircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData.md)  
[ILocalCircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData_members.md)
