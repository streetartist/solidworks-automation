# GetControlPointDistanceAtIndex Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetControlPointDistanceAtIndex`

Gets the Distance 2 radius at the specified control point for the asymmetric fillet.
Gets the Distance 2 radius at the specified control point for the asymmetric fillet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetControlPointDistanceAtIndex( _
   ByVal Index As System.Integer _
) As System.Double
```

```

Dim instance As IVariableFilletFeatureData2
Dim Index As System.Integer
Dim value As System.Double
 
value = instance.GetControlPointDistanceAtIndex(Index)
```

```

System.double GetControlPointDistanceAtIndex( 
   System.int Index
)
```

```

System.double GetControlPointDistanceAtIndex( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Zero-based index of control point for which to get the radius

#### Return Value

Value of the Distance 2 radius at the specified control point for the asymmetric fillet

Remarks

Call [IVariableFilletFeatureData2::GetControlPointRadiusAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetControlPointRadiusAtIndex.md) to get the Distance 1 radius of the control point for this asymmetric fillet.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.md)  
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.md)  
[IVariableFilletFeatureData2::SetControlPointDistanceAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetControlPointDistanceAtIndex.md)
