# ISimpleFilletFeatureData2 Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2`

Allows access to a simple fillet feature.
Allows access to a simple fillet feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface ISimpleFilletFeatureData2 
```

```

Dim instance As ISimpleFilletFeatureData2
```

```

public interface ISimpleFilletFeatureData2 
```

```

public interface class ISimpleFilletFeatureData2 
```

Remarks

To create a simple fillet feature:

1. Call [IFeatureManager::CreateDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateDefinition.md), passing Type = [swFeatureNameID\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureNameID_e.html).swFmFillet, to create an instance of ISimpleFilletFeatureData2.
2. Initialize the fillet/chamfer to a simple fillet type as follows:  
      

   | For... | Call [ISimpleFilletFeatureData2::Initialize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~Initialize.md),  passing FilletType = [swSimpleFilletType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSimpleFilletType_e.html)... |
   | --- | --- |
   | - Constant radius fillet - Offset face chamfer | swConstRadiusFillet |
   | - Face fillet - Face-face chamfer | swFaceFillet |
   | Full round fillet | swFullRoundFillet |
3. Complete the fillet/chamfer type specification by specifying a feature fillet profile type:  
     

   | For... | Set [ISimpleFilletFeatureData2::ConicTypeForCrossSectionProfile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ConicTypeForCrossSectionProfile.md)   to [swFeatureFilletProfileType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletProfileType_e.html).... |
   | --- | --- |
   | Constant radius fillet | - swFeatureFilletCircular (symmetric or asymmetric) - swFeatureFilletConicRho (symmetric or asymmetric) - swFeatureFilletConicRadius (symmetric) |
   | Offset face chamfer | swFeatureFilletConicRhoZeroChamfer |
   | Face fillet | - swFeatureFilletCircular (symmetric, asymmetric, chord width, or hold line) - swFeatureFilletConicRho (symmetric, asymmetric, or chord width) - swFeatureFilletConicRadius (symmetric or chord width) |
   | Face-face chamfer | swFeatureFilletConicRhoZeroChamfer |
   | Full round fillet | swFeatureFilletCircular |
4. Specify other ISimpleFilletFeatureData2 properties as follows:.

   | To create... | You must... |
   | --- | --- |
   | Constant radius fillet/offset face chamfer | 1. Call [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) with Mark = 1 to select the edges, faces, features, or loops to fillet. 2. Set [ISimpleFilletFeatureData2::OverflowType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~OverflowType.md). 3. (Optional) For both fillets and chamfers, set [ISimpleFilletFeatureData2::KeepFeatures](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~KeepFeatures.md) and [ISimpleFilletFeatureData2::PropagateToTangentFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~PropagateToTangentFaces.md). 4. (Optional) For fillets only, set [ISimpleFilletFeatureData2::RoundCorners](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~RoundCorners.md), [ISimpleFilletFeatureData2::ConstantWidth](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ConstantWidth.md), and [ISimpleFilletFeatureData2::CurvatureContinuous](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~CurvatureContinuous.md) (if set to true, then ISimpleFilletFeatureData2::RoundCorners and ISimpleFilletFeatureData2::ConicTypeForCrossSectionProfile are not valid). 5. If a **symmetric fillet/chamfer**:     - For fillets or chamfers, set [ISimpleFilletFeatureData2::DefaultRadius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~DefaultDistance.md) to a default fillet radius or chamfer offset distance.     - For fillets, if ISimpleFilletFeatureData2::CurvatureContinuous is false and  ISimpleFilletFeatureData2::ConicTypeForCrossSectionProfile is set to swFeatureFilletCircular, then you can set [ISimpleFilletFeatureData2::IsMultipleRadius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IsMultipleRadius.md). If MultipleRadius is set to true, then you can call [ISimpleFilletFeatureData2::SetRadius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~SetRadius.md) to specify multiple edge radii. If ISimpleFilletFeatureData2::CurvatureContinuous is false and  ISimpleFilletFeatureData2::ConicTypeForCrossSectionProfile is set to swFeatureFilletConicRho or swFeatureFilletConicRadius, set [ISimpleFilletFeatureData2::DefaultConicRhoOrRadius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~DefaultConicRhoOrRadius.md) to a conic rho value between 0.05 and 0.95, inclusive, or a conic radius value, respectively.      - For chamfers, if ISimpleFilletFeatureData2::IsMultipleRadius is set to true, then you can call ISimpleFilletFeatureData2::SetRadius to set multiple offset distances. 6. If an **asymmetric fillet/chamfer**:      - Set [ISimpleFilletFeatureData2::AsymmetricFillet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~AsymmetricFillet.md).        - Set ISimpleFilletFeatureData2::DefaultRadius to the fillet Distance 1 radius or chamfer Offset Distance 1.         - Set [ISimpleFilletFeatureData2::DefaultDistance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~DefaultDistance.md) to the fillet Distance 2 radius or chamfer Offset Distance 2.         - For fillets only, if ISimpleFilletFeatureData2::CurvatureContinuous is false and  ISimpleFilletFeatureData2::ConicTypeForCrossSectionProfile is set to swFeatureFilletConicRho, set ISimpleFilletFeatureData2::DefaultConicRhoOrRadius to a conic rho value between 0.05 and 0.95, inclusive.  For more information, see the **Constant Size Fillets** and **Chamfer PropertyManager** topics in the SOLIDWORKS user-interface help. |
   | Face fillet/face-face chamfer | 1. Call IModelDocExtension::SelectByID2 with:  - Mark = 2 to select Face Set 1.   - Mark = 4 to select Face Set 2.  1. (Optional) For both fillets and chamfers, set ISimpleFilletFeatureData2::PropagateToTangentFaces and [ISimpleFilletFeatureData2::HelpPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~HelpPoint.md). 2. (Optional) For fillets only, set ISimpleFilletFeatureData2::CurvatureContinuous (if set to true, then ISimpleFilletFeatureData2::ConicTypeForCrossSectionProfile is not valid). 3. If a **symmetric fillet/chamfer**:      - Set ISimpleFilletFeatureData2::DefaultRadius for the fillet radius or the chamfer offset distance.      - For fillets only, if ISimpleFilletFeatureData2::CurvatureContinuous is false and ISimpleFilletFeatureData2::ConicTypeForCrossSectionProfile is set to swFeatureFilletConicRho or swFeatureFilletConicRadius, set ISimpleFilletFeatureData2::DefaultConicRhoOrRadius to a conic rho or conic radius value. 4. If a **chord width fillet/chamfer**:      - Set ISimpleFilletFeatureData2::DefaultRadius to set the chord width.      - For fillets only, if ISimpleFilletFeatureData2::CurvatureContinuous is false and ISimpleFilletFeatureData2::ConicTypeForCrossSectionProfile is set to swFeatureFilletConicRho or swFeatureFilletConicRadius, set ISimpleFilletFeatureData2::DefaultConicRhoOrRadius to a conic rho or conic radius value. 5. If an **asymmetric fillet/chamfer**:      - Set ISimpleFilletFeatureData2::AsymmetricFillet.      - Set ISimpleFilletFeatureData2::DefaultRadius to the fillet Distance 1 radius or the chamfer Offset Distance 1.      - Set ISimpleFilletFeatureData2::DefaultDistance to the fillet Distance 2 radius or the chamfer Offset Distance 2.      - For fillets only, if ISimpleFilletFeatureData2::CurvatureContinuous is false and ISimpleFilletFeatureData2::ConicTypeForCrossSectionProfile is set to swFeatureFilletConicRho, set ISimpleFilletFeatureData2::DefaultConicRhoOrRadius to a conic rho value. 6. If a **hold line fillet/chamfer**:      - Call IModelDocExtension::SelectByID2 with Mark = 8 to select the hold line edges.      - Set [ISimpleFilletFeatureData2::HoldLines](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~HoldLines.md) to the hold line edges. For more information, see the **Face Fillets** and **Chamfer PropertyManager** topics in the SOLIDWORKS user-interface help. |
   | Full round fillet | 1. Call IModelDocExtension::SelectByID2 with:      - Mark = 2 to select Face Set 1.      - Mark = 512 to select Center Face Set.      - Mark = 4 to select Face Set 2. 2. (Optional) Set ISimpleFilletFeatureData2::PropagateToTangentFaces. For more information, see the **Full Round Fillets** topic in the SOLIDWORKS user-interface help. |
   | Setback fillet | 1. Follow the instructions above to create a constant radius fillet. 2. Use the setback methods on ISimpleFilletFeatureData2 to set the setback distances from setback vertices of fillet corners. For more information, see the **Constant Size Fillets** topic in the SOLIDWORKS user-interface help. |
   | Partial edge fillet/chamfer | 1. Follow the instructions above to create a constant radius fillet or offset face chamfer. 2. Set [ISimpleFilletFeatureData2::EnablePartialEdgeParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~EnablePartialEdgeParameters.md) to true. 3. Call [ISimpleFilletFeatureData2::GetPartialEdgeFilletData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetPartialEdgeFilletData.md). 4. Set other properties of IPartialEdgeFilletData as required. 5. Call [ISimpleFilletFeatureData2::SetPartialEdgeFilletData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~SetPartialEdgeFilletData.md), passing in the IPartialEdgeFilletData populated in step d. 6. Repeat steps c-e for each edge to partially fillet. For more information, see the **Constant Size Fillets** and **Chamfer PropertyManager** topics in the SOLIDWORKS user-interface help. |
5. Create the fillet/chamfer feature by calling [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.md).

For more information about fillets, see the **Fillets** topic in the SOLIDWORKS user-interface help.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Example

'VBA

'Preconditions: Open *Public\_documents***\SOLIDWORKS\SOLIDWORKS 2020\samples\tutorial\api\cube.sldprt**.

'Postconditions:

'1. Creates an asymmetric face fillet between the selected faces.

'2. Inspect the graphics area.

'NOTE: Because the model is used elsewhere, do not save changes to it.

'===============================================================

Dim swApp As SldWorks.SldWorks  
Dim swModel As SldWorks.ModelDoc2  
Dim swModelDocExt As SldWorks.ModelDocExtension  
Dim swFeatMgr As SldWorks.FeatureManager  
Dim swFeat As SldWorks.Feature  
Dim swFilletData As SldWorks.SimpleFilletFeatureData2  
Dim swFeatDataObj As Object  
Dim boolstatus As Boolean

Option Explicit

Sub main()  
    Set swApp = Application.SldWorks  
    Set swModel = swApp.ActiveDoc  
    Set swModelDocExt = swModel.Extension  
    Set swFeatMgr = swModel.FeatureManager  
     
    ' Create the fillet feature data object  
    Set swFeatDataObj = swFeatMgr.**CreateDefinition**(swFmFillet)  
    Set swFilletData = swFeatDataObj  
        
    ' Initialize the fillet feature data object with a simple fillet type  
    swFilletData.**Initialize** swFaceFillet  
     
    ' Select adjacent faces using Marks 2 and 4  
    boolstatus = swModel.Extension.SelectByRay(-8.1276449166694E-03, 7.23380744250335E-02, 5.97881679346983E-02, -0.400036026779312, -0.515038074910024, -0.758094294050284, 2.27210389793168E-03, 2, False, 2, 0)  
    boolstatus = swModel.Extension.SelectByRay(5.01369231146214E-02, 6.23282644744449E-03, 5.13547742943388E-02, -0.400036026779312, -0.515038074910024, -0.758094294050284, 2.27210389793168E-03, 2, True, 4, 0)  
    swFilletData.**AsymmetricFillet** = True  
    swFilletData.**DefaultRadius** = 0.01  
    swFilletData.**DefaultDistance** = 0.02  
     
    ' Narrow the fillet type by specifying the feature fillet profile type  
    swFilletData.**ConicTypeForCrossSectionProfile** = swFeatureFilletCircular  
     
    ' Create the fillet feature  
    Set swFeat = swFeatMgr.**CreateFeature**(swFilletData)  
End Sub

Example

[Get Data for Fillet Feature (VBA)](Get_Data_for_Simple_Fillet_Example_VB.htm)  
[Get Data for Fillet Feature (VB.NET)](Get_Data_for_Simple_Fillet_Example_VBNET.htm)  
[Get Data for Fillet Feature (C#)](Get_Data_for_Simple_Fillet_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IChamferFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2.md)  
[IFeatureManager::FilletXpertChange Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FilletXpertChange.md)  
[IFeatureManager::FilletXpertMakeCorner Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FilletXpertMakeCorner.md)  
[IFeatureManager::FilletXpertRemove Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FilletXpertRemove.md)  
[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.md)  
[IPartialEdgeFilletData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData.md)
