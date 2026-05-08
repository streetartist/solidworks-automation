# GetCorners Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData~GetCorners`

Gets all corners of the specified type in this corner relief feature.
Gets all corners of the specified type in this corner relief feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCorners( _
   ByVal CornerReliefType As System.Integer _
) As System.Object
```

```

Dim instance As ICornerReliefFeatureData
Dim CornerReliefType As System.Integer
Dim value As System.Object
 
value = instance.GetCorners(CornerReliefType)
```

```

System.object GetCorners( 
   System.int CornerReliefType
)
```

```

System.Object^ GetCorners( 
   System.int CornerReliefType
) 
```

#### Parameters

*CornerReliefType*
:   Corner relief type as defined by [swCornerReliefType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerReliefType_e.html)

#### Return Value

Array of [ISMCornerReliefData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData.md)s

Remarks

If CornerReliefType is specified with -1, then this method retrieves corners of all types.

Example

See the [ICornerReliefFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICornerReliefFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData.md)  
[ICornerReliefFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData_members.md)
