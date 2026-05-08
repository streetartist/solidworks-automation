# SetControlPointDistanceAtIndex Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetControlPointDistanceAtIndex`

Sets the Distance 2 radius at the specified control point for the asymmetric fillet.
Sets the Distance 2 radius at the specified control point for the asymmetric fillet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetControlPointDistanceAtIndex( _
   ByVal Index As System.Integer, _
   ByVal Dist2 As System.Double _
) 
```

```

Dim instance As IVariableFilletFeatureData2
Dim Index As System.Integer
Dim Dist2 As System.Double
 
instance.SetControlPointDistanceAtIndex(Index, Dist2)
```

```

void SetControlPointDistanceAtIndex( 
   System.int Index,
   System.double Dist2
)
```

```

void SetControlPointDistanceAtIndex( 
   System.int Index,
   System.double Dist2
) 
```

#### Parameters

*Index*
:   Zero-based index of control point whose radius to set

*Dist2*
:   Distance 2 radius for the control point of this asymmetric fillet

Remarks

Call [IVariableFilletFeatureData2::SetControlPointRadiusAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetControlPointRadiusAtIndex.md) to set the Distance 1 radius for the control point of this asymmetric fillet.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.md)  
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.md)  
[IVariableFilletFeatureData2::GetControlPointDistanceAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetControlPointDistanceAtIndex.md)
