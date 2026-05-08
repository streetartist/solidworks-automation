# GetControlPointRadiusAtIndex Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetControlPointRadiusAtIndex`

Gets the radius at the specified control point.
Gets the radius at the specified control point.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetControlPointRadiusAtIndex( _
   ByVal Index As System.Integer, _
   ByRef Location As System.Double, _
   ByRef PEdge As Edge _
) As System.Double
```

```

Dim instance As IVariableFilletFeatureData2
Dim Index As System.Integer
Dim Location As System.Double
Dim PEdge As Edge
Dim value As System.Double
 
value = instance.GetControlPointRadiusAtIndex(Index, Location, PEdge)
```

```

System.double GetControlPointRadiusAtIndex( 
   System.int Index,
   out System.double Location,
   out Edge PEdge
)
```

```

System.double GetControlPointRadiusAtIndex( 
   System.int Index,
   [Out] System.double Location,
   [Out] Edge^ PEdge
) 
```

#### Parameters

*Index*
:   Zero-based index of the control point

*Location*
:   Location of the control point

*PEdge*
:   [Edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)

#### Return Value

Value of the radius at the specified control point for the symmetric fillet; value of the Distance 1 radius at the specified control point for the asymmetric fillet (see **Remarks**)

Remarks

Call [IVariableFilletFeatureData2::GetControlPointsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetControlPointsCount.md) before calling this method.

Call [IVariableFilletFeatureData2::GetControlPointDistanceAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetControlPointDistanceAtIndex.md) to get the Distance 2 radius for the control point of the asymmetric fillet.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.md)  
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.md)  
[IVariableFilletFeatureData2::SetControlPointRadiusAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetControlPointRadiusAtIndex.md)  
[IVariableFilletFeatureData2::GetControlPointConicRhoOrRadiusAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetControlPointConicRhoOrRadiusAtIndex.md)
