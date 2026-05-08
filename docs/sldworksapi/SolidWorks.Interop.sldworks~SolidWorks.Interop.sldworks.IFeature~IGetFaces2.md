# IGetFaces2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetFaces2`

Gets the faces in this feature.
Gets the faces in this feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetFaces2( _
   ByRef FaceCount As System.Integer _
) As Face2
```

```

Dim instance As IFeature
Dim FaceCount As System.Integer
Dim value As Face2
 
value = instance.IGetFaces2(FaceCount)
```

```

Face2 IGetFaces2( 
   out System.int FaceCount
)
```

```

Face2^ IGetFaces2( 
   [Out] System.int FaceCount
) 
```

#### Parameters

*FaceCount*
:   Number of faces in this feature

#### Return Value

- in-process, unmanaged C++: Pointer to an array of pointers to the [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

To determine the size of the array, call [IFeature::GetFaceCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetFaceCount.md) before calling this method.

IFeature::IGetFaces2 compares the number of faces in this feature with FaceCount. If the actual number of faces is larger than the specified FaceCount, then this method returns no faces and a status of S\_ERROR. If the actual number of faces is smaller than the specified in FaceCount, then this method returns all of the faces in the return array, and changes FaceCount to reflect the correct number of faces.

In SOLIDWORKS, a face:

- is the result of evaluating a feature.
- can be owned by several features.

IFeature::IGetFaces2 returns all of the faces owned by a feature. This is different from the faces highlighted in the user interface when the feature is selected. The user interface filters out multiple feature faces. This filter is only for display purposes.

NOTES:

- This method does not return any faces for draft features because draft features do not create any new faces. Drafting only modifies existing faces.
- The number of faces for rolled hems is 0 because all of the faces belong to the children bends.

To filter out multiple feature faces using the SOLIDWORKS API, you must call [IFace2::IGetFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetFeature.md). Only the oldest feature from the face is returned, that is, the first owning feature in the FeatureManager design tree.

**Example**

HRESULT    hr = S\_OK;

long       lNumFaces = 0;

 

hr = feat->GetFaceCount(&lNumFaces);

 

LPFACE2\*   aFaces = new LPFACE2[lNumFaces];

hr = feat->IGetFaces2(&lNumFaces, aFaces);

...

delete [] aFaces;

aFaces = 0;

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)  
[IFeature::GetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetFaces.md)
