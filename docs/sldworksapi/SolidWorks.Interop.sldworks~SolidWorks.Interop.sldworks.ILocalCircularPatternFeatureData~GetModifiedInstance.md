# GetModifiedInstance Method (ILocalCircularPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~GetModifiedInstance`

Gets the modified values for the specified pattern instance in this circular component pattern feature.
Gets the modified values for the specified pattern instance in this circular component pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GetModifiedInstance( _
   ByVal Instance As System.Integer, _
   ByRef AngleFromSeed As System.Double, _
   ByRef OffsetFromNominal As System.Double _
) 
```

```

Dim instance As ILocalCircularPatternFeatureData
Dim Instance As System.Integer
Dim AngleFromSeed As System.Double
Dim OffsetFromNominal As System.Double
 
instance.GetModifiedInstance(Instance, AngleFromSeed, OffsetFromNominal)
```

```

void GetModifiedInstance( 
   System.int Instance,
   out System.double AngleFromSeed,
   out System.double OffsetFromNominal
)
```

```

void GetModifiedInstance( 
   System.int Instance,
   [Out] System.double AngleFromSeed,
   [Out] System.double OffsetFromNominal
) 
```

#### Parameters

*Instance*
:   Pattern instance number (see **Remarks**)

*AngleFromSeed*
:   Angle from the pattern seed

*OffsetFromNominal*
:   Degree offset from the nominal position of Instance

Remarks

To specify Instance, you can use [ILocalCircularPatternFeatureData::GetModifiedInstances](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~GetModifiedInstances.md) to learn which pattern instances are modified.

To calculate Instance:

Calculate:

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

[ILocalCircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData.md)  
[ILocalCircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData_members.md)
