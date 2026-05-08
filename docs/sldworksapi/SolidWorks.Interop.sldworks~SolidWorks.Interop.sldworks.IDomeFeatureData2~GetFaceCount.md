# GetFaceCount Method (IDomeFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2~GetFaceCount`

Gets the number of planar and non-planar faces of this dome feature.
Gets the number of planar and non-planar faces of this dome feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFaceCount() As System.Integer
```

```

Dim instance As IDomeFeatureData2
Dim value As System.Integer
 
value = instance.GetFaceCount()
```

```

System.int GetFaceCount()
```

```

System.int GetFaceCount(); 
```

#### Return Value

Number of planar and non-planar faces

Remarks

Call this method before calling [IDomeFeatureData2::IGetFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2~IGetFaces.md).

Example

[Create and Modify Dome Feature (C#)](Create_and_Modify_Dome_Feature_Example_CSharp.htm)  
[Create and Modify Dome Feature (VB.NET)](Create_and_Modify_Dome_Feature_Example_VBNET.htm)  
[Create and Modify Dome Feature (VBA)](Create_and_Modify_Dome_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDomeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2.md)  
[IDomeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2_members.md)  
[IDomeFeatureData2::ISetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2~ISetFaces.md)  
[IDomeFeatureData2::Faces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2~Faces.md)
