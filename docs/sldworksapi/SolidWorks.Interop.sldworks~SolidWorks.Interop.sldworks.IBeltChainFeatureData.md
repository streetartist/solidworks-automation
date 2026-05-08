# IBeltChainFeatureData Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData`

Allows access to a Belt/Chain assembly feature.
Allows access to a Belt/Chain assembly feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IBeltChainFeatureData 
```

```

Dim instance As IBeltChainFeatureData
```

```

public interface IBeltChainFeatureData 
```

```

public interface class IBeltChainFeatureData 
```

Remarks

For more information, see the **SOLIDWORKS user-interface help > Assemblies > Other Assembly Techniques > Assembly Features > Creating Assembly Features >**

- **Creating a Belt/Chain Assembly Feature**
- **Belt/Chain PropertyManager (Assemblies)**

Example

'VBA

'=====================================================================  
'Preconditions: Ensure the specified assembly template and part exist.  
'  
'Postconditions:  
'1. Creates an assembly of two steel discs.  
'2. Press F5 to create **Belt1** in the FeatureManager design tree.  
'   If a Save As dialog appears, click **Cancel**.  
'3. Press F5 to modify **Belt1**'s belt length, belt thickness,  
'   and pulley diameters. If a Save As dialog appears, click **Cancel**.  
'============================================================  
Dim swApp As SldWorks.SldWorks  
Dim swModel As SldWorks.ModelDoc2  
Dim selMgr As SldWorks.SelectionMgr  
Dim beltChainFeatData As SldWorks.BeltChainFeatureData  
Dim pulleyComps(1) As Object  
Dim pulleyDiams(1) As Double  
Dim pullyFlips(1) As Boolean  
Dim pulleyRefsOri As Variant  
Dim pulleyDiamsOri As Variant  
Dim swFeat As SldWorks.Feature  
Dim swFeatData As SldWorks.BeltChainFeatureData  
Dim BeltLocationPlane As SldWorks.Face2  
Dim beltPart As SldWorks.PartDoc  
Dim index As Long  
Dim I As Long  
Dim J As Long  
Dim boolstatus As Boolean  
Dim longstatus As Long, longwarnings As Long

Option Explicit  
Sub main()

    Set swApp = Application.SldWorks  
     
    ' New assembly  
     
    Dim swSheetWidth As Double  
    swSheetWidth = 0  
    Dim swSheetHeight As Double  
    swSheetHeight = 0  
    Set swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2022\templates\Assembly.asmdot", 0, swSheetWidth, swSheetHeight)  
    Dim swAssembly As AssemblyDoc  
    Set swAssembly = swModel  
     
    ' Insert steel disc component  
     
    Dim AssemblyTitle As String  
    AssemblyTitle = swModel.GetTitle  
    Dim tmpObj As ModelDoc2  
    Dim errors As Long  
    Set tmpObj = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2022\samples\tutorial\api\AdvancedMates\steel disc.sldprt", 1, 1, "", errors, longwarnings)  
    Set swModel = swApp.ActivateDoc3(AssemblyTitle, True, 0, errors)  
    Dim swInsertedComponent As Component2  
    Set swInsertedComponent = swModel.AddComponent5("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2022\samples\tutorial\api\AdvancedMates\steel disc.sldprt", 0, "", False, "", 4.04421078452853E-03, 4.04421078422676E-03, 1.22628871084471E-02)  
    swApp.CloseDoc "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2021\samples\tutorial\api\AdvancedMates\steel disc.sldprt"  
     
    ' Insert steel disc component  
     
    AssemblyTitle = swModel.GetTitle  
    Set tmpObj = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2022\samples\tutorial\api\AdvancedMates\steel disc.sldprt", 1, 1, "", errors, longwarnings)  
    Set swModel = swApp.ActivateDoc3(AssemblyTitle, True, 0, errors)  
    Set swInsertedComponent = swModel.AddComponent5("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2022\samples\tutorial\api\AdvancedMates\steel disc.sldprt", 0, "", False, "", 2.00044210784528E-02, 2.00044210784227E-02, 1.22628871084471E-02)  
    swApp.CloseDoc "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2021\samples\tutorial\api\AdvancedMates\steel disc.sldprt"  
    
    ' Float the components  
     
    boolstatus = swModel.Extension.SelectByID2("steel disc-1", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)  
    swModel.UnfixComponent  
    swModel.ClearSelection2 True  
    boolstatus = swModel.Extension.SelectByID2("steel disc-2", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)  
    swModel.UnfixComponent  
    swModel.ClearSelection2 True  
     
    ' Move one disc  
     
    boolstatus = swModel.Extension.SelectByID2("steel disc-2@Assem14", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)  
    boolstatus = swModel.Extension.SelectByID2("Unknown", "MANIPULATOR", 3.40009836225566E-02, -3.52899570186584E-03, -1.15173288530189E-02, False, 0, Nothing, 0)  
    swModel.ClearSelection2 True  
    boolstatus = swModel.Extension.SelectByID2("steel disc-2@Assem14", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)  
    Dim TransformData() As Double  
    ReDim TransformData(0 To 15) As Double  
    TransformData(0) = 1  
    TransformData(1) = 0  
    TransformData(2) = 0  
    TransformData(3) = 0  
    TransformData(4) = 1  
    TransformData(5) = 0  
    TransformData(6) = 0  
    TransformData(7) = 0  
    TransformData(8) = 1  
    TransformData(9) = 6.64528131333411E-02  
    TransformData(10) = 4.6349356621274E-03  
    TransformData(11) = 9.19716533133533E-03  
    TransformData(12) = 1  
    TransformData(13) = 0  
    TransformData(14) = 0  
    TransformData(15) = 0  
    Dim TransformDataVariant As Variant  
    TransformDataVariant = TransformData  
    Dim swMathUtil As Object  
    Set swMathUtil = swApp.GetMathUtility()  
    Dim swTransForm As Object  
    Set swTransForm = swMathUtil.CreateTransform((TransformDataVariant))  
    Dim swComp As Object  
    Set swComp = swModel.SelectionManager.GetSelectedObjectsComponent4(1, -1)  
    boolstatus = swComp.SetTransformAndSolve2(swTransForm)  
    boolstatus = swModel.ForceRebuild3(False)  
    swModel.ClearSelection2 True  
     
    ' Select the pulley faces  
     
    boolstatus = swModel.Extension.SelectByRay(1.30157615084272E-02, 9.90176398499898E-03, 1.21640119419908E-02, -0.333333333266778, -0.333333333254022, -0.881917103743329, 9.73554376657825E-04, 2, False, 0, 0)  
    boolstatus = swModel.Extension.SelectByRay(7.69710902559098E-02, 6.67589089525222E-03, 1.12969076145077E-02, -0.333333333266778, -0.333333333254022, -0.881917103743329, 9.73554376657825E-04, 2, False, 0, 0)

    Set selMgr = swModel.SelectionManager  
     
    For I = 0 To UBound(pulleyComps)  
    Set pulleyComps(I) = selMgr.GetSelectedObject6(I + 1, -1)  
    Next  
     
    ' Create Belt/Chain feature  
     
    Set beltChainFeatData = swModel.FeatureManager.**CreateDefinition**(swFmBeltAndChain)  
     
    For J = 0 To UBound(pulleyComps)  
    pulleyDiams(J) = 0.005 \* (J + 2)  
    Next  
     
    beltChainFeatData.**PulleyComponents** = pulleyComps  
    beltChainFeatData.**PulleyDiameters** = pulleyDiams  
     
    pullyFlips(0) = False  
    pullyFlips(1) = False  
     
    beltChainFeatData.**FlipSides** = pullyFlips  
     
    beltChainFeatData.**BeltLocationPlane** = selMgr.GetSelectedObject6(3, -1)  
     
    beltChainFeatData.**DrivingLength** = True  
    beltChainFeatData.**BeltLength** = 0.59492  
     
    beltChainFeatData.**UseBeltThickness** = True  
    beltChainFeatData.**BeltThickness** = 0.003  
     
    beltChainFeatData.**CreateBeltPart** = True  
    beltChainFeatData.**EngageBelt** = False  
     
    Set swFeat = swModel.FeatureManager.**CreateFeature**(beltChainFeatData)  
     
    Stop  
     
    Set swFeatData = swFeat.**GetDefinition**()  
     
    ' Modify Belt/Chain feature  
     
    boolstatus = swFeatData.**AccessSelections**(swModel, Nothing)  
     
    pulleyDiamsOri = swFeatData.**PulleyDiameters**  
    pulleyDiamsOri(0) = 0.02  
    pulleyDiamsOri(1) = 0.02  
     
    swFeatData.**PulleyDiameters** = pulleyDiamsOri  
    Debug.Print "Pulley diameters changed to 20 mm"  
     
    swFeatData.**DrivingLength** = True  
    swFeatData.BeltLength = 0.3  
    Debug.Print "Belt length (m) changed to " & swFeatData.**BeltLength**  
     
    swFeatData.**BeltThickness** = 0.002  
    Debug.Print "Belt thickness (m) changed to " & swFeatData.**BeltThickness**  
     
    boolstatus = swFeat.**ModifyDefinition**(swFeatData, swModel, Nothing)

End Sub

Example

[Create Belt/Chain Feature (VB.NET)](Create_Belt_Chain_Feature_Example_VBNET.htm)  
[Create Belt/Chain Feature (C#)](Create_Belt_Chain_Feature_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBeltChainFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
