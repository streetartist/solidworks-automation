# IDeleteFacesMakeSheetBodies Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDeleteFacesMakeSheetBodies`

Creates sheet bodies from deleted faces.
Creates sheet bodies from deleted faces.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IDeleteFacesMakeSheetBodies( _
   ByVal FaceCount As System.Integer, _
   ByRef FaceList As Face2, _
   ByVal SheetCount As System.Integer _
) As Body2
```

```

Dim instance As IBody2
Dim FaceCount As System.Integer
Dim FaceList As Face2
Dim SheetCount As System.Integer
Dim value As Body2
 
value = instance.IDeleteFacesMakeSheetBodies(FaceCount, FaceList, SheetCount)
```

```

Body2 IDeleteFacesMakeSheetBodies( 
   System.int FaceCount,
   ref Face2 FaceList,
   System.int SheetCount
)
```

```

Body2^ IDeleteFacesMakeSheetBodies( 
   System.int FaceCount,
   Face2^% FaceList,
   System.int SheetCount
) 
```

#### Parameters

*FaceCount*
:   Number of faces to delete

*FaceList*
:   - in-process, unmanaged C++: Pointer to an array of the [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

*SheetCount*
:   Number of sheets bodies to create

#### Return Value

- in-process, unmanaged C++: Pointer to an array of sheet [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) created from the deleted faces
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [IBody2:IDeleteFacesMakeSheetBodiesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDeleteFacesMakeSheetBodiesCount.md) to get the number of sheet bodies to create from the deleted faces.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::DeleteFacesMakeSheetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DeleteFacesMakeSheetBodies.md)  
[IFace2::ICreateSheetBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~ICreateSheetBody.md)  
[IFace2::ICreateSheetBodyByFaceExtension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~ICreateSheetBodyByFaceExtension.md)  
[IModeler::ICreateSheetFromFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateSheetFromFaces.md)  
[IModeler::ICreateSheetFromSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateSheetFromSurface2.md)
