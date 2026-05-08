# GetDeletedFacesCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteFaceFeatureData~GetDeletedFacesCount`

Gets the number of faces in the DeleteFace feature.
Gets the number of faces in the DeleteFace feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDeletedFacesCount() As System.Integer
```

```

Dim instance As IDeleteFaceFeatureData
Dim value As System.Integer
 
value = instance.GetDeletedFacesCount()
```

```

System.int GetDeletedFacesCount()
```

```

System.int GetDeletedFacesCount(); 
```

#### Return Value

Number of faces

Remarks

Call this method before calling [IDeleteFaceFeatureData::IGetDeletedFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteFaceFeatureData~IGetDeletedFaces.md) to determine the size of its array.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Example

[Insert and Change DeleteFace Features (C#)](Insert_and_Change_DeleteFace_Feature_Example_CSharp.htm)  
[Insert and Change DeleteFace Features (VB.NET)](Insert_and_Change_DeleteFace_Feature_Example_VBNET.htm)  
[Insert and Change DeleteFace Feature (VBA)](Insert_and_Change_DeleteFace_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDeleteFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteFaceFeatureData.md)  
[IDeleteFaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteFaceFeatureData_members.md)  
[IDeleteFaceFeatureData::GetDeletedFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteFaceFeatureData~GetDeletedFaces.md)  
[IDeleteFaceFeatureData::IGetDeletedFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteFaceFeatureData~IGetDeletedFaces.md)  
[IDeleteFaceFeatureData::ISetDeletedFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteFaceFeatureData~ISetDeletedFaces.md)  
[IDeleteFaceFeatureData::SetDeletedFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteFaceFeatureData~SetDeletedFaces.md)
