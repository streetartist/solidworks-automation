# ModifyInstance Method (ILocalCircularPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~ModifyInstance`

Modifies the specified pattern instance with the specified angle in this circular component pattern feature.
Modifies the specified pattern instance with the specified angle in this circular component pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ModifyInstance( _
   ByVal Instance As System.Integer, _
   ByVal AngleFromSeed As System.Double, _
   ByVal IsOffsetFromNominal As System.Boolean _
) As System.Boolean
```

```

Dim instance As ILocalCircularPatternFeatureData
Dim Instance As System.Integer
Dim AngleFromSeed As System.Double
Dim IsOffsetFromNominal As System.Boolean
Dim value As System.Boolean
 
value = instance.ModifyInstance(Instance, AngleFromSeed, IsOffsetFromNominal)
```

```

System.bool ModifyInstance( 
   System.int Instance,
   System.double AngleFromSeed,
   System.bool IsOffsetFromNominal
)
```

```

System.bool ModifyInstance( 
   System.int Instance,
   System.double AngleFromSeed,
   System.bool IsOffsetFromNominal
) 
```

#### Parameters

*Instance*
:   Pattern instance number (see **Remarks**)

*AngleFromSeed*
:   Angle from the pattern seed

*IsOffsetFromNominal*
:   True if AngleFromSeed is the offset from the nominal position of Instance, false if not

#### Return Value

True if the pattern instance is modified successfully, false if not

Remarks

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
