# DeleteFacesFromSheetBody Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~DeleteFacesFromSheetBody`

Deletes the unused faces of the sheet body.
Deletes the unused faces of the sheet body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function DeleteFacesFromSheetBody( _
   ByVal FaceVar As System.Object _
) As System.Boolean
```

```

Dim instance As IModeler
Dim FaceVar As System.Object
Dim value As System.Boolean
 
value = instance.DeleteFacesFromSheetBody(FaceVar)
```

```

System.bool DeleteFacesFromSheetBody( 
   System.object FaceVar
)
```

```

System.bool DeleteFacesFromSheetBody( 
   System.Object^ FaceVar
) 
```

#### Parameters

*FaceVar*
:   Array of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) to delete from the sheet (surface) body

Remarks

Use this method to remove the unused faces from the sheet body created by [IModeler::CreateBrepBody3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBrepBody3.md) and [IModeler::ICreateBrepBody3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBrepBody3.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)  
[IModeler::IDeleteFacesFromSheetBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IDeleteFacesFromSheetBody.md)
