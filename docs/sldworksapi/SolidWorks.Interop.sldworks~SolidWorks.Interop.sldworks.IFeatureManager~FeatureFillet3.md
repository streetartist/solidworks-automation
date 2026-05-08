# FeatureFillet3 Method (IFeatureManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureFillet3`

Creates a fillet feature for selected edges and control point references.
Creates a fillet feature for selected edges and control point references.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function FeatureFillet3( _
   ByVal Options As System.Integer, _
   ByVal R1 As System.Double, _
   ByVal R2 As System.Double, _
   ByVal Rho As System.Double, _
   ByVal Ftyp As System.Integer, _
   ByVal OverflowType As System.Integer, _
   ByVal ConicRhoType As System.Integer, _
   ByVal Radii As System.Object, _
   ByVal Dist2Arr As System.Object, _
   ByVal RhoArr As System.Object, _
   ByVal SetBackDistances As System.Object, _
   ByVal PointRadiusArray As System.Object, _
   ByVal PointDist2Array As System.Object, _
   ByVal PointRhoArray As System.Object _
) As System.Object
```

```

Dim instance As IFeatureManager
Dim Options As System.Integer
Dim R1 As System.Double
Dim R2 As System.Double
Dim Rho As System.Double
Dim Ftyp As System.Integer
Dim OverflowType As System.Integer
Dim ConicRhoType As System.Integer
Dim Radii As System.Object
Dim Dist2Arr As System.Object
Dim RhoArr As System.Object
Dim SetBackDistances As System.Object
Dim PointRadiusArray As System.Object
Dim PointDist2Array As System.Object
Dim PointRhoArray As System.Object
Dim value As System.Object
 
value = instance.FeatureFillet3(Options, R1, R2, Rho, Ftyp, OverflowType, ConicRhoType, Radii, Dist2Arr, RhoArr, SetBackDistances, PointRadiusArray, PointDist2Array, PointRhoArray)
```

```

System.object FeatureFillet3( 
   System.int Options,
   System.double R1,
   System.double R2,
   System.double Rho,
   System.int Ftyp,
   System.int OverflowType,
   System.int ConicRhoType,
   System.object Radii,
   System.object Dist2Arr,
   System.object RhoArr,
   System.object SetBackDistances,
   System.object PointRadiusArray,
   System.object PointDist2Array,
   System.object PointRhoArray
)
```

```

