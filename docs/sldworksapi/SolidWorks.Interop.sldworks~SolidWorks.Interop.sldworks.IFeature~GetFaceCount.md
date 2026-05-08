# GetFaceCount Method (IFeature)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetFaceCount`

Gets the number of faces in this feature.
Gets the number of faces in this feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFaceCount() As System.Integer
```

```

Dim instance As IFeature
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

Number of faces in this feature

Remarks

Call this method before calling [IFeature::IGetFaces2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetFaces2.md).

A face:

- is the result of evaluating a feature.
- can be owned by several features.

This method returns all of the faces owned by a feature. This is different from the faces highlighted in the user interface when the feature is selected. The user interface filters out multiple feature faces. This filter is only for display purposes.

NOTES:  

- This method does not return any faces for draft features because draft features do not create any new faces. Drafting only modifies existing faces.
- The number of faces for rolled hems is 0 because all of the faces belong to the children bends.

To filter out multiple feature faces, call [IFace2::GetFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetFeature.md) or [IFace2::IGetFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetFeature.md). Only the oldest feature from the face is returned; that is, the first owning feature in the FeatureManager design tree.

Example

[Get Faces Affected by Draft Feature (VBA)](Get_Faces_Affected_by_Draft_Feature_Example_VB.htm)  
[Get Faces Affected by Scale Feature (VBA)](Get_Faces_Affected_by_Scale_Feature_Example_VB.htm)  
[Get Faces Associated with Feature (C#)](Get_Faces_Associated_with_Feature_Example_CSharp.htm)  
[Get Faces Associated with Feature (VB.NET)](Get_Faces_Associated_with_Feature_Example_VBNET.htm)  
[Get Faces Associated with Feature (VBA)](Get_Faces_Associated_with_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)  
[IFace2::GetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetFaces.md)
