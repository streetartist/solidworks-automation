# SetEqualSpacing Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~SetEqualSpacing`

Sets equal spacing between each chain pattern instance in this chain pattern feature.
Sets equal spacing between each chain pattern instance in this chain pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetEqualSpacing() As System.Boolean
```

```

Dim instance As IChainPatternFeatureData
Dim value As System.Boolean
 
value = instance.SetEqualSpacing()
```

```

System.bool SetEqualSpacing()
```

```

System.bool SetEqualSpacing(); 
```

#### Return Value

True if equal spacing is set between each chain pattern instance, false if not

Remarks

This method is only available for distance and distance linkage chain patterns when [IChainPatternFeatureData::FillPath](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~FillPath.md) is false.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IChainPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData.md)  
[IChainPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData_members.md)  
[IChainPatternFeatureData::InstanceCount ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~InstanceCount.md)
