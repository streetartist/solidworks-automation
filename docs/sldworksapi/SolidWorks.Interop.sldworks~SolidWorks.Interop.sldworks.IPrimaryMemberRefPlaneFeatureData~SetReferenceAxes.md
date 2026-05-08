# SetReferenceAxes Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData~SetReferenceAxes`

Sets the direction reference(s) for this structure system member.
Sets the direction reference(s) for this structure system member.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetReferenceAxes( _
   ByVal RetEntities As System.Object _
) As System.Boolean
```

```

Dim instance As IPrimaryMemberRefPlaneFeatureData
Dim RetEntities As System.Object
Dim value As System.Boolean
 
value = instance.SetReferenceAxes(RetEntities)
```

```

System.bool SetReferenceAxes( 
   System.object RetEntities
)
```

```

System.bool SetReferenceAxes( 
   System.Object^ RetEntities
) 
```

#### Parameters

*RetEntities*
:   Array of parallel [IRefPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md)s and/or [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)s

#### Return Value

True if reference axes successfully set, false if not

Remarks

The number of members created = ([IPrimaryMemberRefPlaneFeatureData::GetReferenceAxes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData~GetReferenceAxes.md) \* [IPrimaryMemberRefPlaneFeatureData::GetReferenceLocations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData~GetReferenceLocations.md))

During:

- creation, you can set any number of entities that are intersecting with the start and end reference ([IPrimaryMemberRefPlaneFeatureData::GetStartAndEndReferences](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData~GetStartAndEndReferences.md)).
- editing, you can set only one entity that intersects with the start and end reference.

Example

See the [IPrimaryMemberRefPlaneFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPrimaryMemberRefPlaneFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData.md)  
[IPrimaryMemberRefPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData_members.md)
