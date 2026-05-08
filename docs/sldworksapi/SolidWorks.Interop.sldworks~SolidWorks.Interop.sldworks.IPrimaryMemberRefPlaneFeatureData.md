# IPrimaryMemberRefPlaneFeatureData Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData`

Allows access to a structure system member created along the intersection of two or more planes.
Allows access to a structure system member created along the intersection of two or more planes.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IPrimaryMemberRefPlaneFeatureData 
```

```

Dim instance As IPrimaryMemberRefPlaneFeatureData
```

```

public interface IPrimaryMemberRefPlaneFeatureData 
```

```

public interface class IPrimaryMemberRefPlaneFeatureData 
```

Remarks

The number of members created = ([IPrimaryMemberRefPlaneFeatureData::GetReferenceAxes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData~GetReferenceAxes.md) \* [IPrimaryMemberRefPlaneFeatureData::GetReferenceLocations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData~GetReferenceLocations.md))

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
' 1. Creates five reference planes:  
'       - **Plane1** parallel to **Right Plane**  
'       - **Plane2** and **Plane3** parallel to and flanking **Top Plane**  
'       - **Plane4** and **Plane5** parallel to and flanking **Front Plane**  
' 2. Configures the member profile.  
' 3. Selects the start/end reference planes that define the lengths of the members: **Plane1** and **Right Plane**.  
' 4. Selects the axis reference planes that define the direction of the members: Plane2 and **Plane3**.  
' 5. Selects the location reference planes that define the positions of the members: **Plane4** and **Plane5**.  
' 6. Creates a **Structure System1** with nine structure system reference plane members.  
' 7. Inspect the structure system in the graphics area.  
' 8. Press F5 to edit the structure system.  
' 9. Gets **Member1**.  
'10. Changes its extensions in directions 1 and 2.  
'11. Modifies the structure system.  
'12. Inspect the changes in the graphics area.  
'========================================================================

Dim swApp As SldWorks.SldWorks  
Dim modDoc As SldWorks.ModelDoc2  
Dim swFeatMgr As SldWorks.FeatureManager  
Dim swSelMgr As SldWorks.SelectionMgr  
Dim modDocExt As SldWorks.ModelDocExtension  
Dim structMemDef As SldWorks.StructureSystemMemberFeatureData  
Dim profDef As SldWorks.StructureSystemMemberProfile  
Dim PrimDef As SldWorks.PrimaryStructuralMemberFeatureData  
Dim memRefPlaneDef As PrimaryMemberRefPlaneFeatureData  
Dim startEndPlanes(1) As Object  
Dim horzPlanes(2) As Object  
Dim vertPlanes(2) As Object  
Dim stat As Boolean  
Dim memData(0) As SldWorks.StructureSystemMemberFeatureData  
Dim memDataArray As Variant  
Dim structSysFeat As SldWorks.Feature  
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
Option Explicit  
Sub main()

    Set swApp = Application.SldWorks

    Dim swSheetWidth As Double  
    swSheetWidth = 0  
    Dim swSheetHeight As Double  
    swSheetHeight = 0  
    Set modDoc = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2022\templates\Part.PRTDOT", 0, swSheetWidth, swSheetHeight)  
     
    Set modDoc = swApp.ActiveDoc  
     
    Set swSelMgr = modDoc.SelectionManager  
    Set modDocExt = modDoc.Extension

    stat = modDocExt.SelectByID2("Right Plane", "PLANE", 0, 0, 0, True, 0, Nothing, 0)

    Dim myRefPlane As SldWorks.RefPlane  
    Set myRefPlane = modDoc.FeatureManager.InsertRefPlane(8, 0.381, 0, 0, 0, 0)  
    modDoc.ClearSelection2 True  
    stat = modDocExt.SelectByID2("Top Plane", "PLANE", 0, 0, 0, True, 0, Nothing, 0)  
    Set myRefPlane = modDoc.FeatureManager.InsertRefPlane(8, 0.1778, 0, 0, 0, 0)  
    modDoc.ClearSelection2 True  
    stat = modDocExt.SelectByID2("Plane1", "PLANE", 0, 0, 0, False, 0, Nothing, 0)  
    modDoc.ClearSelection2 True  
    stat = modDocExt.SelectByID2("Top Plane", "PLANE", 0, 0, 0, True, 0, Nothing, 0)  
    Set myRefPlane = modDoc.FeatureManager.InsertRefPlane(264, 0.1778, 0, 0, 0, 0)  
    modDoc.ClearSelection2 True  
    stat = modDocExt.SelectByID2("Plane2", "PLANE", 0, 0, 0, False, 0, Nothing, 0)  
    modDoc.ClearSelection2 True  
    stat = modDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, True, 0, Nothing, 0)  
    Set myRefPlane = modDoc.FeatureManager.InsertRefPlane(8, 0.1778, 0, 0, 0, 0)  
    modDoc.ClearSelection2 True  
    stat = modDocExt.SelectByID2("Plane3", "PLANE", 0, 0, 0, False, 0, Nothing, 0)  
    modDoc.ClearSelection2 True  
    stat = modDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, True, 0, Nothing, 0)  
    Set myRefPlane = modDoc.FeatureManager.InsertRefPlane(264, 0.1778, 0, 0, 0, 0)  
    modDoc.ClearSelection2 True  
    stat = modDocExt.SelectByID2("Plane4", "PLANE", 0, 0, 0, False, 0, Nothing, 0)  
    modDoc.ClearSelection2 True  
     
    stat = modDocExt.SelectByID2("Right Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)  
    stat = modDocExt.SelectByID2("Plane1", "PLANE", 7.29275826275853E-02, 0.103693179609365, 0.188906126602433, True, 0, Nothing, 0)  
    stat = modDocExt.SelectByID2("Plane2", "PLANE", -0.035035924945646, 8.82769827595098E-02, 0.154770056203461, True, 0, Nothing, 0)  
    stat = modDocExt.SelectByID2("Top Plane", "PLANE", 0, 0, 0, True, 0, Nothing, 0)  
    stat = modDocExt.SelectByID2("Plane3", "PLANE", -3.59335022268397E-02, 4.86897858681345E-02, 0.154489603864079, True, 0, Nothing, 0)  
    stat = modDocExt.SelectByID2("Plane4", "PLANE", -3.53613843872154E-02, 0.122848840931965, 0.120060929442332, True, 0, Nothing, 0)  
    stat = modDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, True, 0, Nothing, 0)  
    stat = modDocExt.SelectByID2("Plane5", "PLANE", -3.13617150023902E-02, 0.123208535607716, 7.98165581882131E-02, True, 0, Nothing, 0)

    'Create structure system reference plane member  
    Set structMemDef = modDocExt.**CreateStructureSystemMemberData**(1)  
    Debug.Print "Type of structure system member as defined by swStructureSystemMemberType\_e: " & structMemDef.**StructureSystemMemberType**  
                     
    Debug.Print "Extend length in direction 1 (m): " & structMemDef.**StartEndExtendD1**  
    Debug.Print "Extend length in direction 2 (m): " & structMemDef.**StartEndExtendD2**

    Set profDef = structMemDef.**MemberProfile**  
     
    profDef.ProfileStandard = "ansi inch"  
    profDef.ProfileType = "c channel"  
    profDef.ProfileSize = "3 x 5"

    Set PrimDef = structMemDef  
    Debug.Print "Structure system primary member creation type as defined by swStructureSystemMemberCreationType\_e: " & PrimDef.PrimaryMemberType; ""  
     
    Set memRefPlaneDef = PrimDef  
            
    'Define the member lengths  
    Set startEndPlanes(0) = swSelMgr.GetSelectedObject6(1, 0)  
    Set startEndPlanes(1) = swSelMgr.GetSelectedObject6(2, 0)

    stat = memRefPlaneDef.**SetStartAndEndReferences**(startEndPlanes)  
    Debug.Print "Reference planes set successfully: " & stat  
     
    Set horzPlanes(0) = swSelMgr.GetSelectedObject6(3, 0)  
    Set horzPlanes(1) = swSelMgr.GetSelectedObject6(4, 0)  
    Set horzPlanes(2) = swSelMgr.GetSelectedObject6(5, 0)  
       
    stat = memRefPlaneDef.**SetReferenceAxes**(horzPlanes)  
    Debug.Print "Reference axis planes set successfully: " & stat  
     
    Set vertPlanes(0) = swSelMgr.GetSelectedObject6(6, 0)  
    Set vertPlanes(1) = swSelMgr.GetSelectedObject6(7, 0)  
    Set vertPlanes(2) = swSelMgr.GetSelectedObject6(8, 0)  
       
    stat = memRefPlaneDef.**SetReferenceLocations**(vertPlanes)  
    Debug.Print "Reference location planes set successfully: " & stat

    Set memData(0) = structMemDef  
       
    memDataArray = memData

    Set structSysFeat = modDocExt.**CreateStructureSystem**(memDataArray, Nothing)  
     
    modDoc.ShowNamedView2 "\*Trimetric", 8  
    modDoc.ViewZoomtofit2  
     
    Stop  
   
    Set structSysModDef = structSysFeat.**GetSpecificFeature2**  
    Debug.Print "Number of profile group folders: " & structSysModDef.**GetProfileGroupFoldersCount**

    outProfiles = structSysModDef.**GetProfileGroupFolders**()

    If (Not IsEmpty(outProfiles)) Then  
                For I = 0 To UBound(outProfiles)  
                    Set profileGrpFeat = outProfiles(I)  
                    Set profileGrp = profileGrpFeat.**GetSpecificFeature2**  
                    If Not profileGrp Is Nothing Then  
                     Debug.Print "Number of members in profile group folder: " & profileGrp.GetStructureSystemMemberCount  
                      memberArray = profileGrp.**GetStructureSystemMembers**()  
                        If (Not IsEmpty(memberArray)) Then  
                            For j = 0 To UBound(memberArray)  
                                Set MemberData = memberArray(j) 'Get first member only  
                                Exit For  
                             Next  
                        End If  
                    End If  
                Next  
    End If

    Set memTochange = MemberData  
     
    Set feat = memTochange.**GetFeature**()  
     
    'Change the extensions in directions 1 and 2 for Member1  
    memTochange.**StartEndExtendD1** = 0.5  
    memTochange.**StartEndExtendD2** = 0.2

    modDoc.ClearSelection2 True  
       
    Debug.Print "Member extensions set successfully: " & stat  
       
    'Save edits  
    stat = feat.**ModifyDefinition**(MemberData, modDoc, Nothing)  
   
End Sub

Example

[Create Reference Plane Structure System Member (VB.NET)](Create_Ref_Plane_SSMember_Example_VBNET.htm)  
[Create Reference Plane Structure System Member (C#)](Create_Ref_Plane_SSMember_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPrimaryMemberRefPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
