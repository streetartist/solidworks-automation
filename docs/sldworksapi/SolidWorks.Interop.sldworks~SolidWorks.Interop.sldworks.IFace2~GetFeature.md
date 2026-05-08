# GetFeature Method (IFace2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetFeature`

Gets the feature that owns this face.
Gets the feature that owns this face.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFeature() As System.Object
```

```

Dim instance As IFace2
Dim value As System.Object
 
value = instance.GetFeature()
```

```

System.object GetFeature()
```

```

System.Object^ GetFeature(); 
```

#### Return Value

Owning [feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

In SOLIDWORKS, a face:

- is the result of evaluating a feature.
- can be owned by several features.

[IFeature::GetFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetFaces.md) or [IFeature::IGetFaces2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetFaces2.md) returns all of the faces owned by a feature. This is different from the faces highlighted in the user interface when the feature is selected. The user interface filters out multiple feature faces. This filter is only for display purposes.

To filter out multiple feature faces using the SOLIDWORKS API, you must call IFace2::GetFeature or [IFace2::IGetFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetFeature.md). Only the oldest feature from the face is returned, that is, the first owning feature in the FeatureManager design tree.

Example

[Get Part for Corresponding Component (VBA)](Get_Part_for_Corresponding_Component_Example_VB.htm)  
[Get Faces Associated with Feature (C#)](Get_Faces_Associated_with_Feature_Example_CSharp.htm)  
[Get Faces Associated with Feature (VB.NET)](Get_Faces_Associated_with_Feature_Example_VBNET.htm)  
[Get Faces Associated with Feature (VBA)](Get_Faces_Associated_with_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)  
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.md)  
[IFace2::GetFeatureId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetFeatureId.md)  
[IFace2::IGetFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetFeature.md)
