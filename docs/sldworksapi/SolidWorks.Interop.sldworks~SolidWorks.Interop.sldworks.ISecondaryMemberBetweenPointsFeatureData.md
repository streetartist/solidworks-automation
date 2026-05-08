# ISecondaryMemberBetweenPointsFeatureData Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData`

Allows access to a secondary structure system member that is created between the end points on primary structure system member pairs.
Allows access to a secondary structure system member that is created between the end points on primary structure system member pairs.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface ISecondaryMemberBetweenPointsFeatureData 
```

```

Dim instance As ISecondaryMemberBetweenPointsFeatureData
```

```

public interface ISecondaryMemberBetweenPointsFeatureData 
```

```

public interface class ISecondaryMemberBetweenPointsFeatureData 
```

Remarks

See the [IStructureSystemFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemFolder.md) Remarks.

For more information, see the **SOLIDWORKS user-interface help > Weldments and Structure System > Structure System > Secondary Member PropertyManager** topic.

Example

'VBA

'This example demonstrates how to add these secondary structure system members to a primary structure system:

'   - Between points

'   - On plane

'   - Up to members

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
' 5. Inspect the structure system in the graphics area.  
' 6. Press F5 to add a secondary support plane member.  
'     Creates secondary **Structure System2** (**Member3**).  
' 7. Press F5 to edit the support plane member.  
' 8. Press F5 to add a secondary between points member.  
'     Creates secondary **Structure System3** (**Member4**).  
' 9. Press F5 to edit the between points member.  
'10. Press F5 to add a secondary structure system up to member.  
'11. When the macro stops, multi-select a Member1 vertex  
'      in the graphics area and Member2 in the FeatureManager Design tree.  
'12. Press F5 to create secondary Structure System4 (Member5).  
'13. Inspect the Immediate window.  
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
    Set myRefPlane = modDoc.FeatureManager.**InsertRefPlane**(8, 0.03, 0, 0, 0, 0)  
    modDoc.ClearSelection2 True  
    stat = modDocExt.SelectByID2("Top Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)  
    modDoc.ClearSelection2 True  
    modDoc.SketchManager.InsertSketch True  
     
    stat = modDocExt.SelectByID2("Line1@Sketch1", "EXTSKETCHSEGMENT", -0.168061313304597, 5.44142573846353E-02, 0, False, 0, Nothing, 0)  
    stat = modDocExt.SelectByID2("Line2@Sketch1", "EXTSKETCHSEGMENT", 7.52162521083513E-02, 5.32390034454423E-02, 0, True, 0, Nothing, 0)  
     
    'Create primary structure system path segment members  
    Set structMemDef = modDocExt.**CreateStructureSystemMemberData**(0)  
    Debug.Print "Type of structure system member as defined by swStructureSystemMemberType\_e: " & structMemDef.**StructureSystemMemberType**  
                     
    structMemDef.**StartEndExtendD1** = 1#  
    structMemDef.**StartEndExtendD2** = 2#  
     
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
     
    modDoc.ViewZoomtofit  
       
    Stop  
       
    Set structSysDef = structSysFeat.**GetSpecificFeature2**  
    Debug.Print "Number of profile group folders: " & structSysDef.**GetProfileGroupFoldersCount**  
     
    Dim outProfiles As Variant  
    outProfiles = structSysDef.**GetProfileGroupFolders**()  
     
    Dim memberArray As Variant  
      
    If (Not IsEmpty(outProfiles)) Then  
                For I = 0 To UBound(outProfiles)  
                    Set profileGrpFeat = outProfiles(I)  
                    Set profileGrp = profileGrpFeat.**GetSpecificFeature2**  
                    If Not profileGrp Is Nothing Then  
                     Debug.Print "Number of members in profile group: " & profileGrp.**GetStructureSystemMemberCount**  
                      memberArray = profileGrp.**GetStructureSystemMembers**()  
                        If (Not IsEmpty(memberArray)) Then  
                            Exit For  
                        End If  
                    End If  
                Next  
    End If  
     
     
    'Create secondary structure system support plane member

    Dim structSecMemDef As SldWorks.StructureSystemMemberFeatureData  
    Set structSecMemDef = modDocExt.**CreateStructureSystemMemberData**(4) 'Secondary Support Plane  
     
    Debug.Print "Type of structure system member as defined by swStructureSystemMemberType\_e: " & structMemDef.**StructureSystemMemberType**  
     
    structSecMemDef.StartEndExtendD1 = 0.5  
    structSecMemDef.StartEndExtendD2 = 0.5  
     
    Dim secProfDef As SldWorks.StructureSystemMemberProfile  
    Set secProfDef = structSecMemDef.**MemberProfile**  
     
    secProfDef.ProfileStandard = "ansi inch"  
    secProfDef.ProfileType = "c channel"  
    secProfDef.ProfileSize = "3 x 5"  
     
    Dim SecDef As SecondaryStructuralMemberFeatureData  
    Set SecDef = structSecMemDef  
    Debug.Print "Structure system secondary member creation type as defined by swStructureSystemMemberCreationType\_e: " & SecDef.**SecondaryMemberType**; ""  
     
    Set memSupportPlaneSecDef = SecDef  
     
    stat = memSupportPlaneSecDef.**SetMemberPairs**(memberArray)  
    Debug.Print "Member pairs set successfully: " & stat  
     
    stat = modDocExt.SelectByID2("Plane1", "PLANE", 0, 0, 0, True, 0, Nothing, 0)  
    Dim Planes(0) As Object  
    Set Planes(0) = swSelMgr.GetSelectedObject6(1, 0)  
     
    stat = memSupportPlaneSecDef.**SetIntersectingPlanesAndFaces**(Planes)  
    Debug.Print "Intersecting plane set successfully: " & stat  
     
    Dim secMemData(0) As SldWorks.StructureSystemMemberFeatureData  
    Set secMemData(0) = structSecMemDef  
     
    Dim secMemDatArray As Variant  
    secMemDatArray = secMemData  
     
    Dim structSysFeat2 As SldWorks.Feature  
    Set structSysFeat2 = modDocExt.**CreateStructureSystem**(Nothing, secMemDatArray)  
     
    modDoc.ViewZoomtofit  
       
    Stop  
     
    'Edit secondary support plane member by changing start/end extensions

    Set baseSecondarySystem = structSysFeat2.**GetSpecificFeature2**  
    Debug.Print "Number of profile group folders: " & baseSecondarySystem.**GetProfileGroupFoldersCount**  
     
    outProfiles = baseSecondarySystem.**GetProfileGroupFolders**()  
     
    Dim secMemberData As Object  
    Dim SecMemberArray As Variant  
    Dim secProfileGrpFeat As SldWorks.Feature  
    Dim secProfileGrp As SldWorks.ProfileGroupFolder  
    If (Not IsEmpty(outProfiles)) Then  
                For I = 0 To UBound(outProfiles)  
                    Set secProfileGrpFeat = outProfiles(I)  
                    Set secProfileGrp = secProfileGrpFeat.**GetSpecificFeature2**  
                    If Not secProfileGrp Is Nothing Then  
                     Debug.Print "Number of members in profile group: " & secProfileGrp.**GetStructureSystemMemberCount**  
                      SecMemberArray = secProfileGrp.**GetStructureSystemMembers**()  
                        If (Not IsEmpty(SecMemberArray)) Then  
                            For j = 0 To UBound(SecMemberArray)  
                                Set secMemberData = SecMemberArray(j)  
                                Exit For  
                            Next  
                        End If  
                    End If  
                Next  
    End If  
     
    Dim memTochange As SldWorks.StructureSystemMemberFeatureData  
    Set memTochange = secMemberData  
    Dim SecMemFeat As SldWorks.Feature  
    Set SecMemFeat = memTochange.**GetFeature**()  
    memTochange.**StartEndExtendD1** = 0.2  
    memTochange.**StartEndExtendD2** = 0.1

    stat = SecMemFeat.**ModifyDefinition**(secMemberData, modDoc, Nothing)  
     
    Stop  
     
    'Create secondary between points member

    Set structSecMemDef = modDocExt.**CreateStructureSystemMemberData**(5)  
    Debug.Print "Type of structure system member as defined by swStructureSystemMemberType\_e: " & structMemDef.StructureSystemMemberType

    Set secProfDef = structSecMemDef.**MemberProfile**  
     
    secProfDef.ProfileStandard = "ansi inch"  
    secProfDef.ProfileType = "c channel"  
    secProfDef.ProfileSize = "3 x 5"  
     
    Set SecDef = structSecMemDef  
    Debug.Print "Structure system secondary member creation type as defined by swStructureSystemMemberCreationType\_e: " & SecDef.**SecondaryMemberType**  
      
    Set memBetweenPointsSecDef = SecDef

    stat = memBetweenPointsSecDef.**SetMemberPairs**(memberArray)  
    Debug.Print "Member pairs successfully set: " & stat  
     
    memBetweenPointsSecDef.**SecondaryMemberOffsetType** = 0  
    memBetweenPointsSecDef.**DistanceMember1** = 0.5  
    memBetweenPointsSecDef.**DistanceMember2** = 0.4  
    memBetweenPointsSecDef.**RevDirectionDistanceMember1** = False  
    memBetweenPointsSecDef.**RevDirectionDistanceMember2** = False  
         
    Set secMemData(0) = structSecMemDef  
     
    secMemDatArray = secMemData  
     
    Set structSysFeat2 = modDocExt.**CreateStructureSystem**(Nothing, secMemDatArray)  
       
    Stop  
       
    'Edit between points member by changing start/end extensions and offset type

    Set structSysSecDef = structSysFeat2.**GetSpecificFeature2**  
    Debug.Print "Number of profile group folders: " & structSysSecDef.**GetProfileGroupFoldersCount**

    Dim outSecProfiles As Variant  
    outSecProfiles = structSysSecDef.**GetProfileGroupFolders**()

    If (Not IsEmpty(outSecProfiles)) Then  
            For I = 0 To UBound(outSecProfiles)  
                Set secProfileGrpFeat = outSecProfiles(I)  
                Set secProfileGrp = secProfileGrpFeat.**GetSpecificFeature2**  
                If Not secProfileGrp Is Nothing Then  
                 Debug.Print "Number of members in profile group: " & secProfileGrp.**GetStructureSystemMemberCount**  
                  SecMemberArray = secProfileGrp.**GetStructureSystemMembers**()  
                    If (Not IsEmpty(SecMemberArray)) Then  
                        For j = 0 To UBound(SecMemberArray)  
                            Set secMemberData = SecMemberArray(j)  
                        Next  
                    End If  
                End If  
            Next  
    End If

    Set memTochange = secMemberData

    Set SecMemFeat = memTochange.**GetFeature**()  
    memTochange.**StartEndExtendD1** = 0.2  
    memTochange.**StartEndExtendD2** = 0.1  
     
    Set secMemDatTochange = memTochange  
    secMemDatTochange.**SecondaryMemberOffsetType** = 1  
    secMemDatTochange.**LengthRatioMember1** = 0.1  
    secMemDatTochange.**LengthRatioMember2** = 0.2  
    stat = SecMemFeat.**ModifyDefinition**(secMemberData, modDoc, Nothing)  
  
'Create secondary structure system up to member  
     
    Set structMemDef = modDocExt.**CreateStructureSystemMemberData**(6)

    Debug.Print "Structure system member type as defined by swStructureSystemMemberType\_e: " & structMemDef.**StructureSystemMemberType**  
     
    structMemDef.**StartEndExtendD1** = 0#  
    Debug.Print "Start/end direction 1: " & structMemDef.**StartEndExtendD1**  
    structMemDef.**StartEndExtendD2** = 0#  
    Debug.Print "Start/end direction 2: " & structMemDef.**StartEndExtendD2**  
     
    Set profDef = structMemDef.**MemberProfile**  
     
    profDef.**ProfileStandard** = "ansi inch"  
    profDef.**ProfileType** = "pipe"  
    profDef.**ProfileSize** = "0.5 sch 40"  
     
    Set secDef = structMemDef  
    Debug.Print "Secondary member type as defined by swStructureSystemMemberCreationType\_e: " & secDef.SecondaryMemberType  
     
    Set UpToMemDef = secDef  
     
    UpToMemDef.**MemberPointParametersType** = swSecondaryMemberUpToMembersMemberPointParameters\_e.swSecondaryMemberUpToMembersMemberPointParameters\_FromPoint  
     
    Stop  'Multi-select a Member1 vertex in the graphics area and Member2 in the FeatureManager Design tree

    Set point = swSelMgr.GetSelectedObject6(1, 0)  
    Set Members(0) = swSelMgr.GetSelectedObject6(2, 0)  
     
    Call UpToMemDef.**SetFromPoint**(point)  
    UpToMemDef.**SetFromPointMembers**(Members)  
     
    UpToMemDef.**SecondaryMemberOffsetType** = swSecondaryMemberUpToMembersDistanceFromEndType\_Distance  
    UpToMemDef.**DistanceMember** = 0.1  
    UpToMemDef.**RevDirectionDistanceMember** = False  
     
    Set memData(0) = structMemDef  
    memDataArray = memData  
     
    Dim structSysFeat3 As SldWorks.Feature  
    Set structSysFeat3 = modDocExt.**CreateStructureSystem**(Nothing, memDataArray)  
     
End Sub

Example

[Create Secondary Structure System Members (VB.NET)](Create_Secondary_SSMembers_Example_VBNET.htm)  
[Create Secondary Structure System Members (C#)](Create_Secondary_SSMembers_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISecondaryMemberBetweenPointsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
