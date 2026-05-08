# IInstanceToVaryOptions Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions`

Allows access to options for varying the dimensions and locations of instances in patterns for parts.
Allows access to options for varying the dimensions and locations of instances in patterns for parts.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IInstanceToVaryOptions 
```

```

Dim instance As IInstanceToVaryOptions
```

```

public interface IInstanceToVaryOptions 
```

```

public interface class IInstanceToVaryOptions 
```

Remarks

This interface is valid only if [ILinearPatternFeatureData::InstancesToVary](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~InstancesToVary.md) or [ICircularPatternFeatureData::InstancesToVary](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~InstancesToVary.md) is true.

For more information about the Instance to Vary option, see the **SOLIDWORKS Help > Parts and Features > Features > Patterns and Mirroring > Control and Modify Patterns > Varying Dimension Patterns** topic.

Example

'VBA

'Preconditions:  
' 1. Open *public\_documents***\samples\tutorial\api\box.sldprt**.  
' 2. Open the Immediate window.

'Postconditions:  
' 1. Creates a bi-directional linear pattern of a CBORE feature.  
' 2. Specifies to vary pattern instances.  
' 3. Sets the spacing increment of instances in both directions.  
' 4. Modifies the spacing of instance #3.  
' 5. Increments a near countersink diameter for all pattern instances in Direction 1.  
' 6. Modifies the near countersink diameter for instance #3.  
' 7. Inspect the Immediate window and the graphics area.

' NOTE: Because the part is used elsewhere, do not save changes.

'==========================================

Option Explicit

Dim swApp As SldWorks.SldWorks  
Dim swModel As SldWorks.ModelDoc2  
Dim swSelMgr As SldWorks.SelectionMgr  
Dim feat As SldWorks.Feature  
Dim LPFeatData As SldWorks.LinearPatternFeatureData  
Dim boolstatus As Boolean  
Dim swInstOpts As SldWorks.InstanceToVaryOptions

Sub main()

    Set swApp = Application.SldWorks  
    Set swModel = swApp.ActiveDoc  
    Set swSelMgr = swModel.SelectionManager  
     
    boolstatus = swModel.Extension.SelectByRay(4.39252690830472E-02, 2.99751045230323E-02, 1.26537412306789E-02, -0.400036026779312, -0.515038074910024, -0.758094294050284, 6.33983676613175E-04, 1, True, 1, 0)  
    boolstatus = swModel.Extension.SelectByRay(-1.78361123644777E-02, 2.98747083165836E-02, -3.88627220451099E-02, -0.400036026779312, -0.515038074910024, -0.758094294050284, 6.33983676613175E-04, 1, True, 2, 0)  
    boolstatus = swModel.Extension.SelectByID2("CBORE for #6 Binding Head Machine Screw1", "BODYFEATURE", 0, 0, 0, True, 4, Nothing, 0)  
    swModel.ActivateSelectedFeature  
    swModel.ClearSelection2 True  
    boolstatus = swModel.Extension.SelectByID2("CBORE for #6 Binding Head Machine Screw1", "BODYFEATURE", 0, 0, 0, False, 4, Nothing, 0)  
    boolstatus = swModel.Extension.SelectByRay(4.39252690830472E-02, 2.99751045230323E-02, 1.26537412306789E-02, -0.400036026779312, -0.515038074910024, -0.758094294050284, 6.33983676613175E-04, 1, True, 1, 0)  
    boolstatus = swModel.Extension.SelectByRay(-1.78361123644777E-02, 2.98747083165836E-02, -3.88627220451099E-02, -0.400036026779312, -0.515038074910024, -0.758094294050284, 6.33983676613175E-04, 1, True, 2, 0)  
     
    Dim swFeat As Object  
    Dim swFeatMgr As Object  
     
    Set swFeatMgr = swModel.FeatureManager  
    Dim swFeatData As Object  
    Set swFeatData = swFeatMgr.CreateDefinition(swFeatureNameID\_e.swFmLPattern)  
    swFeatData.D1EndCondition = 0  
    swFeatData.D1ReverseDirection = False  
    swFeatData.D1Spacing = 0.02  
    swFeatData.D1TotalInstances = 2  
    swFeatData.D2EndCondition = 0  
    swFeatData.D2PatternSeedOnly = False  
    swFeatData.D2ReverseDirection = False  
    swFeatData.D2Spacing = 0.01  
    swFeatData.D2TotalInstances = 2  
    swFeatData.GeometryPattern = False  
    swFeatData.VarySketch = False

    Set swFeat = swFeatMgr.CreateFeature(swFeatData)  
     
    boolstatus = swModel.Extension.SelectByID2("LPattern1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)  
    Set feat = swSelMgr.GetSelectedObject6(1, -1)  
    Set LPFeatData = feat.**GetDefinition**  
     
    'Turn on Instances To Vary  
    boolstatus = LPFeatData.**AccessSelections**(swModel, Nothing)

    LPFeatData.**InstancesToVary** = True  
    Debug.Print "Vary instances? " & LPFeatData.InstancesToVary  
     
    boolstatus = feat.**ModifyDefinition**(LPFeatData, swModel, Nothing)  
     
    'Get and set IInstanceToVaryOptions  
    boolstatus = LPFeatData.**AccessSelections**(swModel, Nothing)

    Set swInstOpts = LPFeatData.**GetInstanceToVaryOptions**()  
     
    'Set D1 and D2 spacing increments of all pattern instances  
    swInstOpts.**D1SpacingIncrement** = 0.05  
    swInstOpts.**D2SpacingIncrement** = 0.05  
    Debug.Print "D1 spacing increment is " & swInstOpts.D1SpacingIncrement  
    Debug.Print "D2 spacing increment is " & swInstOpts.D2SpacingIncrement  
     
    'Get current D1 and D2 modified spacing value for patten instance #3 (2,2)  
    Debug.Print "Current D1 modified spacing value for instance #3 is " & swInstOpts.**GetD1ModifiedSpacingValue**(3)  
    Debug.Print "Current D2 modified spacing value for instance #3 is " & swInstOpts.**GetD2ModifiedSpacingValue**(3)  
     
    'Modify the D1 and D2 spacing value for pattern instance #3 (2,2)  
    boolstatus = swInstOpts.**ModifyD1SpacingValue**(3, swInstOpts.GetD1ModifiedSpacingValue(3) + 0.02)  
    boolstatus = swInstOpts.**ModifyD2SpacingValue**(3, swInstOpts.GetD2ModifiedSpacingValue(3) + 0.02)  
      
    'Get the new D1 and D2 modified spacing value for pattern instance #3 (2,2)  
    Debug.Print "New D1 modified spacing value for instance #3 is " & swInstOpts.**GetD1ModifiedSpacingValue**(3)  
    Debug.Print "New D2 modified spacing value for instance #3 is " & swInstOpts.**GetD2ModifiedSpacingValue**(3)  
     
    'Increment a dimension for all pattern instances in Direction 1  
    Dim vIncr1Dims(0) As String  
    Dim vIncr1DimValues(0) As Double  
    vIncr1Dims(0) = "Near C'Sink Dia.@Sketch2"  
    vIncr1DimValues(0) = 0.005  
     
    swInstOpts.**SetD1IncrementDimensions** vIncr1Dims, vIncr1DimValues  
    swInstOpts.**GetD1IncrementDimensions** vIncr1Dims, vIncr1DimValues  
     
    'Modify a specific dimension just for pattern instance #3 (2,2)  
    Dim vDims(0) As String  
    Dim vDimValues(0) As Double  
    vDims(0) = "Near C'Sink Dia.@Sketch2"  
    vDimValues(0) = 0.02  
    boolstatus = swInstOpts.**ModifyDimensions**(3, vDims, vDimValues)  
     
    swInstOpts.**GetModifiedDimensions** 3, vDims, vDimValues  
     
    'Modify the pattern feature with the instance to vary options  
    Call LPFeatData.**SetInstanceToVaryOptions**(swInstOpts)  
    boolstatus = feat.**ModifyDefinition**(LPFeatData, swModel, Nothing)

End Sub

Example

[Vary Linear Pattern Instances (VB.NET)](Vary_Linear_Pattern_Instances_Example_VBNET.htm)  
[Vary Linear Pattern Instances (C#)](Vary_Linear_Pattern_Instances_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IInstanceToVaryOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
