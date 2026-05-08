# SetControlPointRadiusAtIndex Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetControlPointRadiusAtIndex`

Sets the radius at the specified control point.
Sets the radius at the specified control point.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetControlPointRadiusAtIndex( _
   ByVal Index As System.Integer, _
   ByVal Location As System.Double, _
   ByVal Radius As System.Double _
) 
```

```

Dim instance As IVariableFilletFeatureData2
Dim Index As System.Integer
Dim Location As System.Double
Dim Radius As System.Double
 
instance.SetControlPointRadiusAtIndex(Index, Location, Radius)
```

```

void SetControlPointRadiusAtIndex( 
   System.int Index,
   System.double Location,
   System.double Radius
)
```

```

void SetControlPointRadiusAtIndex( 
   System.int Index,
   System.double Location,
   System.double Radius
) 
```

#### Parameters

*Index*
:   Zero-based index of control point whose radius to set

*Location*
:   Percent distance between the edge start vertex and the edge end vertex

*Radius*
:   Value of the radius for the control point of this symmetric fillet; Distance 1 radius for the control point of this asymmetric fillet

Remarks

Call [IVariableFilletFeatureData2::SetControlPointDistanceAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetControlPointDistanceAtIndex.md) to set the Distance 2 radius for the control point of this asymmetric fillet.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.md)  
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.md)  
[IVariableFilletFeatureData2::GetControlPointRadiusAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetControlPointRadiusAtIndex.md)  
[IVariableFilletFeatureData2::GetControlPointsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetControlPointsCount.md)  
[IVariableFilletFeatureData2::SetControlPointConicRhoOrRadiusAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetControlPointConicRhoOrRadiusAtIndex.md)
