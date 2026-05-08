# SetReferenceLocations Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData~SetReferenceLocations`

Gets the location reference(s) used to create this structure system member.
Gets the location reference(s) used to create this structure system member.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetReferenceLocations( _
   ByVal RetEntities As System.Object _
) As System.Boolean
```

```

Dim instance As IPrimaryMemberRefPlaneFeatureData
Dim RetEntities As System.Object
Dim value As System.Boolean
 
value = instance.SetReferenceLocations(RetEntities)
```

```

System.bool SetReferenceLocations( 
   System.object RetEntities
)
```

```

System.bool SetReferenceLocations( 
   System.Object^ RetEntities
) 
```

#### Parameters

*RetEntities*
:   Array of parallel [IRefPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md)s and/or [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)s

#### Return Value

True if location references successfully set, false if not

Remarks

The number of members created = ([IPrimaryMemberRefPlaneFeatureData::GetReferenceAxes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData~GetReferenceAxes.md) \* [IPrimaryMemberRefPlaneFeatureData::GetReferenceLocations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData~GetReferenceLocations.md))

During:

- creation, you can set any number of entities that are intersecting with the start and end references and at least one reference axis entity.
- editing, you can set only one entity that is intersecting with the start and end refereces and one reference axis entity.

Example

See the [IPrimaryMemberRefPlaneFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPrimaryMemberRefPlaneFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData.md)  
[IPrimaryMemberRefPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData_members.md)
