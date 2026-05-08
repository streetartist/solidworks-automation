# StructureSystemToPatternArray Property (ICircularPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~StructureSystemToPatternArray`

Gets or sets the structure systems to pattern in this circular pattern feature.
Gets or sets the structure systems to pattern in this circular pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property StructureSystemToPatternArray As System.Object
```

```

Dim instance As ICircularPatternFeatureData
Dim value As System.Object
 
instance.StructureSystemToPatternArray = value
 
value = instance.StructureSystemToPatternArray
```

```

System.object StructureSystemToPatternArray {get; set;}
```

```

property System.Object^ StructureSystemToPatternArray {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of [IStructureSystemFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemFolder.md)s

Remarks

This property is valid only if [ICircularPatternFeatureData::BodyPattern](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~BodyPattern.md) is true.

Use the setter of this property to change structure systems to pattern only after the feature has been created.

Before using this property in .NET code, read [IDispatch Object Arrays as Input in .NET](sldworksAPIProgGuide.chm::/Overview/IDispatch_Object_Arrays_as_Input_in_.NET.htm). To remove a structure system from the pattern, set this property to a DispatchWrapper array containing one null element.

For more information, see the **SOLIDWORKS user-interface help > Weldments and Structure System > Pattern and Mirror Support** topic.

Example

'VBA  
'This example demonstrates how to create a circular pattern using a structure system.  
'==========================================================================================  
'Preconditions:  
'1. Ensure the specified part template exists.  
'2. Open an Immediate window.  
'3. Press F5.  
'  
'Postconditions:  
' 1. Creates **Sketch1** containing two sketch segments.  
' 2. Configures the start/end extensions and the member profile.  
' 3. Selects the two sketch segments.  
' 4. Creates primary **Structure System1** with two primary path segment members (**Member1** and **Member2**).  
' 5. Creates an axis about which to create a circular pattern.  
' 6. Creates a **Boss-Extrude1** to pattern.  
' 7. Inspect the graphics area.  
' 8. Press F5 to create **CirPattern1**.  
' 9. Press F5 to finish.  
'10. Inspect the Immediate window.  
'========================================================================  
Dim swApp As SldWorks.SldWorks  
Dim modDoc As SldWorks.ModelDoc2  
Dim swFeatMgr As SldWorks.FeatureManager  
Dim swSelMgr As SldWorks.SelectionMgr  
Dim modDocExt As SldWorks.ModelDocExtension  
Dim structMemDef As SldWorks.StructureSystemMemberFeatureData  
Dim profDef As SldWorks.StructureSystemMemberProfile  
Dim PrimDef As SldWorks.PrimaryStructuralMemberFeatureData  
Dim memPathSegDef As PrimaryMemberPathSegmentFeatureData  
Dim memBetweenPointsSecDef As SldWorks.SecondaryMemberBetweenPointsFeatureData  
Dim secMemDatTochange As SldWorks.SecondaryMemberBetweenPointsFeatureData  
Dim memSupportPlaneSecDef As SldWorks.SecondaryMemberSupportPlaneFeatureData  
Dim segments(2) As Object  
Dim stat As Boolean  
Dim memData(0) As SldWorks.StructureSystemMemberFeatureData  
Dim memDataArray As Variant  
Dim structSys As SldWorks.Feature  
Dim baseSecondarySystem As SldWorks.StructureSystemFolder  
Dim structSysDef As SldWorks.StructureSystemFolder  
Dim structSysSecDef As SldWorks.StructureSystemFolder  
Dim feat As SldWorks.Feature  
Dim structSysModDef As SldWorks.StructureSystemFolder  
Dim outProfiles As Variant  
Dim MemberData As SldWorks.StructureSystemMemberFeatureData  
Dim memberArray As Variant  
Dim profileGrpFeat As SldWorks.Feature  
Dim profileGrp As SldWorks.ProfileGroupFolder  
Dim memTochange As SldWorks.StructureSystemMemberFeatureData  
Dim I As Long  
Dim j As Long  
Dim secDef As SldWorks.SecondaryStructuralMemberFeatureData  
Dim UpToMemDef As SldWorks.SecondaryMemberUpToMembersFeatureData  
Dim point As Object  
Dim Members(0) As Object

Dim swModel As SldWorks.ModelDoc2  
Dim swModelDocExt As SldWorks.ModelDocExtension  
Dim swSketchMgr As SldWorks.SketchManager  
Dim swFeatureMgr As SldWorks.FeatureManager  
Dim swSelectionMgr As SldWorks.SelectionMgr  
Dim swSketchSegment As SldWorks.SketchSegment  
Dim swFeature As SldWorks.Feature  
Dim swCircularPatternFeatureData As SldWorks.CircularPatternFeatureData  
Dim sketchSegments As Variant  
Dim status As Boolean  
Dim obj As Object  
Dim patternFeatures(1) As Object

Option Explicit

Sub main()  
    Set swApp = Application.SldWorks  
    
    Dim swSheetWidth As Double  
    swSheetWidth = 0  
    Dim swSheetHeight As Double  
    swSheetHeight = 0  
    Set modDoc = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2023\templates\Part.PRTDOT", 0, swSheetWidth, swSheetHeight)  
    
    Set modDocExt = modDoc.Extension  
    
    modDoc.SketchManager.InsertSketch True  
    stat = modDocExt.SelectByID2("Front Plane", "PLANE", -0.077188654347454, 0.054268560279924, 3.86214196026222E-03, False, 0, Nothing, 0)  
    modDoc.ClearSelection2 True  
    
    Dim skSegment As Object  
    Set skSegment = modDoc.SketchManager.CreateLine(-0.168061, 0.084736, 0#, -0.168061, -0.077684, 0#)  
    Set skSegment = modDoc.SketchManager.CreateLine(0.075216, 0.107771, 0#, 0.075216, -0.006699, 0#)  
    modDoc.ClearSelection2 True  
    
    stat = modDocExt.SelectByID2("Top Plane", "PLANE", 0, 0, 0, True, 0, Nothing, 0)  
    Dim myRefPlane As SldWorks.RefPlane  
    Set myRefPlane = modDoc.FeatureManager.InsertRefPlane(8, 0.03, 0, 0, 0, 0)  
    modDoc.ClearSelection2 True  
    stat = modDocExt.SelectByID2("Top Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)  
    modDoc.ClearSelection2 True  
    modDoc.SketchManager.InsertSketch True  
    
    stat = modDocExt.SelectByID2("Line1@Sketch1", "EXTSKETCHSEGMENT", -0.168061313304597, 5.44142573846353E-02, 0, False, 0, Nothing, 0)  
    stat = modDocExt.SelectByID2("Line2@Sketch1", "EXTSKETCHSEGMENT", 7.52162521083513E-02, 5.32390034454423E-02, 0, True, 0, Nothing, 0)  
    
    'Create primary structure system path segment members  
    Set structMemDef = modDocExt.**CreateStructureSystemMemberData**(0)  
    Debug.Print "Type of structure system member as defined by swStructureSystemMemberType\_e: " & structMemDef.**StructureSystemMemberType**  
                    
    structMemDef.StartEndExtendD1 = 1#  
    structMemDef.StartEndExtendD2 = 2#  
    
    Set profDef = structMemDef.**MemberProfile**  
    
    profDef.ProfileStandard = "ansi inch"  
    profDef.ProfileType = "c channel"  
    profDef.ProfileSize = "3 x 5"  
    
    Set PrimDef = structMemDef  
    Debug.Print "Structure system primary member creation type as defined by swStructureSystemMemberCreationType\_e: " & PrimDef.**PrimaryMemberType**  
    
    Set memPathSegDef = PrimDef  
    memPathSegDef.**MergeTangentMembers** = True  
    
    Set swSelMgr = modDoc.SelectionManager  
    
    Dim segments(1) As Object  
    Set segments(0) = swSelMgr.GetSelectedObject6(1, 0)  
    Set segments(1) = swSelMgr.GetSelectedObject6(2, 0)  
    stat = memPathSegDef.**SetPathSegments**(segments)  
    Debug.Print "Path segments successfully set: " & stat  
      
    Dim PrimMemData(0) As SldWorks.StructureSystemMemberFeatureData  
    Set PrimMemData(0) = structMemDef  
      
    Dim PrimMemDatArray As Variant  
    PrimMemDatArray = PrimMemData  
    
    Dim structSysFeat As SldWorks.Feature  
    Set structSysFeat = modDocExt.**CreateStructureSystem**(PrimMemDatArray, Nothing)  
     
    'Create the axis for the circular pattern  
    status = modDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)  
    modDoc.SketchManager.InsertSketch True  
    modDoc.ClearSelection2 True  
    Dim skSegmentAxis As Object  
    Set skSegmentAxis = modDoc.SketchManager.**CreateLine**(0.695357, 0.586267, 0#, 0.695357, -0.704287, 0#)  
    modDoc.ClearSelection2 True  
    modDoc.SketchManager.InsertSketch True  
     
    'Create a solid body to also pattern  
    status = modDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)  
    modDoc.SketchManager.InsertSketch True  
    modDoc.ClearSelection2 True  
    status = modDocExt.SketchBoxSelect("0.509957", "-0.990370", "0.000000", "1.024907", "-1.314598", "0.000000")  
    status = modDocExt.SetUserPreferenceToggle(swUserPreferenceToggle\_e.swSketchAddConstToRectEntity, swUserPreferenceOption\_e.swDetailingNoOptionSpecified, False)  
    status = modDocExt.SetUserPreferenceToggle(swUserPreferenceToggle\_e.swSketchAddConstLineDiagonalType, swUserPreferenceOption\_e.swDetailingNoOptionSpecified, True)  
    Dim vSkLines As Variant  
    vSkLines = modDoc.SketchManager.**CreateCornerRectangle**(0.713394086918119, -0.907724114572968, 0, 1.44449597678115, -1.33367043301491, 0)  
    modDoc.ClearSelection2 True  
    modDoc.SketchManager.InsertSketch True  
    modDoc.SketchManager.InsertSketch True  
    Dim myFeature As SldWorks.Feature  
    Set myFeature = modDoc.FeatureManager.**FeatureExtrusion2**(True, False, False, 0, 0, 0.07, 0.01, False, False, False, False, 1.74532925199433E-02, 1.74532925199433E-02, False, False, False, False, False, True, True, 0, 0, False)  
    modDoc.SelectionManager.EnableContourSelection = False

    modDoc.ViewZoomtofit  
     
    Stop  
     
    Set swModel = swApp.ActiveDoc  
    Set swModelDocExt = swModel.Extension  
    Set swSketchMgr = swModel.SketchManager  
    Set swFeatureMgr = swModel.FeatureManager  
    Set swSelectionMgr = swModel.SelectionManager  
         
    'Pre-select axis/direction, bodies, structure system folders  
    status = swModelDocExt.SelectByID2("Line1@Sketch12", "EXTSKETCHSEGMENT", 0.695357, 0.185750016352603, 0, False, 1, Nothing, 0)  
    status = swModelDocExt.SelectByID2("Structure System1", "BODYFEATURE", 0, 0, 0, True, 134217728, Nothing, 0)  
    status = swModelDocExt.SelectByID2("Boss-Extrude1", "SOLIDBODY", 0, 0, 0, True, 256, Nothing, 0)  
     
    'Create circular pattern  
    Set swCircularPatternFeatureData = swFeatureMgr.**CreateDefinition**(swFmCirPattern)  
    swCircularPatternFeatureData.**EqualSpacing** = True  
    swCircularPatternFeatureData.**ReverseDirection** = True  
    swCircularPatternFeatureData.**Spacing** = 1.919862   '110 degrees  
    swCircularPatternFeatureData.**TotalInstances** = 3  
    swCircularPatternFeatureData.**GeometryPattern** = False  
    swCircularPatternFeatureData.**VarySketch** = False  
  
    'Set BodyPattern property to True to pattern structure system folders  
    swCircularPatternFeatureData.**BodyPattern** = True  
     
    Set swFeature = swFeatureMgr.**CreateFeature**(swCircularPatternFeatureData)  
         
    Stop  'Examine the graphics area  
     
    swModel.ClearSelection2 True  
    status = swModelDocExt.SelectByID2("CirPattern1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)  
    Set swFeature = swSelectionMgr.GetSelectedObject6(1, -1)  
    Set swCircularPatternFeatureData = swFeature.**GetDefinition**  
    swCircularPatternFeatureData.**AccessSelections** swModel, Nothing  
    Debug.Print "Is CirPattern1 a features/faces pattern or a bodies pattern (true if a bodies pattern)? " & swCircularPatternFeatureData.**BodyPattern**  
     
    Dim var As Variant  
    var = swCircularPatternFeatureData.**StructureSystemToPatternArray**  
     
    Dim strctSysFolder As StructureSystemFolder  
    Dim index As Integer  
    For index = LBound(var) To UBound(var)  
        Set strctSysFolder = var(index)  
        Set patternFeatures(0) = strctSysFolder  
        Debug.Print "Number of structure system folders: " & strctSysFolder.**GetProfileGroupFoldersCount**  
    Next  
     
    'Uncomment the following lines of code to modify the circular pattern  
    'to use another structure system (e.g., Structure System2)  
    'Stop  
     
    'Dim feat As Feature  
    'swModel.ClearSelection2 True  
    'status = swModelDocExt.SelectByID2("Structure System2", "BODYFEATURE", 0, 0, 0, True, 0, Nothing, 0)  
    'Set feat = swSelectionMgr.GetSelectedObject6(1, 0)  
    'Set patternFeatures(1) = feat.GetSpecificFeature2()  
     
    ''During circular pattern modification, use StructureSystemPatternArray property to change structure system to pattern  
    'swCircularPatternFeatureData.**StructureSystemToPatternArray** = patternFeatures  
     
    Debug.Print swFeature.**ModifyDefinition**(swCircularPatternFeatureData, swModel, Nothing)  
     
    End Sub

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData.md)  
[ICircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData_members.md)
