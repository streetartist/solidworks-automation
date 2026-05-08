# GetCornerAtIndex Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData~GetCornerAtIndex`

Gets the corner at the specified index of this corner relief feature.
Gets the corner at the specified index of this corner relief feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCornerAtIndex( _
   ByVal CornerIndex As System.Integer, _
   ByRef Corner As System.Object _
) As System.Integer
```

```

Dim instance As ICornerReliefFeatureData
Dim CornerIndex As System.Integer
Dim Corner As System.Object
Dim value As System.Integer
 
value = instance.GetCornerAtIndex(CornerIndex, Corner)
```

```

System.int GetCornerAtIndex( 
   System.int CornerIndex,
   out System.object Corner
)
```

```

System.int GetCornerAtIndex( 
   System.int CornerIndex,
   [Out] System.Object^ Corner
) 
```

#### Parameters

*CornerIndex*
:   One-based index of corner to retrieve

*Corner*
:   [ISMCornerReliefData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData.md)

#### Return Value

Error code as defined by [swCornerReliefError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerReliefError_e.html)

Example

See the [ICornerReliefFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICornerReliefFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData.md)  
[ICornerReliefFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData_members.md)
