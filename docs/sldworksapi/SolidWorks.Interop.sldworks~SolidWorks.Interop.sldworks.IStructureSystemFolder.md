# IStructureSystemFolder Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemFolder`

Allows access to a structure system folder.
Allows access to a structure system folder.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IStructureSystemFolder 
```

```

Dim instance As IStructureSystemFolder
```

```

public interface IStructureSystemFolder 
```

```

public interface class IStructureSystemFolder 
```

Remarks

This interface accesses the top-level folder of a structure system in the FeatureManager design tree. The structure system folder contains one or more profile group folders. Each profile group folder contains profile references and structure system members.

When a structure system is created in the user interface, the Corner Management PropertyManager opens automatically. When structure systems are created using the API, a Corner Management*X* folder is automatically created for each structure system in the FeatureManager design tree.

A structure system and its corner management folder appears similar to the following in the FeatureManager design tree. In parentheses are the APIs that you use to access the corresponding item:

- **Structure System1** (IStructureSystemFolder accessors)

  - **Structure System Grid1**

  - **<ansi inch> <c channel><3 x 5> (1)** ([IProfileGroupFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileGroupFolder.md) accessors)

     - **Plane2** (profile reference plane - [IProfileGroupFolder::GetPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileGroupFolder~GetPlane.md))

     - **Sketch11** (profile sketch - [IProfileGroupFolder::GetSketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileGroupFolder~GetSketch.md))

     - **Member1** (structure system member - [IProfileGroupFolder::GetStructureSystemMembers](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileGroupFolder~GetStructureSystemMembers.md))

- **Corner Management1** ([ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.md) accessors)

  - **Complex Corner Group1** ([ICornerTreatmentGroupFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerTreatmentGroupFolder.md) accessors)

     - **Corner5** ([ICornerTreatmentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerTreatmentFeatureData.md) accessors and then cast to [IComplexCornerTreatmentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData.md))

     - more corners...

     (Each corner in a complex corner group contains multiple corner members. If you edit a corner to open a Corner Management PropertyManager in the user interface, on the Complex tab are three boxes that list corner members for Trim Tool, Body Trim, and Planar Trim. Use [ICornerMember](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerMember.md) to access these corner members.)

  - **Two member Corner Group1** (ICornerTreatmentGroupFolder accessors)

     - **Corner1**(ICornerTreatmentFeatureData accessors and then cast to [ITwoMemberCornerTreatmentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITwoMemberCornerTreatmentFeatureData.md))

     - more corners...

     (Each corner in a two member corner group contains two corner members, one for Trim Tool, and one for Body Trim. Use ICornerMember to access these corner members.)

  - **Simple Corner Group1** (ICornerTreatmentGroupFolder accessors)

     - **Corner9**(ICornerTreatmentFeatureData accessors and then cast to [ISimpleCornerTreatmentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleCornerTreatmentFeatureData.md))

     - more corners...

To create a structure system:

1. Create an [IStructureSystemMemberFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberFeatureData.md) object for every primary and secondary structure system member you intend to create.
2. Create [IStructureSystemSplitMember](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemSplitMember.md) objects as needed. Use [IStructureSystemMemberFeatureData::IsSplit](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberFeatureData~IsSplit.md) to indicate that split members exist.
3. Create one or more [IStructureSystemMemberProfile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile.md) objects as the number of different profiles is needed.
4. Cast the IStructureSystemMemberFeatureData objects to [IPrimaryStructuralMemberFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryStructuralMemberFeatureData.md) objects and  [ISecondaryStructuralMemberFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryStructuralMemberFeatureData.md) objects as needed.
5. Create specific primary member feature data objects by casting IPrimaryStructuralMemberFeatureData objects to:  
     
     -  [IPrimaryMemberFacePlaneIntersectionFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberFacePlaneIntersectionFeatureData.md)  
     -  [IPrimaryMemberPathSegmentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPathSegmentFeatureData.md)  
     -  [IPrimaryMemberPointLengthFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData.md)  
     -  [IPrimaryMemberRefPlaneFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData.md)
6. Create specific secondary member feature data objects by casting ISecondaryStructuralMemberFeatureData objects to:  
     
     -  [ISecondaryMemberBetweenPointsFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData.md)  
     -  [ISecondaryMemberSupportPlaneFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberSupportPlaneFeatureData.md)
7. Use the methods and properties on the specific primary and secondary member feature data objects to detail the structure system members.
8. Call [IModelDocExtension::CreateStructureSystem](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateStructureSystem.md)(*primaryFDArray*, *secondaryFDArray*), where *primaryFDArray* is an array of primary IStructureSystemMemberFeatureData objects and *secondaryFDArray* is an array of secondary IStructureSystemMemberFeatureData objects created in step 1.

To edit a structure system:

1. Get the structure system folder feature, which is returned by IModelDocExtension::CreateStructureSystem in step 8 above. Then call the accessor of this interface, IFeature::GetSpecificFeature2.  
   (Or call both accessors of this interface.)
2. Use [IStructureSystemFolder::GetProfileGroupFolders](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemFolder~GetProfileGroupFolders.md) to access the profile group folders in a structure system folder.
3. Use IProfileGroupFolder methods and properties to get the sketch, reference plane, and structure system members in each profile group folder.
4. Use [IStructureSystemMemberFeatureData::StructureSystemMemberType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberFeatureData~StructureSystemMemberType.md) to determine whether a structure system member retrieved in step 3 is a primary or a secondary member.
5. Call [IStructureSystemMemberFeatureData::AccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberFeatureData~AccessSelections.md) before editing the selections used to create the structure system. Call [IStructureSystemMemberFeatureData::ReleaseSelectionAccess](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberFeatureData~ReleaseSelectionAccess.md) after editing.
6. Cast IStructureSystemMemberFeatureData objects to their subclass feature data objects (see create steps 5 and 6).
7. If you need to change a structure member's profile, use [IStructureSystemMemberFeatureData::MemberProfile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberFeatureData~MemberProfile.md) to get the IStructureSystemMemberProfile object for each structure member.
8. Complete the structure system edit by calling [IStructureSystemMemberFeatureData::GetFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberFeatureData~GetFeature.md), calling methods and properties on objects retrieved in previous steps as required, and finally calling [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.md).

Use the examples as models to create and edit structure sytems in your own applications.

For more information, read the **SOLIDWORKS user-interface help > Weldments and Structure System > Structure System** topics.

Example

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.md) examples.

See the [IPrimaryMemberFacePlaneIntersectionFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberFacePlaneIntersectionFeatureData.md) examples.

See the [IPrimaryMemberPointLengthFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData.md) examples.

See the [IPrimaryMemberPathSegmentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPathSegmentFeatureData.md) examples.

See the [IPrimaryMemberRefPlaneFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData.md) examples.

See the [ISecondaryMemberBetweenPointsFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IStructureSystemFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemFolder_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
