# SetInstanceToVaryOptions Method (ICircularPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~SetInstanceToVaryOptions`

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

Dim instance As ICircularPatternFeatureData
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

This method is valid only if [ICircularPatternFeatureData::InstancesToVary](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~InstancesToVary.md) is true.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData.md)  
[ICircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData_members.md)  
[ICircularPatternFeatureData::GetInstanceToVaryOptions Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~GetInstanceToVaryOptions.md)
