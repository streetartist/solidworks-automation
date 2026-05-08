# InsertVaryInstanceOverride Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertVaryInstanceOverride`

Obsolete. Superseded by IInstanceToVaryOptions.
Obsolete. Superseded by [IInstanceToVaryOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertVaryInstanceOverride( _
   ByVal DName As System.String, _
   ByVal PatternType As System.Integer, _
   ByVal OverrideType As System.Integer, _
   ByVal Direction As System.Integer, _
   ByVal InstanceRowIndex As System.Integer, _
   ByVal InstanceColumnIndex As System.Integer, _
   ByVal OverrideValue As System.Double _
) As System.Boolean
```

```

Dim instance As IFeatureManager
Dim DName As System.String
Dim PatternType As System.Integer
Dim OverrideType As System.Integer
Dim Direction As System.Integer
Dim InstanceRowIndex As System.Integer
Dim InstanceColumnIndex As System.Integer
Dim OverrideValue As System.Double
Dim value As System.Boolean
 
value = instance.InsertVaryInstanceOverride(DName, PatternType, OverrideType, Direction, InstanceRowIndex, InstanceColumnIndex, OverrideValue)
```

```

System.bool InsertVaryInstanceOverride( 
   System.string DName,
   System.int PatternType,
   System.int OverrideType,
   System.int Direction,
   System.int InstanceRowIndex,
   System.int InstanceColumnIndex,
   System.double OverrideValue
)
```

```

System.bool InsertVaryInstanceOverride( 
   System.String^ DName,
   System.int PatternType,
   System.int OverrideType,
   System.int Direction,
   System.int InstanceRowIndex,
   System.int InstanceColumnIndex,
   System.double OverrideValue
) 
```

#### Parameters

*DName*
:   | If OverrideType is... | Then set DName to... |
    | --- | --- |
    | 1 | Name of the pattern instance dimension to override |
    | 2 | "Spacing Increment" |

*PatternType*
:   Type of pattern (see **Remarks**):

    - 2 = linear
    - 4 = circular
    - 256 = variable

*OverrideType*
:   Type of increment override:

    - 1 = dimension
    - 2 = spacing

*Direction*
:   Direction in which to apply the spacing override.

    | If OverrideType is ... | Then set Direction to ... |
    | --- | --- |
    | 2 | - 0 = direction 1  - 1 = direction 2 |
    | 1 | -1 |

*InstanceRowIndex*
:   0 < row index of the instance to modify < number of instances per row

*InstanceColumnIndex*
:   0 < column index of the instance to modify < number of instances per column; valid only for PatternType = 2

*OverrideValue*
:   Value to override the current value of the dimension or spacing of the specified instance

#### Return Value

True if the override is applied successfully, false if not

Remarks

To vary the dimensions or spacings of pattern instances:

1. Call this method multiple times to override multiple dimensions or spacings of pattern instances.
2. Call [IFeatureManager::InsertVaryInstanceIncrement](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertVaryInstanceIncrement.md) multiple times to increment multiple dimensions or spacings of pattern instances.

| If PatternType is... | Call IFeatureManager::CreateFeature(...) |
| --- | --- |
| 2 | LinearPatternFeatureData object |
| 4 | CircularPatternFeatureData object |
| 256 | DimPatternFeatureData object |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)
