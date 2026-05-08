# D1FaceNormal Property (ICurveDrivenPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~D1FaceNormal`

Gets or sets the face on which the 3D curve lies in Direction 1 of this curve driven pattern.
Gets or sets the face on which the 3D curve lies in Direction 1 of this curve driven pattern.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property D1FaceNormal As System.Object
```

```

Dim instance As ICurveDrivenPatternFeatureData
Dim value As System.Object
 
instance.D1FaceNormal = value
 
value = instance.D1FaceNormal
```

```

System.object D1FaceNormal {get; set;}
```

```

property System.Object^ D1FaceNormal {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

[IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

Remarks

This property is valid only when:

- editing the curve-driven pattern feature
- ICurveDrivePatternFeatureData::D1AlignmentMethod is set to swCurveDrivenPatternAlignment\_e.swCurvePatternTangentToCurve
- specifying Direction 1 using a 3D curve

To create a curve-driven pattern feature that uses a 3D curve for Direction 1, you must pre-select the face normal with selection Mark = 1024 before creating the curve-driven pattern feature data object.

If you try to edit this property to null or Nothing, [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.md) returns true but the property does not change.

For more information, see the **Curve Driven Patterns and the** **Curve Driven Pattern PropertyManager** topic in the SOLIDWORKS user-interface help.

Example

' VBA  
'  
' This example shows how to pre-select the face normal entity for creating a curve-driven pattern  
' that uses a helical curve for Direction 1.  
'  
' Preconditions: Ensure that the specified part template exists.  
'  
' Postconditions: Inspect the graphics area and the FeatureManager design tree  
'==========================================================

Dim swApp As SldWorks.SldWorks  
Dim swFeat As SldWorks.Feature  
Dim swFeatMgr As SldWorks.FeatureManager  
Dim swFeatData As SldWorks.CurveDrivenPatternFeatureData  
Dim swPart As SldWorks.PartDoc  
Dim Part As SldWorks.ModelDoc2  
Dim skSegment As SldWorks.SketchSegment  
Dim myFeature As SldWorks.Feature  
Dim vSkLines As Variant  
Dim swSheetWidth As Double  
Dim swSheetHeight As Double  
Dim boolstatus As Boolean  
Dim longstatus As Long, longwarnings As Long

Option Explicit

Sub main()

    Set swApp = Application.SldWorks  
     
    'Create new part that includes 3 features: Boss-Extrude1, Boss-Extrude2, and Helix/Spiral1  
    swSheetWidth = 0  
    swSheetHeight = 0  
    Set Part = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2021\templates\Part.PRTDOT", 0, swSheetWidth, swSheetHeight)  
    Set swPart = Part  
    swApp.ActivateDoc2 "Part1", False, longstatus  
    Set Part = swApp.ActiveDoc  
    
    Part.SketchManager.InsertSketch True  
    Set skSegment = Part.SketchManager.CreateCircle(0#, 0#, 0#, 0.31751, 0#, 0#)  
    Part.ClearSelection2 True  
    Part.SketchManager.InsertSketch True  
     
    Set myFeature = Part.FeatureManager.FeatureExtrusion2(True, False, False, 0, 0, 1.029208, 0.00254, False, False, False, False, 1.74532925199433E-02, 1.74532925199433E-02, False, False, False, False, True, True, True, 0, 0, False)  
    Part.SelectionManager.EnableContourSelection = False  
    Part.SketchManager.InsertSketch True  
    boolstatus = Part.Extension.SelectByRay(-8.19439014833279E-03, -2.48002522846491E-03, 8.63600000000702E-02, -0.400036026779312, -0.515038074910024, -0.758094294050284, 8.9519512195122E-04, 2, False, 0, 0)  
    Part.ClearSelection2 True  
     
    vSkLines = Part.SketchManager.CreatePolygon(-0.19, -0.01, 0, -0.19, 0.05, 0, 6, True)  
    Set myFeature = Part.FeatureManager.FeatureExtrusion2(True, False, True, 0, 0, 0.24638, 0.00254, False, False, False, False, 1.74532925199433E-02, 1.74532925199433E-02, False, False, False, False, True, True, True, 0, 0, False)  
    Part.ClearSelection2 True  
     
    boolstatus = Part.Extension.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)  
    Set skSegment = Part.SketchManager.CreateCircle(0#, 0#, 0#, 0.3175, 0, 0)  
    Part.InsertHelix False, True, False, False, swHelixDefinedBy\_e.swHelixDefinedByPitchAndRevolution, 1.016, 1.0167, 1, 0, 3.926  
     
    'Pre-select Helix/Spiral1 for Direction 1 entity  
    boolstatus = Part.Extension.SelectByID2("Helix/Spiral1", "REFERENCECURVES", 0, 0, 0, False, 1, Nothing, 0)  
    'Pre-select Boss-Extrude2 as feature to pattern  
    boolstatus = Part.Extension.SelectByID2("Boss-Extrude2", "BODYFEATURE", 0, 0, 0, True, 4, Nothing, 0)  
    'Pre-select face on Boss-Extrude1 as face normal entity  
    boolstatus = Part.Extension.SelectByRay(0.298048689727977, -0.109451261534383, 0.233585198055067, -0.903801459854838, 2.28031013589574E-02, 0.427344053114907, 7.98164962810585E-03, 2, True, 1024, 0)  
    
    Set swFeatMgr = Part.FeatureManager  
     
    'Create curve driven pattern feature data object  
    Set swFeatData = swFeatMgr.**CreateDefinition**(swFeatureNameID\_e.swFmCurvePattern)  
     
    swFeatData.**D1AlignmentMethod** = 0  
    swFeatData.**D1CurveMethod** = 0  
    swFeatData.**D1InstanceCount** = 8  
    swFeatData.**D1IsEqualSpaced** = True  
    swFeatData.**D1ReverseDirection** = False  
    swFeatData.**D1Spacing** = 0.00254  
    swFeatData.**D2InstanceCount** = 1  
    swFeatData.**D2IsEqualSpaced** = False  
    swFeatData.**D2PatternSeedOnly** = False  
    swFeatData.**D2ReverseDirection** = False  
    swFeatData.**D2Spacing** = 0.00254  
    swFeatData.**Dir2Specified** = False  
     
    'Create CrvPattern1 feature  
    Set swFeat = swFeatMgr.**CreateFeature**(swFeatData)  
     
    Part.ViewZoomtofit2  
     
End Sub

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICurveDrivenPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData.md)  
[ICurveDrivenPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData_members.md)
