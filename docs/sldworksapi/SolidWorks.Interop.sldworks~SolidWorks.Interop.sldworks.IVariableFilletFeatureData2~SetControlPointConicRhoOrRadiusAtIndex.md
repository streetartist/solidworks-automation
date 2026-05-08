# SetControlPointConicRhoOrRadiusAtIndex Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetControlPointConicRhoOrRadiusAtIndex`

Sets the conic rho or radius at the specified control point.
Sets the conic rho or radius at the specified control point.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetControlPointConicRhoOrRadiusAtIndex( _
   ByVal Index As System.Integer, _
   ByVal ConicRhoVal As System.Double _
) 
```

```

Dim instance As IVariableFilletFeatureData2
Dim Index As System.Integer
Dim ConicRhoVal As System.Double
 
instance.SetControlPointConicRhoOrRadiusAtIndex(Index, ConicRhoVal)
```

```

void SetControlPointConicRhoOrRadiusAtIndex( 
   System.int Index,
   System.double ConicRhoVal
)
```

```

void SetControlPointConicRhoOrRadiusAtIndex( 
   System.int Index,
   System.double ConicRhoVal
) 
```

#### Parameters

*Index*
:   Zero-based index of the control point for which to set ConicRhoVal (see **Remarks**)

*ConicRhoVal*
:   Conic rho or radius (see **Remarks**)

Remarks

Call [IVariableFilletFeatureData2::GetControlPointsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetControlPointsCount.md) before calling this method to determine a value for Index.

If [IVariableFilletFeatureData2::ConicTypeForCrossSectionProfile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~ConicTypeForCrossSectionProfile.md) is set to [swFeatureFilletProfileType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletProfileType_e.html).:

- swFeatureFilletConicRadius (symmetric fillet only), then specify ConicRhoVal with a radius.
- swFeatureFilletConicRho (symmetric or asymmetric fillet), then specify ConicRhoVal with the conic rho value in the range [0.05, 0.95].

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.md)  
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.md)  
[IVariableFilletFeatureData2::GetControlPointConicRhoOrRadiusAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~GetControlPointConicRhoOrRadiusAtIndex.md)  
[IVariableFilletFeatureData2::SetControlPointRadiusAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~SetControlPointRadiusAtIndex.md)
