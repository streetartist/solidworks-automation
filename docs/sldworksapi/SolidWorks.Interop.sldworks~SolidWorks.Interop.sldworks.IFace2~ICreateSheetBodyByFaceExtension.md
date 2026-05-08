# ICreateSheetBodyByFaceExtension Method (IFace2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~ICreateSheetBodyByFaceExtension`

Creates a sheet body by extending the face.
Creates a sheet body by extending the face.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateSheetBodyByFaceExtension( _
   ByRef BoxLowIn As System.Double, _
   ByRef BoxHighIn As System.Double _
) As Body2
```

```

Dim instance As IFace2
Dim BoxLowIn As System.Double
Dim BoxHighIn As System.Double
Dim value As Body2
 
value = instance.ICreateSheetBodyByFaceExtension(BoxLowIn, BoxHighIn)
```

```

Body2 ICreateSheetBodyByFaceExtension( 
   ref System.double BoxLowIn,
   ref System.double BoxHighIn
)
```

```

Body2^ ICreateSheetBodyByFaceExtension( 
   System.double% BoxLowIn,
   System.double% BoxHighIn
) 
```

#### Parameters

*BoxLowIn*
:   Pointer to an array of 3 doubles (x,y,z)

*BoxHighIn*
:   Pointer to an array of 3 doubles (x,y,z)

#### Return Value

Pointer to the newly created sheet [body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)  
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.md)  
[IBody2::DeleteFacesMakeSheetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DeleteFacesMakeSheetBodies.md)  
[IBody2::IDeleteFacesMakeSheetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDeleteFacesMakeSheetBodies.md)  
[IBody2::IDeleteFacesMakeSheetBodiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDeleteFacesMakeSheetBodiesCount.md)  
[IFace2::CreateSheetBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~CreateSheetBody.md)  
[IFace2::CreateSheetBodyByFaceExtension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~CreateSheetBodyByFaceExtension.md)  
[IFace2::ICreateSheetBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~ICreateSheetBody.md)  
[IModeler::CreateBodiesFromSheets2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodiesFromSheets2.md)  
[IModeler::ICreateBodiesFromSheets2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodiesFromSheets2.md)
