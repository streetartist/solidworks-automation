# GetD2ModifiedSpacingValue Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions~GetD2ModifiedSpacingValue`

Gets the modified spacing in Direction 2 of the specified pattern instance.
Gets the modified spacing in Direction 2 of the specified pattern instance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetD2ModifiedSpacingValue( _
   ByVal Instance As System.Integer _
) As System.Double
```

```

Dim instance As IInstanceToVaryOptions
Dim Instance As System.Integer
Dim value As System.Double
 
value = instance.GetD2ModifiedSpacingValue(Instance)
```

```

System.double GetD2ModifiedSpacingValue( 
   System.int Instance
)
```

```

System.double GetD2ModifiedSpacingValue( 
   System.int Instance
) 
```

#### Parameters

*Instance*
:   Pattern instance number (see **Remarks**)

#### Return Value

Spacing value in Direction 2

Remarks

To specify Instance, you can use [IInstanceToVaryOptions::GetModifiedInstances](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions~GetModifiedInstances.md) to learn which pattern instances are modified.

To calculate Instance:

1. Ensure that the D2PatternSeedOnly property in the pattern feature data object is set to false.
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

Example

See the [IInstanceToVaryOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IInstanceToVaryOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions.md)  
[IInstanceToVaryOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions_members.md)