System.Object^ FeatureFillet3( 
   System.int Options,
   System.double R1,
   System.double R2,
   System.double Rho,
   System.int Ftyp,
   System.int OverflowType,
   System.int ConicRhoType,
   System.Object^ Radii,
   System.Object^ Dist2Arr,
   System.Object^ RhoArr,
   System.Object^ SetBackDistances,
   System.Object^ PointRadiusArray,
   System.Object^ PointDist2Array,
   System.Object^ PointRhoArray
) 
```

#### Parameters

*Options*
:   Feature fillet options as defined in [swFeatureFilletOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletOptions_e.html) (see **Remarks**)

*R1*
:   Uniform radius of the symmetric fillet; valid only if:

    - Ftyp != swFeatureFilletType\_e.swFeatureFilletType\_VariableRadius
    - Options include swFeatureFilletOptions\_e.swFeatureFilletUniformRadius

    - or -

    Distance 1 radius of the asymmetric fillet; valid only if:

    - Options include swFeatureFilletOptions\_e.swFeatureFilletAsymmetric

*R2*
:   Distance 2 radius of the asymmetric fillet; valid only if:

    - Ftyp != swFeatureFilletType\_e.swFeatureFilletType\_VariableRadius
    - Options include swFeatureFilletOptions\_e.swFeatureFilletAsymmetric

*Rho*
:   Value that determines the conic rho or radius of the fillet:

    - Ftyp != swFeatureFilletType\_e.swFeatureFilletType\_VariableRadius
    - Conic rho value [0.05, 0.95], if ConicRhoType = swFeatureFilletProfileType\_e.swFeatureFilletConicRho
    - Conic radius value, if ConicRhoType = swFeatureFilletProfileType\_e.swFeatureFilletConicRadius

    (see **Remarks**)

*Ftyp*
:   Type of fillet as defined in [swFeatureFilletType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletType_e.html) (see **Remarks**)

*OverflowType*
:   Control of fillet overflowing onto adjacent surfaces as defined in [swFilletOverFlowType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFilletOverFlowType_e.html) (see **Remarks**)

*ConicRhoType*
:   Fillet cross-section profile as defined in [swFeatureFilletProfileType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletProfileType_e.html); valid only if Options does not include swFeatureFilletOptions\_e.swFeatureFilletCurvatureContinuous (see **Remarks**)

*Radii*
:   Array containing the radii for selected edges for the symmetric variable radius fillet; valid only if:

    - Ftyp = swFeatureFilletType\_e.swFeatureFilletType\_VariableRadius

    - or -

    Array containing the Distance 1 radii for selected edges for the asymmetric variable radius fillet; valid only if:

    - Ftyp = swFeatureFilletType\_e.swFeatureFilletType\_VariableRadius
    - Options include swFeatureFilletOptions\_e.swFeatureFilletAsymmetric

    (see **Remarks**)

*Dist2Arr*
:   Array containing the Distance 2 radii for selected edges for the asymmetric variable radius fillet; valid only if:

    - Ftyp = swFeatureFilletType\_e.swFeatureFilletType\_VariableRadius
    - Options include swFeatureFilletOptions\_e.swFeatureFilletAsymmetric

    (see **Remarks**)

*RhoArr*
:   Array of conic rho or radius values for the specified ConicRhoType for selected edges for the variable radius fillet; valid only if:

    - Conic rho value [0.05, 0.95], if ConicRhoType = swFeatureFilletProfileType\_e.swFeatureFilletConicRho
    - Conic radius value, if ConicRhoType = swFeatureFilletProfileType\_e.swFeatureFilletConicRadius
    - Ftyp = swFeatureFilletType\_e.swFeatureFilletType\_VariableRadius

    (see **Remarks**)

*SetBackDistances*
:   Array assigning setback distances on edges meeting at a selected fillet corner (see **Remarks**)

*PointRadiusArray*
:   Array containing control point radii along the lengths of the selected edges for the symmetric variable radius fillet; valid only if:

    - Ftyp = swFeatureFilletType\_e.swFeatureFilletType\_VariableRadius
    - Options include swFeatureFilletOptions\_e.swFeatureFilletVarRadiusType

    - or -

    Array containing Distance 1 control point radii along the lengths of the selected edges for the asymmetric variable radius fillet; valid only if:

    - Ftyp = swFeatureFilletType\_e.swFeatureFilletType\_VariableRadius
    - Options include swFeatureFilletOptions\_e.swFeatureFilletAsymmetric

    (see **Remarks**)

*PointDist2Array*
:   Array containing Distance 2 control point radii along the lengths of the selected edges for the asymmetric variable radius fillet; valid only if:

    - Ftyp = swFeatureFilletType\_e.swFeatureFilletType\_VariableRadius
    - Options include swFeatureFilletOptions\_e.swFeatureFilletAsymmetric

    (see **Remarks**)

*PointRhoArray*
:   Array of conic rho or radius values for the specified ConicRhoType at various control points along the lengths of the selected edges for the variable radius fillet; valid only if:

    - Conic rho value [0.05, 0.95], if ConicRhoType = swFeatureFilletProfileType\_e.swFeatureFilletConicRho
    - Conic radius value, if ConicRhoType = swFeatureFilletProfileType\_e.swFeatureFilletConicRadius
    - Ftyp = swFeatureFilletType\_e.swFeatureFilletType\_VariableRadius

    (see **Remarks**)

#### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

As of SOLIDWORKS 2020, this method is obsolete for creating:

- constant radius fillets
- offset face chamfers
- face fillets
- face-face chamfers
- full round fillets
- partial fillets
- partial chamfers

To create the fillet/chamfers above, use [IFeatureManager::CreateDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateDefinition.md), [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.md), IPartialEdgeFilletData, and [ISimpleFilletFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.md).

All of the parameter arrays of this method scale with the number of selected edges to fillet. Take care to populate and order the arrays meaningfully, or this method will fail.

If the conic rho values of Rho, RhoArray, or PointRhoArray are not in the valid range, then this method replaces them with the closest value in the valid range. For example, 0.01 is replaced by 0.05, and 0.99 is replaced by 0.95.

| To create... | You must... |
| --- | --- |
| Variable radius fillets | 1. Call [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) with Mark = 1 to select the edges to fillet. 2. Call IModelDocExtension::SelectByID2 with Mark = 256 to select the control point references along the lengths of the selected edges; select one control point reference for each radius in PointRadiusArray. 3. Specify Ftyp with swFeatureFilletType\_e.swFeatureFilletType\_VariableRadius. 4. (Optional) Specify OverflowType. 5. (Optional) Include swFeatureFilletOptions\_e.swFeatureFilletVarRadiusType in Options. 6. (Optional) Include swFeatureFilletOptions\_e.swFeatureFilletPropagate in Options. 7. (Optional) Include swFeatureFilletOptions\_e.swFeatureFilletCurvatureContinuous in Options. 8. (Optional) If Options does not include swFeatureFilletOptions\_e.swFeatureFilletCurvatureContinuous, then include swFeatureFilletOptions\_e.swFeatureFilletCornerType in Options. 9. (Optional) Include swFeatureFilletOptions\_e.swFeatureFilletKeepFeatures in Options. 10. If a **symmetric fillet**:       - If Options does not include swFeatureFilletOptions\_e.swFeatureFilletCurvatureContinuous, then specify ConicRhoType with swFeatureProfileType\_e.swFeatureFilletCircular, swFeatureFilletConicRadius, or swFeatureFilletConicRho.       - Specify Radii.       - If ConicRhoType is not swFeatureFilletProfileType\_e.swFeatureFilletCircular, then specify RhoArr with conic rho or radius values.       - Specify PointRadiusArray with multiple control point radii, one radius for each control point reference selected in step 2.       - If ConicRhoType is not swFeatureFilletProfileType\_e.swFeatureFilletCircular, then specify PointRhoArray with conic rho or radius values. 11. If an **asymmetric fillet**:       - If Options does not include swFeatureFilletOptions\_e.swFeatureFilletCurvatureContinuous, then specify ConicRhoType with swFeatureProfileType\_e.swFeatureFilletCircular or swFeatureFilletConicRho.         - Include swFeatureFilletOptions\_e.swFeatureFilletAsymmetric in Options.       - Specify Radii with the Distance 1 radii.       - Specify Dist2Array with the Distance 2 radii.       - If ConicRhoType is not swFeatureFilletProfileType\_e.swFeatureFilletCircular, then specify RhoArr with conic rho or radius values.       - Specify PointRadiusArray, one Distance 1 radius for each control point reference selected in step 2.        - Specify PointDist2Array, one Distance 2 radius for each control point reference selected in step 2.       - If ConicRhoType = swFeatureFilletProfileType\_e.swFeatureFilletConicRho, specify PointRhoArray with the conic rho values. |
| Setback fillets | 1. Follow the instructions above to create a variable radius fillet. 2. Call IModelDocExtension::SelectByID2 with Mark = 0 to select the vertex of the fillet corner whose setback parameters you want to set. 3. Specify SetBackDistances and call this method.   - or -    1. Call this method. 2. Use the setback methods on [IVariableFilletFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.md) to set the setback distances from setback vertices of multiple fillet corners. |

For more information, read the **Variable Size Fillets** topic in the SOLIDWORKS user-interface help.

Example

[Create Variable Radius Asymmetric Elliptical Fillet (VBA)](Create_Asymmetric_Elliptic_Fillets_Example_VB.htm)  
[Create Variable Radius Asymmetric Elliptical Fillet (VB.NET)](Create_Asymmetric_Elliptic_Fillets_Example_VBNET.htm)  
[Create Variable Radius Asymmetric Elliptical Fillet (C#)](Create_Asymmetric_Elliptic_Fillets_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IFeatureManager::FilletXpertChange Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FilletXpertChange.md)  
[IFeatureManager::FilletXpertMakeCorner Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FilletXpertMakeCorner.md)  
[IFeatureManager::FilletXpertRemove Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FilletXpertRemove.md)
