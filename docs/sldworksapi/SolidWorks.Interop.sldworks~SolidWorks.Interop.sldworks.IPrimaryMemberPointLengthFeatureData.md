# IPrimaryMemberPointLengthFeatureData Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData`

Allows access to a structure system member originating at a point and extending to a specified end condition.
Allows access to a structure system member originating at a point and extending to a specified end condition.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IPrimaryMemberPointLengthFeatureData 
```

```

Dim instance As IPrimaryMemberPointLengthFeatureData
```

```

public interface IPrimaryMemberPointLengthFeatureData 
```

```

public interface class IPrimaryMemberPointLengthFeatureData 
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
' 1. Creates **Sketch1**, **Sketch2**, and **Sketch3** in a new part.  
' 2. Configures the start/end extensions and the member profile.  
' 3. Configures the length end condition for the structure members.  
' 4. Selects three sketch points.  
' 5. Specifies the length.  
' 6. Creates a **Structure System1** with three structure system point length members.  
' 7. Inspect the structure system in the graphics area.  
' 8. Press F5 to edit the structure system.  
' 9. Gets one structure system member..  
'10. Changes the length and member extensions in directions 1 and 2.  
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
Dim memPointLengthDef As SldWorks.PrimaryMemberPointLengthFeatureData  
Dim startPoints(2) As Object  
Dim stat As Boolean  
Dim memData(0) As SldWorks.StructureSystemMemberFeatureData  
Dim memDataArray As Variant  
Dim systemFeature As SldWorks.Feature  
Dim structSysModDef As SldWorks.StructureSystemFolder  
Dim outProfiles As Variant  
Dim MemberData As SldWorks.StructureSystemMemberFeatureData  
Dim memberArray As Variant  
Dim profileGrpFeat As SldWorks.Feature  
Dim profileGrp As SldWorks.ProfileGroupFolder  
Dim memTochange As SldWorks.StructureSystemMemberFeatureData  
Dim pointLengthMember As SldWorks.PrimaryMemberPointLengthFeatureData  
Dim memberFeat As SldWorks.Feature  
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
     
    modDoc.SketchManager.InsertSketch True  
    stat = modDocExt.SelectByID2("Front Plane", "PLANE", -3.78286223842605E-02, 4.26130572878663E-02, -8.98903374939048E-03, False, 0, Nothing, 0)  
    modDoc.ClearSelection2 True  
    Dim skPoint As SldWorks.SketchPoint  
    Set skPoint = modDoc.SketchManager.CreatePoint(-0.040799, 0.008094, 0#)  
    modDoc.ClearSelection2 True  
    modDoc.SketchManager.InsertSketch True  
    stat = modDocExt.SelectByID2("Top Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)  
    modDoc.SketchManager.InsertSketch True  
    Set skPoint = modDoc.SketchManager.CreatePoint(-0.023183, 0.004864, 0#)  
    modDoc.ClearSelection2 True  
    modDoc.SketchManager.InsertSketch True  
    stat = modDocExt.SelectByID2("Right Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)  
    modDoc.SketchManager.InsertSketch True  
    Set skPoint = modDoc.SketchManager.CreatePoint(-0.020877, 0.010539, 0#)  
    modDoc.ClearSelection2 True  
    modDoc.SketchManager.InsertSketch True

    modDoc.ClearSelection2 True  
    modDoc.ShowNamedView2 "\*Trimetric", 8  
    modDoc.ViewZoomtofit2  
     
    'Configure a structure system point length member  
    Set structMemDef = modDocExt.**CreateStructureSystemMemberData**(2)  
     
    Debug.Print "Type of structure system member as defined by swStructureSystemMemberType\_e: " & structMemDef.**StructureSystemMemberType**  
                     
    structMemDef.**StartEndExtendD1** = 1#  
    Debug.Print "Extend length in direction 1: " & structMemDef.**StartEndExtendD1**  
    structMemDef.**StartEndExtendD2** = 2#  
    Debug.Print "Extend length in direction 2: " & structMemDef.**StartEndExtendD2**  
     
    Set profDef = structMemDef.**MemberProfile**  
     
    profDef.**ProfileStandard** = "ansi inch"  
    profDef.**ProfileType** = "c channel"  
    profDef.**ProfileSize** = "3 x 5"  
     
    Set PrimDef = structMemDef  
    Debug.Print "Structure system primary member creation type as defined by swStructureSystemMemberCreationType\_e: " & PrimDef.**PrimaryMemberType**; ""  
     
    Set memPointLengthDef = PrimDef  
                    
    memPointLengthDef.**EndCondition** = 0  
     
    'Set three points that define three structure system point length members  
    stat = modDocExt.SelectByID2("Point1@Sketch3", "EXTSKETCHPOINT", -0.020877, 0.010539, 0, False, 0, Nothing, 0)  
    stat = modDocExt.SelectByID2("Point1@Sketch1", "EXTSKETCHPOINT", -0.040799, 0.008094, 0, True, 0, Nothing, 0)  
    stat = modDocExt.SelectByID2("Point1@Sketch2", "EXTSKETCHPOINT", -0.023183, 0.004864, 0, True, 0, Nothing, 0)

    Set startPoints(0) = swSelMgr.GetSelectedObject6(1, 0)  
    Set startPoints(1) = swSelMgr.GetSelectedObject6(2, 0)  
    Set startPoints(2) = swSelMgr.GetSelectedObject6(3, 0)  
     
    stat = memPointLengthDef.**SetPoints**(startPoints)  
    Debug.Print "Start points set successfully: " & stat  
       
    'Set the length for each member  
    memPointLengthDef.**Length** = 5  
    memPointLengthDef.**ReverseDirection** = False

    Set memData(0) = structMemDef  
       
    memDataArray = memData  
       
    Set systemFeature = modDocExt.**CreateStructureSystem**(memDataArray, Nothing)  
     
    modDoc.ViewZoomtofit2  
     
    Stop  
       
    Set structSysModDef = systemFeature.**GetSpecificFeature2**  
    Debug.Print "Number of structure system profile groups: " & structSysModDef.**GetProfileGroupFoldersCount**  
     
    outProfiles = structSysModDef.**GetProfileGroupFolders**()  
     
    If (Not IsEmpty(outProfiles)) Then  
            For I = 0 To UBound(outProfiles)  
                Set profileGrpFeat = outProfiles(I)  
                Set profileGrp = profileGrpFeat.**GetSpecificFeature2**  
                If Not profileGrp Is Nothing Then  
                    Debug.Print "Number of members inside profile group " & profileGrp.**GetStructureSystemMemberCount**  
                    memberArray = profileGrp.**GetStructureSystemMembers**()  
                    If (Not IsEmpty(memberArray)) Then  
                        For j = 0 To UBound(memberArray)  
                            Set MemberData = memberArray(j) 'Get one structure system member to change  
                            Exit For  
                        Next  
                    End If  
                End If  
            Next  
    End If

    'Changing one member only  
    Set memTochange = MemberData  
     
    Debug.Print "Change member length and extensions in directions 1 and 2 for one member only"  
    memTochange.**StartEndExtendD1** = 0.1  
    memTochange.**StartEndExtendD2** = 0.1  
     
    Set pointLengthMember = MemberData  
    pointLengthMember.**Length** = 1  
    
    'Save edits  
    Set memberFeat = memTochange.**GetFeature**()  
    stat = memberFeat.**ModifyDefinition**(MemberData, modDoc, Nothing)

End Sub

Example

[Create Point Length Structure System Member (VB.NET)](Create_Point_Length_SSMember_Example_VBNET.htm)  
[Create Point Length Structure System Member (C#)](Create_Point_Length_SSMember_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPrimaryMemberPointLengthFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
