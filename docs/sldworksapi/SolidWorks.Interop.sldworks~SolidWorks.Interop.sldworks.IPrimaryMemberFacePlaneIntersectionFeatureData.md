# IPrimaryMemberFacePlaneIntersectionFeatureData Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberFacePlaneIntersectionFeatureData`

Allows access to a structure system member created along the intersection of a face or surface with a plane.
Allows access to a structure system member created along the intersection of a face or surface with a plane.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IPrimaryMemberFacePlaneIntersectionFeatureData 
```

```

Dim instance As IPrimaryMemberFacePlaneIntersectionFeatureData
```

```

public interface IPrimaryMemberFacePlaneIntersectionFeatureData 
```

```

public interface class IPrimaryMemberFacePlaneIntersectionFeatureData 
```

Remarks

See the [IStructureSystemFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemFolder.md) Remarks.

For more information, see the **SOLIDWORKS user-interface help > Weldments and Structure System > Structure System > PrimaryMember PropertyManager** topic.

Example

'VBA

'==========================================================================================

'Preconditions:

'1. Ensure the specified part template exists.

'2. Open an Immediate window.

'3. Press F5.

'

'Postconditions:

' 1. Creates **Boss-Extrude1** and **Plane1** in a new part.

' 2. Selects a parameter face on the extrusion.

' 3. Selects Plane1.

' 4. Creates a face plane intersection member along the intersection of the selected face and plane.

' 5. Creates a **Structure System1**.

' 6. Inspect the member on **Plane1** in the graphics area.

' 7. Press F5 to edit the structure system.

' 8. Gets all of the structure system members in all of the profile group folders.

' 9. Changes the member extension lengths in directions 1 and 2.

'10. Selects the **Right Plane** to intersect the parameter face.

'11. Modifies the structure system.

'12. Inspect the member move to the **Right Plane** in the graphics area.

'========================================================================

Dim swApp As SldWorks.SldWorks

Dim modDoc As SldWorks.ModelDoc2

Dim swFeatMgr As SldWorks.FeatureManager

Dim swSelMgr As SldWorks.SelectionMgr

Dim modDocExt As SldWorks.ModelDocExtension

Dim structMemDef As SldWorks.StructureSystemMemberFeatureData

Dim profDef As SldWorks.StructureSystemMemberProfile

Dim PrimDef As SldWorks.PrimaryStructuralMemberFeatureData

Dim facePlaneIntrSecDef As SldWorks.PrimaryMemberFacePlaneIntersectionFeatureData

Dim faces(0) As Object

Dim stat As Boolean

Dim IntSecPlane(0) As Object

Dim memData(0) As SldWorks.StructureSystemMemberFeatureData

Dim memDataArray As Variant

Dim structSys As SldWorks.Feature

Dim structSysModDef As SldWorks.StructureSystemFolder

Dim outProfiles As Variant

Dim MemberData As SldWorks.StructureSystemMemberFeatureData

Dim memberArray As Variant

Dim profileGrpFeat As SldWorks.Feature

Dim profileGrp As SldWorks.ProfileGroupFolder

Dim memTochange As SldWorks.StructureSystemMemberFeatureData

Dim faceIntrMemberToChange As SldWorks.PrimaryMemberFacePlaneIntersectionFeatureData

Dim newIntSecPlane(0) As Object

Dim feat As Feature

Dim I As Long

Dim j As Long

Option Explicit

Sub main()

    Set swApp = Application.SldWorks

   

    Dim swSheetWidth As Double

    swSheetWidth = 0

    Dim swSheetHeight As Double

    swSheetHeight = 0

    Set modDoc = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2022\templates\Part.PRTDOT", 0, swSheetWidth, swSheetHeight)

    Dim swPart As SldWorks.PartDoc

    Set swPart = modDoc

    Set modDoc = swApp.ActiveDoc

  

    Set modDocExt = modDoc.Extension

    Set swSelMgr = modDoc.SelectionManager

  

    stat = modDocExt.SelectByID2("Right Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)

    modDoc.SketchManager.InsertSketch True

    modDoc.ClearSelection2 True

    stat = modDocExt.SetUserPreferenceToggle(swUserPreferenceToggle\_e.swSketchAddConstToRectEntity, swUserPreferenceOption\_e.swDetailingNoOptionSpecified, False)

    stat = modDocExt.SetUserPreferenceToggle(swUserPreferenceToggle\_e.swSketchAddConstLineDiagonalType, swUserPreferenceOption\_e.swDetailingNoOptionSpecified, True)

    Dim vSkLines As Variant

    vSkLines = modDoc.SketchManager.CreateCornerRectangle(-1.68788132580097E-02, 1.16544186781496E-02, 0, 1.39317188796271E-02, -7.36773594595662E-03, 0)

    

    modDoc.ShowNamedView2 "\*Trimetric", 8

    modDoc.ViewZoomtofit2

    Dim myFeature As SldWorks.Feature

    Set myFeature = modDoc.FeatureManager.FeatureExtrusion2(False, False, False, 0, 0, 0.2, 0.2, False, False, False, False, 1.74532925199433E-02, 1.74532925199433E-02, False, False, False, False, True, True, True, 0, 0, False)

    swSelMgr.EnableContourSelection = False

    stat = modDocExt.SelectByRay(0.199999999999932, 2.80649656951937E-03, 8.80259028576802E-04, -0.400036026779314, -0.515038074910018, -0.758094294050287, 1.11139990390966E-03, 2, False, 0, 0)

    Dim myRefPlane As SldWorks.RefPlane

    Set myRefPlane = modDoc.FeatureManager.**InsertRefPlane**(4, 0, 0, 0, 0, 0)

    modDoc.ClearSelection2 True

  

    'Configure a structure system face plane intersection member

    Set structMemDef = modDocExt.**CreateStructureSystemMemberData**(3)

    Debug.Print "Type of structure system member as defined by swStructureSystemMemberType\_e: " & structMemDef.StructureSystemMemberType

                  

    structMemDef.**StartEndExtendD1** = 0.4

    Debug.Print "Extend length in direction 1: " & structMemDef.**StartEndExtendD1**

    structMemDef.**StartEndExtendD2** = 0.15

    Debug.Print "Extend length in direction 2: " & structMemDef.**StartEndExtendD2**

  

    Set profDef = structMemDef.**MemberProfile**

  

    profDef.**ProfileStandard** = "ansi inch"

    profDef.**ProfileType** = "c channel"

    profDef.**ProfileSize** = "3 x 5"

  

    Set PrimDef = structMemDef

    Debug.Print "Structure system primary member creation type as defined by swStructureSystemMemberCreationType\_e: " & PrimDef.**PrimaryMemberType**

  

    Set facePlaneIntrSecDef = PrimDef

             

    facePlaneIntrSecDef.**MergeTangentMembers** = False

  

    'Select parameter face and intersecting plane

    stat = modDocExt.SelectByRay(-1.7443058891331E-04, 1.16544186780629E-02, -4.26704146832435E-04, -0.400036026779314, -0.515038074910018, -0.758094294050287, 1.89520697225961E-04, 2, False, 0, 0)

    stat = modDocExt.SelectByID2("Plane1", "PLANE", 0, 0, 0, True, 0, Nothing, 0)

    

    Set faces(0) = swSelMgr.GetSelectedObject6(1, -1)

    

    stat = facePlaneIntrSecDef.**SetParameterFaces**(faces)

    Debug.Print "Member's parameter face set successfully: " & stat

    

    Set IntSecPlane(0) = swSelMgr.GetSelectedObject6(2, -1)

    

    stat = facePlaneIntrSecDef.**SetIntersectingPlanesAndFaces**(IntSecPlane)

    Debug.Print "Member's intersecting plane set successfully: " & stat

  

    Set memData(0) = structMemDef

    

    memDataArray = memData

  

    'Create Structure System1 in the FeatureManager design tree

    Set structSys = modDocExt.**CreateStructureSystem**(memDataArray, Nothing)

  

    modDoc.ViewZoomtofit2

  

    Stop

  

    Debug.Print ""

    Debug.Print "Edit Structure System1..."

  

    Set structSysModDef = structSys.**GetSpecificFeature2**()

    Debug.Print "Number of structure system profile groups: " & structSysModDef.**GetProfileGroupFoldersCount**

  

    outProfiles = structSysModDef.**GetProfileGroupFolders**()

  

    If (Not IsEmpty(outProfiles)) Then

                For I = 0 To UBound(outProfiles)

                    Set profileGrpFeat = outProfiles(I)

                    Set profileGrp = profileGrpFeat.**GetSpecificFeature2**

                    If Not profileGrp Is Nothing Then

                     Debug.Print "Number of members inside group: " & profileGrp.**GetStructureSystemMemberCount**

                      memberArray = profileGrp.**GetStructureSystemMembers**()

                        If (Not IsEmpty(memberArray)) Then

                            For j = 0 To UBound(memberArray)

                            Set MemberData = memberArray(j)

                              Exit For

                             Next

                        End If

                    End If

                Next

    End If

    Set memTochange = MemberData

    Set feat = memTochange.**GetFeature**()

  

    Debug.Print "Change member extensions in directions 1 and 2..."

    memTochange.**StartEndExtendD1** = 0.1

    memTochange.**StartEndExtendD2** = 0.2

           

    Set faceIntrMemberToChange = memTochange

  

    modDoc.ClearSelection2 True

  

    stat = modDocExt.SelectByID2("Right Plane", "PLANE", 0, 0, 0, True, 0, Nothing, 0)

    Set newIntSecPlane(0) = swSelMgr.GetSelectedObject6(1, -1)

    stat = faceIntrMemberToChange.**SetIntersectingPlanesAndFaces**(newIntSecPlane)

    Debug.Print "Intersecting plane successfully changed: " & stat

  

    stat = feat.**ModifyDefinition**(MemberData, modDoc, Nothing)

  

End Sub

Example

[Create Face Plane Intersection Structure System Member (VB.NET)](Create_Face_Plane_Intersection_SSMember_Example_VBNET.htm)  
[Create Face Plane Intersection Structure System Member (C#)](Create_Face_Plane_Intersection_SSMember_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPrimaryMemberFacePlaneIntersectionFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberFacePlaneIntersectionFeatureData_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
