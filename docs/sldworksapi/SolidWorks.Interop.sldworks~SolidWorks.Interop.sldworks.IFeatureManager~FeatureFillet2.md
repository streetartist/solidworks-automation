# FeatureFillet2 Method (IFeatureManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureFillet2`

Obsolete. Superseded by IFeatureManager::FeatureFillet3.
Obsolete. Superseded by [IFeatureManager::FeatureFillet3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureFillet3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function FeatureFillet2( _
   ByVal Options As System.Integer, _
   ByVal R1 As System.Double, _
   ByVal Rho As System.Double, _
   ByVal Ftyp As System.Integer, _
   ByVal OverflowType As System.Integer, _
   ByVal ConicRhoType As System.Integer, _
   ByVal Radii As System.Object, _
   ByVal RhoArr As System.Object, _
   ByVal SetBackDistances As System.Object, _
   ByVal PointRadiusArray As System.Object, _
   ByVal PointRhoArray As System.Object _
) As System.Object
```

```

Dim instance As IFeatureManager
Dim Options As System.Integer
Dim R1 As System.Double
Dim Rho As System.Double
Dim Ftyp As System.Integer
Dim OverflowType As System.Integer
Dim ConicRhoType As System.Integer
Dim Radii As System.Object
Dim RhoArr As System.Object
Dim SetBackDistances As System.Object
Dim PointRadiusArray As System.Object
Dim PointRhoArray As System.Object
Dim value As System.Object
 
value = instance.FeatureFillet2(Options, R1, Rho, Ftyp, OverflowType, ConicRhoType, Radii, RhoArr, SetBackDistances, PointRadiusArray, PointRhoArray)
```

```

System.object FeatureFillet2( 
   System.int Options,
   System.double R1,
   System.double Rho,
   System.int Ftyp,
   System.int OverflowType,
   System.int ConicRhoType,
   System.object Radii,
   System.object RhoArr,
   System.object SetBackDistances,
   System.object PointRadiusArray,
   System.object PointRhoArray
)
```

```

System.Object^ FeatureFillet2( 
   System.int Options,
   System.double R1,
   System.double Rho,
   System.int Ftyp,
   System.int OverflowType,
   System.int ConicRhoType,
   System.Object^ Radii,
   System.Object^ RhoArr,
   System.Object^ SetBackDistances,
   System.Object^ PointRadiusArray,
   System.Object^ PointRhoArray
) 
```

#### Parameters

*Options*
:   Feature fillet options as defined in [swFeatureFilletOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletOptions_e.html)

*R1*
:   Uniform radius of the fillet; valid only if:

    - Ftyp != [swFeatureFilletType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletType_e.html).swFeatureFilletType\_VariableRadius
    - Options include [swFeatureFilletOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletOptions_e.html).swFeatureFilletUniformRadius

*Rho*
:   Value that determines the conic shape of the fillet:

    - Conic rho value [0.05, 0.95], if ConicRhoType = [swFeatureFilletProfileType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletProfileType_e.html).swFeatureFilletConicRho (see **Remarks**)
    - Conic radius value, if ConicRhoType = swFeatureFilletProfileType\_e.swFeatureFilletConicRadius
    - Circular radius value, if ConicRhoType = swFeatureFilletProfileType\_e.swFeatureFilletCircular

*Ftyp*
:   Type of fillet as defined in [swFeatureFilletType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletType_e.html) (see **Remarks**)

*OverflowType*
:   Control of fillet overflowing onto adjacent surfaces as defined in [swFilletOverFlowType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFilletOverFlowType_e.html)

*ConicRhoType*
:   Conic fillet profile type as defined in [swFeatureFilletProfileType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletProfileType_e.html)

*Radii*
:   Array containing the radii for the variable radius fillet; valid only if:

    - Ftyp = [swFeatureFilletType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletType_e.html).swFeatureFilletType\_VariableRadius
    - Options include [swFeatureFilletOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletOptions_e.html).swFeatureFilletVarRadiusType
    - Options do not include [swFeatureFilletOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletOptions_e.html).swFeatureFilletUniformRadius

*RhoArr*
:   Array of Rho values for the specified ConicRhoType for the variable radius fillet; valid only if:

    - Ftyp = [swFeatureFilletType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletType_e.html).swFeatureFilletType\_VariableRadius
    - Options include [swFeatureFilletOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletOptions_e.html).swFeatureFilletVarRadiusType
    - Options do not include [swFeatureFilletOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletOptions_e.html).swFeatureFilletUniformRadius

*SetBackDistances*
:   Array containing setback distances along the fillet edge

*PointRadiusArray*
:   Array containing radii at various control points along the length of the edge; valid only if Ftyp = [swFeatureFilletType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletType_e.html).swFeatureFilletType\_VariableRadius

*PointRhoArray*
:   Array of Rho values for the specified ConicRhoType at various control points along the length of the edge; valid only if Ftyp = [swFeatureFilletType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletType_e.html).swFeatureFilletType\_VariableRadius

#### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

If the conic rho value specified in parameter, Rho, is not in the valid range, then this method replaces it with the closest value in the valid range. For example, 0.01 is replaced by 0.05, and 0.99 is replaced by 0.95.

| Before calling this method to create... | You must... |
| --- | --- |
| Simple fillets | 1. Call [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) with Mark = 1 to select the edges to fillet. 2. Specify Ftyp with [swFeatureFilletType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletType_e.html).swFeatureFilletType\_Simple. |
| Face blend fillets | 1. Call IModelDocExtension::SelectByID2 with:   - Mark = 2 to select the first set of faces. - Mark = 4 to select the second set of faces.   1. Specify Ftyp with [swFeatureFilletType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletType_e.html).swFeatureFilletType\_Face. |
| Variable radius fillets | 1. Call IModelDocExtension::SelectByID2 with Mark = 1 to select the edges to fillet. 2. Call IModelDocExtension::SelectByID2 with Mark = 256 to select the control point references along the length of the selected edge; one control point reference for each radius in PointRadiusArray. 3. Specify Ftyp with [swFeatureFilletType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletType_e.html).swFeatureFilletType\_VariableRadius. 4. Specify multiple radii in Radii. 5. Specify multiple control point radii in PointRadiusArray. 6. Do not include [swFeatureFilletOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletOptions_e.html).swFilletUniformRadius in Options. |
| Full-round fillets | 1. Call IModelDocExtension::SelectByID2 with:   - Mark = 2 to select the first set of side faces. - Mark = 512 to select the set of center faces. - Mark = 4 to select the second set of side faces.   1. Specify Ftyp with [swFeatureFilletType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletType_e.html).swFeatureFilletType\_FullRound. |
| Setback fillets | See the SOLIDWORKS Help for details. |
| Conic fillets | See the SOLIDWORKS Help for details. |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IFeatureManager::IFeatureFillet2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~IFeatureFillet2.md)  
[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.md)  
[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.md)  
[IFeatureManager::FilletXpertChange Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FilletXpertChange.md)  
[IFeatureManager::FilletXpertMakeCorner Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FilletXpertMakeCorner.md)  
[IFeatureManager::FilletXpertRemove Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FilletXpertRemove.md)
