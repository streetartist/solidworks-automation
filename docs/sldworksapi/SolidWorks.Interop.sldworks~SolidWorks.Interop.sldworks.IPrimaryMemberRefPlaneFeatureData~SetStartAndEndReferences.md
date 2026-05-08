# SetStartAndEndReferences Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData~SetStartAndEndReferences`

Sets the start and end reference entities that are used to define the length of this structure system member.
Sets the start and end reference entities that are used to define the length of this structure system member.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetStartAndEndReferences( _
   ByVal RetEntities As System.Object _
) As System.Boolean
```

```

Dim instance As IPrimaryMemberRefPlaneFeatureData
Dim RetEntities As System.Object
Dim value As System.Boolean
 
value = instance.SetStartAndEndReferences(RetEntities)
```

```

System.bool SetStartAndEndReferences( 
   System.object RetEntities
)
```

```

System.bool SetStartAndEndReferences( 
   System.Object^ RetEntities
) 
```

#### Parameters

*RetEntities*
:   Array of parallel [IRefPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md)s and/or [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)s

#### Return Value

True if start and end references successfully set, false if not

Remarks

The array set by this method should have only two entities: start and end references.

Example

See the [IPrimaryMemberRefPlaneFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPrimaryMemberRefPlaneFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData.md)  
[IPrimaryMemberRefPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData_members.md)
