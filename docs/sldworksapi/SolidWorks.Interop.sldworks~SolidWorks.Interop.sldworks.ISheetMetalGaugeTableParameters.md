# ISheetMetalGaugeTableParameters Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters`

Allows access to sheet metal gauge table parameters.
Allows access to sheet metal gauge table parameters.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface ISheetMetalGaugeTableParameters 
```

```

Dim instance As ISheetMetalGaugeTableParameters
```

```

public interface ISheetMetalGaugeTableParameters 
```

```

public interface class ISheetMetalGaugeTableParameters 
```

Remarks

For more information about sheet metal gauge tables, read the **SOLIDWORKS Help > Sheet Metal > Sheet Metal Parts > Sheet Metal Gauge Tables** topic.

Example

'VBA

'This example demonstrates how to create a swept flange using a bend table in a non-sheet-metal part.

'============================================

'Preconditions:

'1. Ensure that the paths to templates and gauge tables are valid.

'2. Open an Immediate window.

'3. Press F5 repeatedly and inspect the Immediate window and FeatureManager design tree as instructed.

'

'Postconditions:

'1. Creates **Sketch1** for the sweep path.

'2. Creates **Sketch2** for the sweep profile.

'3. Creates **Swept Flange1** using a gauge table installed with SOLIDWORKS.

'4. Displays gauge table parameters.

'5. Modifies **Swept Flange1** to override the gauge number, bend radius, and gauge thickness.

'6. Displays new gauge parameters.

'============================================

Option Explicit

Dim swApp As SldWorks.SldWorks  
Dim swPart As PartDoc  
Dim swModel As SldWorks.ModelDoc2  
Dim swFeat As SldWorks.Feature  
Dim swFeatMgr As SldWorks.FeatureManager  
Dim swSweptFlangeFeatureData As SldWorks.SweptFlangeFeatureData  
Dim featData As SldWorks.SweptFlangeFeatureData  
Dim smGaugeTableParam As SheetMetalGaugeTableParameters  
Dim skSegment As SldWorks.SketchSegment  
Dim myRefPlane As SldWorks.RefPlane  
Dim swFeatNameID As Long  
Dim swSketch As SldWorks.Feature  
Dim oPath(0) As Object  
Dim boolstatus As Boolean  
Dim errCode As Long  
Dim swSheetWidth As Double  
Dim swSheetHeight As Double  
Dim vPath As Variant  
Dim gaugePath As String  
Dim gaugeCount As Long  
Dim gaugeNumbers As Variant  
Dim i As Long  
Dim radiiCount As Long  
Dim radii As Variant  
Dim newgaugePath As String

Sub main()

    Set swApp = Application.SldWorks  
     
    swSheetWidth = 0  
    swSheetHeight = 0  
    Set swModel = swApp.NewDocument("C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\Tutorial\part.prtdot", 0, swSheetWidth, swSheetHeight)  
     
    Set swPart = swModel  
    Set swModel = swApp.ActiveDoc  
     
    Set skSegment = swModel.SketchManager.Create3PointArc(-0.058601, -0.015313, 0#, -0.003828, -0.021603, 0#, 0.002265, -0.05642, 0#)  
    swModel.ClearSelection2 True  
    swModel.SketchManager.InsertSketch True 'Sketch1  
    swModel.ClearSelection2 True  
     
    boolstatus = swModel.Extension.SelectByID2(Point2@Sketch1, "EXTSKETCHPOINT", -0.003828, -0.021603, 0, True, 0, Nothing, 0)  
    boolstatus = swModel.Extension.SelectByID2(Arc1@Sketch1, "EXTSKETCHSEGMENT", 2.85760095397308E-03, -3.42380271903227E-02, 0, True, 1, Nothing, 0)  
     
    Set myRefPlane = swModel.FeatureManager.InsertRefPlane(4, 0, 2, 0, 0, 0)  
     
    boolstatus = swModel.Extension.SelectByID2("Plane1", "PLANE", 1.03901931573406E-02, -9.17038599747196E-03, -6.22490227027586E-03, True, 0, Nothing, 0)  
     
    swModel.SketchManager.InsertSketch True  
    Set skSegment = swModel.SketchManager.CreateLine(0#, 0#, 0#, 0#, 0.018316, 0#)  
    Set skSegment = swModel.SketchManager.CreateLine(0#, 0.018316, 0#, 0.008362, 0.035435, 0#)  
    swModel.ClearSelection2 True  
    swModel.SketchManager.InsertSketch True 'Sketch2

    swFeatNameID = swFeatureNameID\_e.swFmSweptFlange  
    Set swFeatMgr = swModel.FeatureManager  
    Set swSweptFlangeFeatureData = swFeatMgr.**CreateDefinition**(swFeatNameID)

    swModel.ClearSelection2 True  
     
    'Select the sweep path  
    boolstatus = swModel.Extension.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)  
    Set swSketch = swModel.SelectionManager.GetSelectedObject6(1, -1)  
     
    Set oPath(0) = swSketch  
    vPath = oPath  
    swSweptFlangeFeatureData.**Path** = vPath  
     
    'Select the sweep profile  
    boolstatus = swModel.Extension.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)  
    Set swSketch = swModel.SelectionManager.GetSelectedObject6(1, -1)  
    swSweptFlangeFeatureData.**Profile** = swSketch

    errCode = swSweptFlangeFeatureData.**GetErrorCodes**  
    Debug.Print "Swept flange definition error code: " + CStr(errCode)  
     
    Stop 'Inspect the Immediate window for the swept flange definition error

    swSweptFlangeFeatureData.**UseMaterialSheetMetalParameters** = False  
    swSweptFlangeFeatureData.**UseGaugeTable** = True  
     
    Debug.Print "Use Gauge Table? " + CStr(swSweptFlangeFeatureData.**UseGaugeTable**)  
     
    Set smGaugeTableParam = swSweptFlangeFeatureData.**GetGaugeTableParameters**  
    boolstatus = smGaugeTableParam.**GetGaugeTablePath**(gaugePath)  
    
    If boolstatus = False Then  
        smGaugeTableParam.**SetGaugeTablePath** ("C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\LANG\ENGLISH\SHEET METAL GAUGE TABLES\BEND ALLOWANCE MM SAMPLE.XLS")  
    End If  
     
    boolstatus = smGaugeTableParam.**GetGaugeTablePath**(gaugePath)  
    Debug.Print "Got gauge table path? " + CStr(boolstatus)  
    Debug.Print "Gauge Table Path: " + gaugePath  
    Debug.Print "Process: " + smGaugeTableParam.**Process**  
     
    gaugeCount = smGaugeTableParam.**GetGaugeNumberCount**()  
    Debug.Print "Gauge Number Count: " + CStr(gaugeCount)  
     
    Debug.Print "Available gauge numbers: "  
     
    gaugeNumbers = smGaugeTableParam.**GetAvailableGaugeNumbers**()  
     
    For i = 0 To gaugeCount - 1  
        Debug.Print gaugeNumbers(i)  
    Next  
    Debug.Print "Current Gauge Number: " + smGaugeTableParam.**GetCurrentGaugeNumber**()  
     
    Stop 'Inspect the Immediate window for the current gauge number  
     
    radiiCount = smGaugeTableParam.GetRadiiCount()  
    Debug.Print "Bend Radii Count: " + CStr(smGaugeTableParam.GetRadiiCount())  
     
    Debug.Print "Available bend radii: "  
    radii = smGaugeTableParam.**GetAvailableRadii**()  
    For i = 0 To radiiCount - 1  
        Debug.Print radii(i)  
    Next  
    Debug.Print "Current Bend Radius: " + CStr(smGaugeTableParam.**GetCurrentRadius**)  
     
    Debug.Print "Thickness: " + CStr(smGaugeTableParam.**GetThickness**)  
    Debug.Print "Override Thickness? " + CStr(smGaugeTableParam.**OverrideThickness**)  
    Debug.Print "Override Bend Radius? " + CStr(smGaugeTableParam.**OverrideRadius**)  
    Debug.Print "Reverse Direction? " + CStr(smGaugeTableParam.**ReverseDirection**)  
     
    Stop 'Inspect the Immediate window for current bend radius and current gauge thickness  
   
    swSweptFlangeFeatureData.**SetGaugeTableParameters** smGaugeTableParam  
   
    Set swFeat = swFeatMgr.**CreateFeature**(swSweptFlangeFeatureData)  
     
    errCode = swSweptFlangeFeatureData.**GetErrorCodes**  
    Debug.Print "Swept flange creation error code: " + CStr(errCode)  
    swModel.ClearSelection2 True  
     
    Stop 'Inspect the Immediate window for the swept flange creation status  
    'Observe Sheet-Metal, Swept Flange1, and Flat-Pattern in the FeatureManager design tree  
     
    'Set new gauge number and override gauge thickness and bend radius  
    Set featData = swFeat.**GetDefinition**()  
    Set smGaugeTableParam = featData.**GetGaugeTableParameters**  
     
    smGaugeTableParam.**ReverseDirection** = True  
    smGaugeTableParam.**SetCurrentGaugeNumber** "Gauge 3"  
    smGaugeTableParam.**SetThickness** 0.006, True  
    smGaugeTableParam.**SetRadius** 0.006, True  
     
    featData.**SetGaugeTableParameters** smGaugeTableParam  
    boolstatus = swFeat.**ModifyDefinition**(featData, swModel, Nothing)  
    Debug.Print "Swept flange modification status: " + CStr(boolstatus)  
     
    Stop 'Inspect the Immediate window for the swept flange modification status  
     
    'Get new gauge number  
    boolstatus = featData.**AccessSelections**(swModel, Nothing)  
    Set smGaugeTableParam = featData.**GetGaugeTableParameters**  
     
    boolstatus = smGaugeTableParam.**GetGaugeTablePath**(newgaugePath)  
    Debug.Print "Got gauge table path? " + CStr(boolstatus)  
    Debug.Print "Gauge Table Path: " + newgaugePath  
     
    Debug.Print "Process: " + smGaugeTableParam.**Process**  
     
    gaugeCount = smGaugeTableParam.**GetGaugeNumberCount**()  
    Debug.Print "Gauge Number Count: " + CStr(gaugeCount)  
    Debug.Print "Available gauge numbers: "  
    gaugeNumbers = smGaugeTableParam.**GetAvailableGaugeNumbers**()

    For i = 0 To gaugeCount - 1  
        Debug.Print gaugeNumbers(i)  
    Next  
    Debug.Print "Current Gauge Number: " + smGaugeTableParam.**GetCurrentGaugeNumber**()  
     
    Stop 'Inspect the Immediate window for the new gauge number  
     
    'Get new bend radius and gauge thickness  
    radiiCount = smGaugeTableParam.**GetRadiiCount**()  
    Debug.Print "Bend Radii Count: " + CStr(radiiCount)

    Debug.Print "Available bend radii: "  
    radii = smGaugeTableParam.**GetAvailableRadii**()  
    For i = 0 To radiiCount - 1  
        Debug.Print radii(i)  
    Next  
    Debug.Print "Current Bend Radius: " + CStr(smGaugeTableParam.**GetCurrentRadius**)  
     
    Debug.Print "Thickness: " + CStr(smGaugeTableParam.**GetThickness**)  
    Debug.Print "Override Thickness? " + CStr(smGaugeTableParam.**OverrideThickness**)  
    Debug.Print "Override Bend Radius? " + CStr(smGaugeTableParam.**OverrideRadius**)  
    Debug.Print "Reverse Direction? " + CStr(smGaugeTableParam.**ReverseDirection**)  
     
    featData.**ReleaseSelectionAccess**  
     
    Stop 'Inspect the Immediate window for the new bend radius and gauge thickness

End Sub

Example

[Create Swept Flange Using Gauge Table (C#)](Create_Swept_Flange_Using_Gauge_Table_Example_CSharp.htm)  
[Create Swept Flange Using Gauge Table (VB.NET)](Create_Swept_Flange_Using_Gauge_Table_Example_VBNET.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISheetMetalGaugeTableParameters Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
