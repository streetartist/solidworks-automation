# IDeleteFacesFromSheetBody Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IDeleteFacesFromSheetBody`

Deletes the unused faces of the sheet body.
Deletes the unused faces of the sheet body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IDeleteFacesFromSheetBody( _
   ByVal Count As System.Integer, _
   ByRef FaceVar As Face2 _
) As System.Boolean
```

```

Dim instance As IModeler
Dim Count As System.Integer
Dim FaceVar As Face2
Dim value As System.Boolean
 
value = instance.IDeleteFacesFromSheetBody(Count, FaceVar)
```

```

System.bool IDeleteFacesFromSheetBody( 
   System.int Count,
   ref Face2 FaceVar
)
```

```

System.bool IDeleteFacesFromSheetBody( 
   System.int Count,
   Face2^% FaceVar
) 
```

#### Parameters

*Count*
:   Number of faces to delete

*FaceVar*
:   Array of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) to delete from the sheet (surface) body

#### Return Value

True if all of the faces are deleted, false if not

Remarks

Use this method to remove the unused faces from the sheet body created by [IModeler::CreateBrepBody3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBrepBody3.md) and [IModeler::ICreateBrepBody3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBrepBody3.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)  
[IModeler::DeleteFacesFromSheetBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~DeleteFacesFromSheetBody.md)
