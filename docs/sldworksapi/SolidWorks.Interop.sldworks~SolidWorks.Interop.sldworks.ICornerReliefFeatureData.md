# ICornerReliefFeatureData Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData`

Allows access to sheet metal corner relief feature data.
Allows access to sheet metal corner relief feature data.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface ICornerReliefFeatureData 
```

```

Dim instance As ICornerReliefFeatureData
```

```

public interface ICornerReliefFeatureData 
```

```

public interface class ICornerReliefFeatureData 
```

Remarks

For more information see the **SOLIDWORKS user-interface help > Sheet Metal > Using Sheet Metal Tools > Corner Reliefs and Bend Transitions** topics.

Example

'VBA

'=========================================================

'Preconditions:

'1. Ensure that the specified part template exists.

'2. Open an Immediate window.

'

'Postconditions:

' 1. Press F5.

' 2. Creates:

'     - **Base-Flange1**

'     - **Sketched Bend1**

'     - **Sketched Bend2**

'     - **Sketched Bend3**

'     - **Sketched Bend4**

' 3. Selects the sheet metal solid body.

' 4. Sets rectangular reliefs for the four corners.

' 5. Creates **Corner Relief1**.

' 6. Press F5.

' 7. Changes four corners to have circular reliefs.

' 8. Press F5.

' 9. Changes four corners to have constant width reliefs.

'10. Inspect the Immediate window and the graphics area after each change.

'===============================================================================

Dim swApp As SldWorks.SldWorks

Dim swModel As SldWorks.ModelDoc2

Dim featMgr As SldWorks.FeatureManager

Dim cornerReliefFeatData As SldWorks.CornerReliefFeatureData

Dim swBody As SldWorks.Body2

Dim selMgr As SldWorks.SelectionMgr

Dim SMCorner As SldWorks.SMCornerReliefData

Dim getCornerVar As Variant

Dim cntr1 As Long

Dim cornerItr As SldWorks.SMCornerReliefData

Dim Feat As SldWorks.Feature

Dim featModData As SldWorks.CornerReliefFeatureData

Dim cornerReliefMod3Data As SldWorks.CornerReliefFeatureData

Dim UseRatio As Boolean

Dim CFace1 As SldWorks.face2

Dim CFace2 As SldWorks.face2

Dim CFace3 As SldWorks.face2

Dim boolstatus As Boolean

Dim longstatus As Long, longwarnings As Long

Sub PrintReliefData(ByVal cornerIndex As Long, ByVal cornerReliefFeatData As SldWorks.CornerReliefFeatureData)

    Dim smCornerReliefData1 As SldWorks.SMCornerReliefData

    boolstatus = cornerReliefFeatData.**GetCornerAtIndex**(cornerIndex, smCornerReliefData1)

   

    Debug.Print "Add filleted corners? " & smCornerReliefData1.**AddFilletedCorners**

    Debug.Print "Corner fillet diameter = " & smCornerReliefData1.**CornerFilletDiameter**

    Debug.Print "Use ratio to thickness? " & smCornerReliefData1.**RatioToThickness**

    Debug.Print "Relief type as defined by swCornerBendReliefType\_e = " & smCornerReliefData1.**ReliefType**

    Debug.Print "Slot length = " & smCornerReliefData1.**SlotLength**

    Debug.Print "Slot width = " & smCornerReliefData1.**SlotWidth**

    Debug.Print "Center on bend lines? " & smCornerReliefData1.**CenterOnBendLines**

    Debug.Print "Tangent to bend? " & smCornerReliefData1.**TangentToBend**

   

    Call smCornerReliefData1.**GetFaces**(CFace1, CFace2, CFace3)

End Sub

Sub main()

    Set swApp = Application.SldWorks

    Set swModel = swApp.ActiveDoc

   

    Dim swSheetWidth As Double

    swSheetWidth = 0

    Dim swSheetHeight As Double

    swSheetHeight = 0

    Set swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2022\templates\\Part.PRTDOT", 0, swSheetWidth, swSheetHeight)

    Set featMgr = swModel.FeatureManager

    boolstatus = swModel.Extension.SelectByID2("Front Plane", "PLANE", -7.54055245830957E-02, 5.42345258765876E-02, 2.94433115750138E-03, False, 0, Nothing, 0)

    swModel.SketchManager.InsertSketch True

    swModel.ClearSelection2 True

    Dim skSegment As Object

    Set skSegment = swModel.SketchManager.CreateLine(-0.049594, 0.029143, 0#, 0.026075, 0.029143, 0#)

    Set skSegment = swModel.SketchManager.CreateLine(0.026075, 0.029143, 0#, 0.026075, 0.015645, 0#)

    Set skSegment = swModel.SketchManager.CreateLine(0.026075, 0.015645, 0#, 0.04305, 0.015645, 0#)

    Set skSegment = swModel.SketchManager.CreateLine(0.04305, 0.015645, 0#, 0.04305, -0.034869, 0#)

    Set skSegment = swModel.SketchManager.CreateLine(0.04305, -0.034869, 0#, 0.026075, -0.034869, 0#)

    Set skSegment = swModel.SketchManager.CreateLine(0.026075, -0.034869, 0#, 0.026075, -0.048571, 0#)

    Set skSegment = swModel.SketchManager.CreateLine(0.026075, -0.048571, 0#, -0.049594, -0.048571, 0#)

    Set skSegment = swModel.SketchManager.CreateLine(-0.049594, -0.048571, 0#, -0.049594, -0.034869, 0#)

    Set skSegment = swModel.SketchManager.CreateLine(-0.049594, -0.034869, 0#, -0.066568, -0.034869, 0#)

    Set skSegment = swModel.SketchManager.CreateLine(-0.066568, -0.034869, 0#, -0.066568, 0.015645, 0#)

    Set skSegment = swModel.SketchManager.CreateLine(-0.066568, 0.015645, 0#, -0.049594, 0.015645, 0#)

    Set skSegment = swModel.SketchManager.CreateLine(-0.049594, 0.015645, 0#, -0.049594, 0.029143, 0#)

    swModel.ClearSelection2 True

    swModel.SketchManager.InsertSketch True

   

    swModel.ShowNamedView2 "\*Trimetric", 8

    swModel.ViewZoomtofit2

    swModel.SketchManager.InsertSketch True

    Dim customBendAllowanceData As SldWorks.CustomBendAllowance

    Set customBendAllowanceData = swModel.FeatureManager.CreateCustomBendAllowance()

    customBendAllowanceData.KFactor = 0.5

    Dim myFeature As SldWorks.Feature

    Set myFeature = swModel.FeatureManager.InsertSheetMetalBaseFlange2(0.0007366, False, 0.0007366, 0.02, 0.01, False, 0, 0, 1, customBendAllowanceData, False, 0, 0.0001, 0.0001, 0.5, True, False, True, True)

   

    boolstatus = swModel.Extension.SelectByRay(-1.45172925108454E-02, -3.87700058865903E-03, 0, -0.5, -0.707106781186547, -0.5, 5.56802642645787E-04, 2, False, 0, 0)

    swModel.SketchManager.InsertSketch True

    swModel.ClearSelection2 True

    Set skSegment = swModel.SketchManager.CreateLine(-0.049594, 0.015645, 0#, -0.049594, -0.034869, 0#)

    swModel.ClearSelection2 True

    swModel.SketchManager.InsertSketch True

    swModel.SketchManager.InsertSketch True

    boolstatus = swModel.Extension.SelectByRay(-2.54254889823514E-02, -6.75397704068888E-03, 0, 0, 0, -1, 4.28258640921609E-04, 2, True, 0, 0)

    Dim CBAObject As SldWorks.CustomBendAllowance

    Set myFeature = swModel.FeatureManager.InsertSheetMetal3dBend(1.5707963267949, True, 0.0007366, False, 3, CBAObject)

    boolstatus = swModel.Extension.SelectByRay(-2.46697384395485E-02, -2.97522432667467E-03, 0, 0, 0, -1, 4.28258640921609E-04, 2, False, 0, 0)

    swModel.SketchManager.InsertSketch True

    swModel.ClearSelection2 True

    boolstatus = swModel.Extension.SelectByRay(-0.049594, 0.015645, 0, 0, 0, -1, 3.92913800359539E-04, 3, False, 0, 0)

    swModel.ClearSelection2 True

    Set skSegment = swModel.SketchManager.CreateLine(-0.049594, 0.015645, 0#, 0.026075, 0.015645, 0#)

    swModel.ClearSelection2 True

    swModel.SketchManager.InsertSketch True

    swModel.SketchManager.InsertSketch True

    boolstatus = swModel.Extension.SelectByRay(-2.35965085767476E-02, -4.34032596567101E-03, 0, 0, 0, -1, 3.92913800359539E-04, 2, True, 0, 0)

    Set myFeature = swModel.FeatureManager.InsertSheetMetal3dBend(1.5707963267949, True, 0.0007366, False, 3, CBAObject)

    boolstatus = swModel.Extension.SelectByRay(-2.34809456942889E-02, -1.97101893326765E-02, 0, 0, 0, -1, 3.92913800359539E-04, 2, False, 0, 0)

    swModel.SketchManager.InsertSketch True

    swModel.ClearSelection2 True

    Set skSegment = swModel.SketchManager.CreateLine(-0.049594, -0.034869, 0#, 0.026075, -0.034869, 0#)

    swModel.ClearSelection2 True

    swModel.SketchManager.InsertSketch True

    swModel.SketchManager.InsertSketch True

    boolstatus = swModel.Extension.SelectByRay(-1.71484564194607E-02, -3.99245414393841E-03, 0, 0, 0, -1, 3.67699685812068E-04, 2, True, 0, 0)

    Set myFeature = swModel.FeatureManager.InsertSheetMetal3dBend(1.5707963267949, True, 0.0007366, False, 3, CBAObject)

    boolstatus = swModel.Extension.SelectByRay(-1.07677854009571E-02, -9.72424336395007E-03, 0, 0, 0, -1, 3.67699685812068E-04, 2, False, 0, 0)

    swModel.SketchManager.InsertSketch True

    swModel.ClearSelection2 True

    Set skSegment = swModel.SketchManager.CreateLine(0.026075, -0.034869, 0#, 0.026075, 0.015645, 0#)

    swModel.ClearSelection2 True

    swModel.SketchManager.InsertSketch True

    swModel.SketchManager.InsertSketch True

    boolstatus = swModel.Extension.SelectByRay(-2.59083606991011E-02, -6.2053705579176E-03, 0, 0, 0, -1, 3.67699685812068E-04, 2, True, 0, 0)

    Set myFeature = swModel.FeatureManager.InsertSheetMetal3dBend(1.5707963267949, True, 0.0007366, False, 3, CBAObject)

    ' Zoom to Area

    swModel.ViewZoomTo2 1.52447662706814E-02, 2.18199896815251E-03, -8.86660359613402E-03, 0.022429935049572, -6.38493303744786E-03, -8.86660359613402E-03

   

    Set cornerReliefFeatData = featMgr.**CreateDefinition**(swFmCornerRelief)

   

    boolstatus = swModel.Extension.SelectByID2("Sketched Bend4", "SOLIDBODY", 0, 0, 0, False, 0, Nothing, 0)

   

    Set selMgr = swModel.SelectionManager

   

    Set swBody = selMgr.GetSelectedObject6(1, -1)

   

    cornerReliefFeatData.**Initialize** swCornerReliefBendType\_TwoBend

    cornerReliefFeatData.**SetBodyScope** swBody

   

    'Create corners (tear reliefs are the default reliefs for Sketched Bends)

    longstatus = cornerReliefFeatData.**CollectAllCorners**(swCornerTearRelief, getCornerVar)

   

    Debug.Print ""

    Debug.Print "-------------Changing corners to rectangular reliefs------------------- "

    For cntr1 = 0 To UBound(getCornerVar)

       

        Set cornerItr = getCornerVar(cntr1)

       

        cornerItr.**AddFilletedCorners** = True

        cornerItr.**CornerFilletDiameter** = 0.00025

        cornerItr.**CenterOnBendLines** = True

        cornerItr.**TangentToBend** = True

        cornerItr.**ReliefType** = swCornerRectangularRelief

       

        UseRatio = True

       

        If Not UseRatio Then

            cornerItr.**SlotLength** = 0.009

        Else

            cornerItr.**RatioToThickness** = True

        End If

       

        PrintReliefData cntr1 + 1, cornerReliefFeatData

        Debug.Print ""

    Next

   

    Set Feat = featMgr.**CreateFeature**(cornerReliefFeatData)

   

    Stop

   

    Set featModData = Feat.**GetDefinition**()

   

    featModData.**AccessSelections** swModel, Nothing

   

    getCornerVar = featModData.**GetCorners**(-1)

   

    Debug.Print ""

    Debug.Print "-------------Changing corners to circular reliefs------------------- "

   

    For cntr1 = 0 To UBound(getCornerVar)

   

        Set cornerItr = getCornerVar(cntr1)

       

        cornerItr.**ReliefType** = swCornerCircularRelief

       

        UseRatio = False

       

        If Not UseRatio Then

            cornerItr.**SlotWidth** = 0.0008

        Else

            cornerItr.**RatioToThickness** = True

        End If

       

        PrintReliefData cntr1 + 1, featModData

        Debug.Print ""

   

    Next

   

    Feat.**ModifyDefinition** featModData, swModel, Nothing

   

    Stop

   

    Set cornerReliefMod3Data = Feat.**GetDefinition**()

   

    cornerReliefMod3Data.**AccessSelections** swModel, Nothing

   

    getCornerVar = cornerReliefMod3Data.**GetCorners**(-1)

   

    Debug.Print ""

    Debug.Print "-------------Changing corners to constant width reliefs------------------- "

   

    For cntr1 = 0 To UBound(getCornerVar)

   

        Set cornerItr = getCornerVar(cntr1)

       

        cornerItr.**ReliefType** = swCornerConstantWidthRelief

       

        PrintReliefData cntr1 + 1, cornerReliefMod3Data

        Debug.Print ""

   

    Next

   

    Feat.ModifyDefinition cornerReliefMod3Data, swModel, Nothing

End Sub

Example

[Create Sheet Metal Corner Relief Feature (VB.NET)](Create_SM_Corner_Relief_Feature_Example_VBNET.htm)  
[Create Sheet Metal Corner Relief Feature (C#)](Create_SM_Corner_Relief_Feature_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICornerReliefFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
