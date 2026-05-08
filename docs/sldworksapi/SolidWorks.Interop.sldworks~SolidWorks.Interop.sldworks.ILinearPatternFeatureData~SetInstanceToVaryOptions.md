# SetInstanceToVaryOptions Method (ILinearPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~SetInstanceToVaryOptions`

Sets the options for varying the spacing of pattern instances in this circular pattern feature.
Sets the options for varying the spacing of pattern instances in this circular pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetInstanceToVaryOptions( _
   ByVal InstancesToVaryObj As System.Object _
) As System.Boolean
```

```

Dim instance As ILinearPatternFeatureData
Dim InstancesToVaryObj As System.Object
Dim value As System.Boolean
 
value = instance.SetInstanceToVaryOptions(InstancesToVaryObj)
```

```

System.bool SetInstanceToVaryOptions( 
   System.object InstancesToVaryObj
)
```

```

System.bool SetInstanceToVaryOptions( 
   System.Object^ InstancesToVaryObj
) 
```

#### Parameters

*InstancesToVaryObj*
:   [IInstanceToVaryOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions.md)

#### Return Value

True if options successfully set, false if not

Remarks

This method is valid only if [ILinearPatternFeatureData::InstancesToVary](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~InstancesToVary.md) is true.

Example

See the [IInstanceToVaryOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.md)  
[ILinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData_members.md)  
[ILinearPatternFeatureData::GetInstanceToVaryOptions Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~GetInstanceToVaryOptions.md)
