# RemoveCorner Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData~RemoveCorner`

Removes the specified corner from this corner relief feature.
Removes the specified corner from this corner relief feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function RemoveCorner( _
   ByVal CornerIndex As System.Integer _
) As System.Boolean
```

```

Dim instance As ICornerReliefFeatureData
Dim CornerIndex As System.Integer
Dim value As System.Boolean
 
value = instance.RemoveCorner(CornerIndex)
```

```

System.bool RemoveCorner( 
   System.int CornerIndex
)
```

```

System.bool RemoveCorner( 
   System.int CornerIndex
) 
```

#### Parameters

*CornerIndex*
:   One-based index of corner to remove

#### Return Value

True if specified corner successfully removed, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICornerReliefFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData.md)  
[ICornerReliefFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData_members.md)
