# GetFaces Method (IFeature)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetFaces`

Gets the faces in this feature.
Gets the faces in this feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFaces() As System.Object
```

```

Dim instance As IFeature
Dim value As System.Object
 
value = instance.GetFaces()
```

```

System.object GetFaces()
```

```

System.Object^ GetFaces(); 
```

#### Return Value

Array of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

Remarks

A face:

- is the result of evaluating a feature.
- can be owned by several features.

This method returns all of the faces owned by a feature. This is different from the faces highlighted in the user interface when the feature is selected. The user interface filters out multiple feature faces. This filter is only for display purposes.

NOTES:  

- This method does not return any faces for draft features because draft features do not create any new faces. Drafting only modifies existing faces.
- The number of faces for rolled hems is 0 because all of the faces belong to the children bends.

To filter out multiple feature faces, call [IFace2::GetFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetFeature.md) or [IFace2::IGetFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetFeature.md). Only the oldest feature from the face is returned; that is, the first owning feature in the FeatureManager design tree.

Example

[Get Faces Associated with Feature (VBA)](Get_Faces_Associated_with_Feature_Example_VB.htm)  
[Get Part for Corresponding Component (VBA)](Get_Part_for_Corresponding_Component_Example_VB.htm)  
[Add Attribute to Feature and Include in Library Feature (VB.NET)](Add_Attribute_to_Feature_and_Include_in_Library_Feature_Example_VBNET.htm)  
[Add Attribute to Feature and Include in Library Feature (C#)](Add_Attribute_to_Feature_and_Include_in_Library_Feature_Example_CSharp.htm)  
[Add Attribute to Feature and Include in Library Feature (VBA)](Add_Attribute_to_Feature_and_Include_In_Library_Feature_Example_VB.htm)  
[Roll Back Model (C#)](Roll_Back_Model_Example_CSharp.htm)  
[Roll Back Model (VB.NET)](Roll_Back_Model_Example_VBNET.htm)  
[Roll Back Model (VBA)](Roll_Back_Model_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)  
[IFeature::IGetFaces2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetFaces2.md)  
[IFeature::GetFaceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetFaceCount.md)
