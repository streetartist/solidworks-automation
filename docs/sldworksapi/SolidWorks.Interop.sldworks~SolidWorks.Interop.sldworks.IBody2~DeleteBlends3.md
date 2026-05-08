# DeleteBlends3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DeleteBlends3`

Removes a set of fillet faces from a temporary body and heals the body.
Removes a set of fillet faces from a temporary body and heals the body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function DeleteBlends3( _
   ByVal FaceList As System.Object, _
   ByVal DoLocalCheck As System.Boolean, _
   ByVal UsePlanarCap As System.Boolean _
) As System.Boolean
```

```

Dim instance As IBody2
Dim FaceList As System.Object
Dim DoLocalCheck As System.Boolean
Dim UsePlanarCap As System.Boolean
Dim value As System.Boolean
 
value = instance.DeleteBlends3(FaceList, DoLocalCheck, UsePlanarCap)
```

```

System.bool DeleteBlends3( 
   System.object FaceList,
   System.bool DoLocalCheck,
   System.bool UsePlanarCap
)
```

```

System.bool DeleteBlends3( 
   System.Object^ FaceList,
   System.bool DoLocalCheck,
   System.bool UsePlanarCap
) 
```

#### Parameters

*FaceList*
:   List of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) to delete

*DoLocalCheck*
:   True to perform a local check, false to not

*UsePlanarCap*
:   True to use planar caps, false to not (see **Remarks**)

#### Return Value

True if the set of fillet faces are removed, false if not

Remarks

Typically when deleting blends, an entire chain of blends is deleted. However, if only a few blends are deleted from a chain of blends and the UsePlanarCap parameter is not set to true, then the resultant body might be invalid.

Example

[Delete Blended Faces (C#)](Delete_Blended_Faces_Example_CSharp.htm)  
[Delete Blended Faces (VB.NET)](Delete_Blended_Faces_Example_VBNET.htm)  
[Delete Blended Faces (VBA)](Delete_Blended_Faces_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::IDeleteBlends3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDeleteBlends3.md)  
[IBody5::DeleteFaces5 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DeleteFaces5.md)
