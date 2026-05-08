# CreateSheetBodyByFaceExtension Method (IFace2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~CreateSheetBodyByFaceExtension`

Creates a sheet body by extending the face.
Creates a sheet body by extending the face.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateSheetBodyByFaceExtension( _
   ByVal BoxLowIn As System.Object, _
   ByVal BoxHighIn As System.Object _
) As System.Object
```

```

Dim instance As IFace2
Dim BoxLowIn As System.Object
Dim BoxHighIn As System.Object
Dim value As System.Object
 
value = instance.CreateSheetBodyByFaceExtension(BoxLowIn, BoxHighIn)
```

```

System.object CreateSheetBodyByFaceExtension( 
   System.object BoxLowIn,
   System.object BoxHighIn
)
```

```

System.Object^ CreateSheetBodyByFaceExtension( 
   System.Object^ BoxLowIn,
   System.Object^ BoxHighIn
) 
```

#### Parameters

*BoxLowIn*
:   Array of 3 doubles (x,y,z)

*BoxHighIn*
:   Array of 3 doubles (x,y,z)

#### Return Value

Newly created sheet body

Remarks

A sheet body is a surface body.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)  
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.md)  
[IFace2::ICreateSheetBodyByFaceExtension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~ICreateSheetBodyByFaceExtension.md)  
[IFace2::ICreateSheetBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~ICreateSheetBody.md)  
[IFace2::CreateSheetBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~CreateSheetBody.md)  
[IBody2::DeleteFacesMakeSheetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DeleteFacesMakeSheetBodies.md)  
[IBody2::IDeleteFacesMakeSheetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDeleteFacesMakeSheetBodies.md)  
[IModeler::CreateSheetFromFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSheetFromFaces.md)  
[IModeler::ICreateSheetFromFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateSheetFromFaces.md)  
[IBody2::IDeleteFacesMakeSheetBodiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDeleteFacesMakeSheetBodiesCount.md)
