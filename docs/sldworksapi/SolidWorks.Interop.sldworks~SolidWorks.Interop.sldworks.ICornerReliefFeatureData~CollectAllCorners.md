# CollectAllCorners Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData~CollectAllCorners`

Creates corners, all with the specified relief, in a selected sheet-metal body.
Creates corners, all with the specified relief, in a selected sheet-metal body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CollectAllCorners( _
   ByVal ReliefType As System.Integer, _
   ByRef Corners As System.Object _
) As System.Integer
```

```

Dim instance As ICornerReliefFeatureData
Dim ReliefType As System.Integer
Dim Corners As System.Object
Dim value As System.Integer
 
value = instance.CollectAllCorners(ReliefType, Corners)
```

```

System.int CollectAllCorners( 
   System.int ReliefType,
   out System.object Corners
)
```

```

System.int CollectAllCorners( 
   System.int ReliefType,
   [Out] System.Object^ Corners
) 
```

#### Parameters

*ReliefType*
:   Corner relief type as defined by [swCornerReliefType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerReliefType_e.html)

*Corners*
:   Array of [ISMCornerReliefData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData.md)s

#### Return Value

Error code as defined by [swCornerReliefError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerReliefError_e.html)

Remarks

Before calling this method, call [ICornerReliefFeatureData::SetBodyScope](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData~SetBodyScope.md).

Example

See the [ICornerReliefFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICornerReliefFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData.md)  
[ICornerReliefFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData_members.md)
