# GetModifiedInstance Method (ILocalLinearPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~GetModifiedInstance`

Gets the modified values for the specified pattern instance in this linear component pattern feature.
Gets the modified values for the specified pattern instance in this linear component pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GetModifiedInstance( _
   ByVal Instance As System.Integer, _
   ByRef D1Distance As System.Double, _
   ByRef D1NominalVal As System.Double, _
   ByRef D2Distance As System.Double, _
   ByRef D2NominalVal As System.Double _
) 
```

```

Dim instance As ILocalLinearPatternFeatureData
Dim Instance As System.Integer
Dim D1Distance As System.Double
Dim D1NominalVal As System.Double
Dim D2Distance As System.Double
Dim D2NominalVal As System.Double
 
instance.GetModifiedInstance(Instance, D1Distance, D1NominalVal, D2Distance, D2NominalVal)
```

```

void GetModifiedInstance( 
   System.int Instance,
   out System.double D1Distance,
   out System.double D1NominalVal,
   out System.double D2Distance,
   out System.double D2NominalVal
)
```

```

void GetModifiedInstance( 
   System.int Instance,
   [Out] System.double D1Distance,
   [Out] System.double D1NominalVal,
   [Out] System.double D2Distance,
   [Out] System.double D2NominalVal
) 
```

#### Parameters

*Instance*
:   Pattern instance number (see **Remarks**)

*D1Distance*
:   Distance from the pattern seed in Direction 1

*D1NominalVal*
:   Offset from the nominal position of Instance in Direction 1

*D2Distance*
:   Distance from the pattern seed in Direction 2

*D2NominalVal*
:   Offset from the nominal position of Instance in Direction 2

Remarks

To specify Instance, you can use [ILocalLinearPatternFeatureData::GetModifiedInstances](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~GetModifiedInstances.md) to learn which pattern instances are modified.

To calculate Instance:

1. Ensure that [ILocalLinearPatternFeatureData::D2PatternSeedOnly](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D2PatternSeedOnly.md) is set to false.
2. Calculate:

      For a bi-directional pattern:

*I* = *n2* \* (*i* - 1) + (*j* - 1)

      For a uni-directional pattern:

*I* = *i* - 1

      where:

- *I* = pattern instance number
- *n2* = number of instances in Direction 2
- *i* = index for Direction 1
- *j* = index for Direction 2

> In the pattern's PropertyManager, find *n2* in the **Direction 2** **> Spacing and Instances > Number of instances** field and find [*i,j*] in the **Modified Instances** section.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILocalLinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData.md)  
[ILocalLinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData_members.md)
