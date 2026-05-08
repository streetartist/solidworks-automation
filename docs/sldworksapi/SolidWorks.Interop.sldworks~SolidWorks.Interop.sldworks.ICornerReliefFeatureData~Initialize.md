# Initialize Method (ICornerReliefFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData~Initialize`

Initializes this corner relief feature to have specified corner relief bend type.
Initializes this corner relief feature to have specified corner relief bend type.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Initialize( _
   ByVal CornerType As System.Integer _
) As System.Boolean
```

```

Dim instance As ICornerReliefFeatureData
Dim CornerType As System.Integer
Dim value As System.Boolean
 
value = instance.Initialize(CornerType)
```

```

System.bool Initialize( 
   System.int CornerType
)
```

```

System.bool Initialize( 
   System.int CornerType
) 
```

#### Parameters

*CornerType*
:   Corner relief bend type as defined by [swCornerReliefBendType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerReliefBendType_e.html)

#### Return Value

True if the corner relief feature is initialized to the specified bend type, false if not

Example

See the [ICornerReliefFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICornerReliefFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData.md)  
[ICornerReliefFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData_members.md)  
[ICornerReliefFeatureData::CornerType Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData~CornerType.md)
