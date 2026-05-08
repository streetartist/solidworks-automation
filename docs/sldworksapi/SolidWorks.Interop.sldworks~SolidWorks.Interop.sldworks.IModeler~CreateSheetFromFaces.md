# CreateSheetFromFaces Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSheetFromFaces`

Creates a sheet (surface) body from connected faces.
Creates a sheet (surface) body from connected faces.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateSheetFromFaces( _
   ByVal FaceArr As System.Object _
) As Body2
```

```

Dim instance As IModeler
Dim FaceArr As System.Object
Dim value As Body2
 
value = instance.CreateSheetFromFaces(FaceArr)
```

```

Body2 CreateSheetFromFaces( 
   System.object FaceArr
)
```

```

Body2^ CreateSheetFromFaces( 
   System.Object^ FaceArr
) 
```

#### Parameters

*FaceArr*
:   Array of connected [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

#### Return Value

Newly created [body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

Example

[Create Sheet Body From Faces and Feature From Sheet Body (VBA)](Create_Sheet_Body_From_Faces_and_Feature_from_Sheet_Body_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)  
[IModeler::CreateSheetFromSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSheetFromSurface.md)  
[IModeler::ICreateSheetFromFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateSheetFromFaces.md)  
[IModeler::ICreateSheetFromSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateSheetFromSurface2.md)  
[IFace2::CreateSheetBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~CreateSheetBody.md)  
[IFace2::CreateSheetBodyByFaceExtension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~CreateSheetBodyByFaceExtension.md)  
[IFace2::ICreateSheetBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~ICreateSheetBody.md)  
[IFace2::ICreateSheetBodyByFaceExtension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~ICreateSheetBodyByFaceExtension.md)
