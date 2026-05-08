# AutoMateRepair Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AutoMateRepair`

Automatically repairs broken mates in this assembly.
Automatically repairs broken mates in this assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AutoMateRepair( _
   ByRef ProcessedMates As System.Object, _
   ByRef FailedMates As System.Object _
) As System.Integer
```

```

Dim instance As IAssemblyDoc
Dim ProcessedMates As System.Object
Dim FailedMates As System.Object
Dim value As System.Integer
 
value = instance.AutoMateRepair(ProcessedMates, FailedMates)
```

```

System.int AutoMateRepair( 
   out System.object ProcessedMates,
   out System.object FailedMates
)
```

```

System.int AutoMateRepair( 
   [Out] System.Object^ ProcessedMates,
   [Out] System.Object^ FailedMates
) 
```

#### Parameters

*ProcessedMates*
:   Array of successfully repaired [IMate2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.md)s

*FailedMates*
:   Array of failed IMate2s

#### Return Value

Mate repair errors as defined by [swAutoMateRepairErrors\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAutoMateRepairErrors_e.html)

Remarks

Before calling this method you must:

- ensure that the entities needed to repair the broken mates are present in the assembly

    - and -

- select the Mates folder in the FeatureManager design tree.

Example

'VBA

'---------------------------------------------------------------

' Preconditions:

' 1. Open the Immediate window.

' 2. Ensure that **c:\temp** and the specified templates exist.

'

' Postconditions:

' 1. When the macro stops, inspect the FeatureManager design tree.

'    Observe that two Cylinder\_225 components, two planes, and two mates are added to the assembly.

' 2. In the FeatureManager design tree delete PLANE2.

'    Observe that Cylinder\_225<1> and Coincident2 are red, indicating a mate error has occurred.

' 3. In the user interface add a reference plane that is 1 mm from the Front Plane.

' 4. In the FeatureManager design tree select the Mates folder.

' 5. Press F5 to autorepair the broken mate.

'    The Immediate window shows one repaired mate.

'----------------------------------------------------------------

Dim swApp As SldWorks.SldWorks

Dim Part As SldWorks.ModelDoc2

Dim boolstatus As Boolean

Dim longstatus As Long, longwarnings As Long

Option Explicit

Sub main()

    Set swApp = Application.SldWorks

    Dim swSheetWidth As Double

    swSheetWidth = 0

    Dim swSheetHeight As Double

    swSheetHeight = 0

    Set Part = swApp.NewDocument("c:\temp\Part.prtdot", 0, swSheetWidth, swSheetHeight)

    Dim swPart As SldWorks.PartDoc

    Set swPart = Part

    swApp.ActivateDoc2 "Part1", False, longstatus

    Set Part = swApp.ActiveDoc

    Dim myModelView As SldWorks.ModelView

    Set myModelView = Part.ActiveView

    myModelView.FrameState = swWindowState\_e.swWindowMaximized

    Part.SketchManager.InsertSketch True

    boolstatus = Part.Extension.SelectByID2("Front Plane", "PLANE", -0.068513658157061, 4.03895355082156E-02, 8.71366929740688E-03, False, 0, Nothing, 0)

    Part.ClearSelection2 True

    Dim skSegment As Object

    Set skSegment = Part.SketchManager.CreateCircle(0#, 0#, 0#, 0.045995, 0.021666, 0#)

    Part.ShowNamedView2 "\*Trimetric", 8

    Part.ViewZoomtofit2

    Dim myFeature As SldWorks.Feature

    Set myFeature = Part.FeatureManager.FeatureExtrusion2(True, False, False, 0, 0, 0.225, 0.01, False, False, False, False, 1.74532925199433E-02, 1.74532925199433E-02, False, False, False, False, True, True, True, 0, 0, False)

    Part.SelectionManager.EnableContourSelection = False

   

    ' Save As

    longstatus = Part.SaveAs3("c:\temp\Cylinder\_225.SLDPRT", 0, 0)

    swSheetWidth = 0

    swSheetHeight = 0

    Set Part = swApp.NewDocument("c:\temp\Assembly.asmdot", 0, swSheetWidth, swSheetHeight)

    Dim swAssembly As SldWorks.AssemblyDoc

    Set swAssembly = Part

    swApp.ActivateDoc2 "Assem3", False, longstatus

    Set Part = swApp.ActiveDoc

    Set myModelView = Part.ActiveView

    myModelView.FrameState = swWindowState\_e.swWindowMaximized

   

    ' Insert Component

    Dim AssemblyTitle As String

    AssemblyTitle = Part.GetTitle

    Dim tmpObj As SldWorks.ModelDoc2

    Dim errors As Long

    Set tmpObj = swApp.OpenDoc6("c:\temp\Cylinder\_225.SLDPRT", 1, 32, "", errors, longwarnings)

    Set Part = swApp.ActivateDoc3(AssemblyTitle, True, 0, errors)

    Dim swInsertedComponent As SldWorks.Component2

    Set swInsertedComponent = Part.AddComponent5("c:\temp\Cylinder\_225.SLDPRT", 0, "", False, "", 0.721748083354866, 0.92923566513213, 1.36775956940221)

    swApp.CloseDoc "c:\temp\Cylinder\_225.SLDPRT"

   

    boolstatus = Part.Extension.SelectByID2("Cylinder\_225-1", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)

    Part.UnfixComponent

    ' Create PLANE1 and PLANE2

   

    boolstatus = Part.SetUserPreferenceToggle(swUserPreferenceToggle\_e.swDisplayPlanes, True)

    boolstatus = Part.Extension.SelectByID2("Front Plane", "PLANE", 0, 0, 0, True, 0, Nothing, 0)

    Dim myRefPlane As SldWorks.RefPlane

    Set myRefPlane = Part.FeatureManager.InsertRefPlane(8, 0.1, 0, 0, 0, 0)

    boolstatus = Part.Extension.SelectByID2("Front Plane", "PLANE", 0, 0, 0, True, 0, Nothing, 0)

    Set myRefPlane = Part.FeatureManager.InsertRefPlane(8, 0.001, 0, 0, 0, 0)

    Part.ClearSelection2 True

   

    ' Insert Component

    AssemblyTitle = Part.GetTitle

    Set tmpObj = swApp.OpenDoc6("c:\temp\Cylinder\_225.SLDPRT", 1, 32, "", errors, longwarnings)

    Set Part = swApp.ActivateDoc3(AssemblyTitle, True, 0, errors)

    Set swInsertedComponent = Part.AddComponent5("c:\temp\Cylinder\_225.SLDPRT", 0, "", False, "", -9.24876597127877E-02, 5.65812429995276E-02, 0.22909678472206)

    swApp.CloseDoc "c:\temp\Cylinder\_225.SLDPRT"

   

    Part.ClearSelection2 True

    boolstatus = Part.Extension.SelectByID2("PLANE1", "PLANE", 0.012624285665936, 0.154967158689601, 0.112309569516221, True, 1, Nothing, 0)

    boolstatus = Part.Extension.SelectByRay(-0.076247080467482, 0.103507691590153, 0.115945777078347, -0.283810108456217, -0.958610200111282, 2.27663475480263E-02, 2.30409955137483E-03, 1, True, 1, 0)

   

    ' Create CoincidentMateFeatureData

    Dim MateData As SldWorks.CoincidentMateFeatureData

    Set MateData = Part.CreateMateData(0)

   

    ' Set the Entities To Mate

    Dim EntitiesToMate(1) As Object

    Set EntitiesToMate(0) = Part.SelectionManager.GetSelectedObject6(1, -1)

    Set EntitiesToMate(1) = Part.SelectionManager.GetSelectedObject6(2, -1)

    Dim EntitiesToMateVar As Variant

    EntitiesToMateVar = EntitiesToMate

    MateData.EntitiesToMate = (EntitiesToMateVar)

   

    ' Set the Mate Alignment

    MateData.MateAlignment = 1

   

    ' Create the mate

    Dim MateFeature As SldWorks.Feature

    Set MateFeature = Part.CreateMate(MateData)

    Part.ClearSelection2 True

    Part.EditRebuild3

   

    Part.ClearSelection2 True

    boolstatus = Part.Extension.SelectByID2("PLANE2", "PLANE", -0.051265823820458, 0.210240836185798, -8.14719342065839E-02, True, 1, Nothing, 0)

    boolstatus = Part.Extension.SelectByRay(0.767058330396253, 0.909200270895155, 1.48052500817425, -0.400036026779312, -0.515038074910024, -0.758094294050284, 1.12587739183236E-02, 1, True, 0, 0)

   

    ' Create CoincidentMateFeatureData

    Set MateData = Part.CreateMateData(0)

   

    ' Set the Entities To Mate

    Set EntitiesToMate(0) = Part.SelectionManager.GetSelectedObject6(1, -1)

    Set EntitiesToMate(1) = Part.SelectionManager.GetSelectedObject6(2, -1)

    EntitiesToMateVar = EntitiesToMate

    MateData.EntitiesToMate = (EntitiesToMateVar)

   

    ' Set the Mate Alignment

    MateData.MateAlignment = 1

   

    ' Create the mate

    Set MateFeature = Part.CreateMate(MateData)

    Part.ClearSelection2 True

    Part.EditRebuild3

    Part.ViewZoomtofit2

   

    Stop  ' Delete Plane2; create a new plane that is 1mm from the Front Plane; select the Mates folder in the FeatureManager design tree; then press F5 to repair the broken mate

   

    Dim swModel As SldWorks.ModelDoc2

    Dim cnt As Long

   

    Set swModel = swApp.ActiveDoc

   

    Dim swAsm As SldWorks.AssemblyDoc

    Set swAsm = swModel

   

    Dim failedMates As Variant

    Dim ProcessedMates As Variant

    Dim lStatus As Long

    lStatus = swAsm.**AutoMateRepair**(ProcessedMates, failedMates)

   

    Debug.Print "Number of Processed Mates is " & UBound(ProcessedMates) + 1 & ":"

    For cnt = 0 To UBound(ProcessedMates)

    Debug.Print ProcessedMates(cnt).Name

    Next

   

    Debug.Print vbNewLine

   

    Debug.Print "Number of failed Mates is " & UBound(failedMates) + 1 & ":"

    For cnt = 0 To UBound(failedMates)

    Debug.Print failedMates(cnt).Name

    Next

End Sub

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::CreateMate Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateMate.md)
