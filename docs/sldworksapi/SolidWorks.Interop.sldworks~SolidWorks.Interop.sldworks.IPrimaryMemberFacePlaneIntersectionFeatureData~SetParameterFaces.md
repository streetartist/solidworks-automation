# SetParameterFaces Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberFacePlaneIntersectionFeatureData~SetParameterFaces`

Sets the parameter faces of this structure system member.
Sets the parameter faces of this structure system member.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetParameterFaces( _
   ByVal Faces As System.Object _
) As System.Boolean
```

```

Dim instance As IPrimaryMemberFacePlaneIntersectionFeatureData
Dim Faces As System.Object
Dim value As System.Boolean
 
value = instance.SetParameterFaces(Faces)
```

```

System.bool SetParameterFaces( 
   System.object Faces
)
```

```

System.bool SetParameterFaces( 
   System.Object^ Faces
) 
```

#### Parameters

*Faces*
:   Array of [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)s

#### Return Value

True if parameter faces successfully set, false if not

Remarks

Only [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSelectType_e.html).swSelFACES type entities can be set using this method.

At edit time you can set only one parameter face.

Example

See the [IPrimaryMemberFacePlaneIntersectionFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberFacePlaneIntersectionFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPrimaryMemberFacePlaneIntersectionFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberFacePlaneIntersectionFeatureData.md)  
[IPrimaryMemberFacePlaneIntersectionFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberFacePlaneIntersectionFeatureData_members.md)
