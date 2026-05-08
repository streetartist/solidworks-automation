# IPrimaryMemberPathSegmentFeatureData Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPathSegmentFeatureData`

Allows access to a structure system member created along path segments in a sketch.
Allows access to a structure system member created along path segments in a sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IPrimaryMemberPathSegmentFeatureData 
```

```

Dim instance As IPrimaryMemberPathSegmentFeatureData
```

```

public interface IPrimaryMemberPathSegmentFeatureData 
```

```

public interface class IPrimaryMemberPathSegmentFeatureData 
```

Remarks

See the [IStructureSystemFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemFolder.md) Remarks.

For more information, see the **SOLIDWORKS user-interface help > Weldments and Structure System > Structure System > PrimaryMember PropertyManager** topic.

Example

'VBA

'This example creates primary structure system path segment members that are split along a reference plane.

'==========================================================================================  
'Preconditions:  
'1. Ensure the specified part template exists.  
'2. Open an Immediate window.  
'3. Press F5.  
'  
'Postconditions:  
' 1. Creates **Sketch1** containing two sketch segments.  
' 2. Creates **Plane1**.  
' 3. Configures the start/end extensions and the member profile.  
' 4. Selects two sketch segments and **Plane1**.  
' 5. Configures structure system to split members using **Plane1**.  
' 6. Creates a **Structure System1** with four split members: **Member1\_1**, **Member1\_2**, **Member2\_1**, and **Member2\_2**.  
' 7. Inspect the structure system in the graphics area.  
' 8. Press F5 to edit the structure system.  
' 9. Changes the start/end extensions for **Member1\_1** and **Member1\_2**.  
'10. Modifies the structure system.  
'11. Inspect the changes in the graphics area.  
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
Dim segments(1) As Object  
Dim stat As Boolean  
Dim memData(0) As SldWorks.StructureSystemMemberFeatureData  
Dim memDataArray As Variant  
Dim structSys As SldWorks.Feature  
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
     
    Set modDocExt = modDoc.Extension  
    Set swSelMgr = modDoc.SelectionManager

    modDoc.SketchManager.InsertSketch True  
    stat = modDocExt.SelectByID2("Front Plane", "PLANE", -5.50812963393624E-02, 2.28249965575248E-02, 1.35586835718293E-02, False, 0, Nothing, 0)  
    modDoc.ClearSelection2 True  
    Dim skSegment As Object  
    Set skSegment = modDoc.SketchManager.CreateLine(-0.036101, -0.017052, 0#, 0.03111, 0.018383, 0#)  
    Set skSegment = modDoc.SketchManager.CreateLine(0.055067, -0.015222, 0#, -0.01281, -0.055483, 0#)

    modDoc.SketchManager.InsertSketch True  
    modDoc.ClearSelection2 True  
     
    stat = modDocExt.SelectByID2("Right Plane", "PLANE", 0, 0, 0, True, 0, Nothing, 0)  
    Dim myRefPlane As SldWorks.RefPlane  
    Set myRefPlane = modDoc.FeatureManager.InsertRefPlane(8, 0.02, 0, 0, 0, 0)  
    modDoc.ClearSelection2 True  
     
    stat = modDocExt.SelectByID2("Line1@Sketch1", "EXTSKETCHSEGMENT", -1.23094293114227E-02, -4.50860223252535E-03, 0, True, 0, Nothing, 0)  
    stat = modDocExt.SelectByID2("Line2@Sketch1", "EXTSKETCHSEGMENT", 1.11728134432853, -3.76344266391984E-02, 0, True, 0, Nothing, 0)  
    stat = modDocExt.SelectByID2("Plane1", "PLANE", 1.99883401957978E-02, 2.02450835544425E-02, -2.43017856732353E-02, True, 0, Nothing, 0)  
     
    Set structMemDef = modDocExt.**CreateStructureSystemMemberData**(0)  
     
    Debug.Print "Type of structure system member as defined by swStructureSystemMemberType\_e: " & structMemDef.**StructureSystemMemberType**  
                     
    structMemDef.**StartEndExtendD1** = 0.1  
    Debug.Print "Extend length in direction 1 (m): " & structMemDef.StartEndExtendD1  
    structMemDef.**StartEndExtendD2** = 0.2  
    Debug.Print "Extend length in direction 2 (m): " & structMemDef.StartEndExtendD2

    Set profDef = structMemDef.**MemberProfile**  
     
    profDef.**ProfileStandard** = "ansi inch"  
    profDef.**ProfileType** = "c channel"  
    profDef.**ProfileSize** = "3 x 5"

    Set PrimDef = structMemDef  
    Debug.Print "Structure system primary member creation type as defined by swStructureSystemMemberCreationType\_e: " & PrimDef.**PrimaryMemberType**  
     
    Set memPathSegDef = PrimDef  
    memPathSegDef.**MergeTangentMembers** = True  
    Debug.Print "Merge tangent members? " & memPathSegDef.**MergeTangentMembers**

    Set segments(0) = swSelMgr.GetSelectedObject6(1, 0)  
    Set segments(1) = swSelMgr.GetSelectedObject6(2, 0)

    stat = memPathSegDef.**SetPathSegments**(segments)  
    Debug.Print "Path segments set successfully: " & stat  
     
    Dim planes(0) As Object  
    Set planes(0) = swSelMgr.GetSelectedObject6(3, 0)  
    structMemDef.**IsSplit** = True  
    Dim structSplitMember As SldWorks.StructureSystemSplitMember  
    Set structSplitMember = structMemDef.**GetSplitMember**  
    structSplitMember.**MemberType** = swStructureSplitMemberType\_e.swStructureSplitMember\_Reference  
    stat = structSplitMember.**SetSplitReferences**(planes)  
       
    Set memData(0) = structMemDef  
    memDataArray = memData  
       
    Set structSys = modDocExt.**CreateStructureSystem**(memDataArray, Nothing)  
     
    modDoc.ViewZoomtofit  
     
    Stop  
       
    'Edit the structure system  
    Set structSysModDef = structSys.**GetSpecificFeature2**  
    Debug.Print "Number of profile group folders: " & structSysModDef.**GetProfileGroupFoldersCount**  
     
    outProfiles = structSysModDef.**GetProfileGroupFolders**()

    If (Not IsEmpty(outProfiles)) Then  
                For I = 0 To UBound(outProfiles)  
                    Set profileGrpFeat = outProfiles(I)  
                    Set profileGrp = profileGrpFeat.**GetSpecificFeature2**  
                    If Not profileGrp Is Nothing Then  
                        Debug.Print "Number of members inside profile group folder: " & profileGrp.**GetStructureSystemMemberCount**  
                        memberArray = profileGrp.**GetStructureSystemMembers**()  
                        If (Not IsEmpty(memberArray)) Then  
                            For j = 0 To UBound(memberArray)  
                                Set MemberData = memberArray(j) 'Get Member1 only  
                                Exit For  
                             Next  
                        End If  
                    End If  
                Next  
    End If  
         
    Set memTochange = MemberData

    'Change the start/end extensions for Member1  
    Debug.Print "Change member extensions in directions 1 and 2 for one member only"  
    Set feat = memTochange.**GetFeature**()  
    memTochange.**StartEndExtendD1** = 0.5  
    memTochange.**StartEndExtendD2** = 0.2  
     
    'Save edits  
    stat = feat.**ModifyDefinition**(MemberData, modDoc, Nothing)  
     
End Sub

Example

[Create Path Segment Structure System Member (VB.NET)](Create_Path_Segment_SSMember_Example_VBNET.htm)  
[Create Path Segment Structure System Member (C#)](Create_Path_Segment_SSMember_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPrimaryMemberPathSegmentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPathSegmentFeatureData_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
