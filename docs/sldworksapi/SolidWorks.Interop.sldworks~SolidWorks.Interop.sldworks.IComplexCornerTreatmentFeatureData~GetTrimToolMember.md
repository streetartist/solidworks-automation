# GetTrimToolMember Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData~GetTrimToolMember`

Gets the specified trim tool member for this complex corner treatment.
Gets the specified trim tool member for this complex corner treatment.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTrimToolMember( _
   ByRef MemberObjType As System.Integer _
) As System.Object
```

```

Dim instance As IComplexCornerTreatmentFeatureData
Dim MemberObjType As System.Integer
Dim value As System.Object
 
value = instance.GetTrimToolMember(MemberObjType)
```

```

System.object GetTrimToolMember( 
   out System.int MemberObjType
)
```

```

System.Object^ GetTrimToolMember( 
   [Out] System.int MemberObjType
) 
```

#### Parameters

*MemberObjType*
:   Trim tool member object to return as defined by [swTrimToolMemberObjectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTrimToolMemberObjectType_e.html)

#### Return Value

[ICornerMember](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerMember.md) or [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Example

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComplexCornerTreatmentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData.md)  
[IComplexCornerTreatmentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData_members.md)
