# InsertVaryInstanceIncrement Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertVaryInstanceIncrement`

Obsolete. Superseded by IInstanceToVaryOptions.
Obsolete. Superseded by [IInstanceToVaryOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertVaryInstanceIncrement( _
   ByVal DName As System.String, _
   ByVal PatternType As System.Integer, _
   ByVal IncrementType As System.Integer, _
   ByVal Direction As System.Integer, _
   ByVal IncrementValue As System.Double _
) As System.Boolean
```

```

Dim instance As IFeatureManager
Dim DName As System.String
Dim PatternType As System.Integer
Dim IncrementType As System.Integer
Dim Direction As System.Integer
Dim IncrementValue As System.Double
Dim value As System.Boolean
 
value = instance.InsertVaryInstanceIncrement(DName, PatternType, IncrementType, Direction, IncrementValue)
```

```

System.bool InsertVaryInstanceIncrement( 
   System.string DName,
   System.int PatternType,
   System.int IncrementType,
   System.int Direction,
   System.double IncrementValue
)
```

```

System.bool InsertVaryInstanceIncrement( 
   System.String^ DName,
   System.int PatternType,
   System.int IncrementType,
   System.int Direction,
   System.double IncrementValue
) 
```

#### Parameters

*DName*
:   | If IncrementType is... | Then set DName to... |
    | --- | --- |
    | 1 | Name of the pattern instance dimension to increment |
    | 2 | "Spacing Increment" |

*PatternType*
:   Type of pattern (see **Remarks**):

    - 2 = linear
    - 4 = circular
    - 256 = table-driven

*IncrementType*
:   Type of increment:

    - 1 = dimension
    - 2 = spacing

*Direction*
:   Direction in which to apply the dimension or spacing increment.

    | If PatternType is... | Then set Direction to... |
    | --- | --- |
    | 2 | - 0 = direction 1  - 1 = direction 2 |
    | 4 | 0 = direction 1 |

*IncrementValue*
:   Value with which to increment the pattern instance dimension or spacing

#### Return Value

True if the increment is applied successfully, false if not

Remarks

To vary the spacings or dimensions of pattern instances:

1. Call this method multiple times to increment multiple dimensions or spacings of pattern instances.
2. Call [IFeatureManager::InsertVaryInstanceOverride](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertVaryInstanceOverride.md) multiple times to override multiple dimensions or spacings of pattern instances.

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
