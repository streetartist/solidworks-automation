# GetAffectedFaceCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetAffectedFaceCount`

Gets the number of faces modified by a feature, such as a draft feature.
Gets the number of faces modified by a feature, such as a draft feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetAffectedFaceCount() As System.Integer
```

```

Dim instance As IFeature
Dim value As System.Integer
 
value = instance.GetAffectedFaceCount()
```

```

System.int GetAffectedFaceCount()
```

```

System.int GetAffectedFaceCount(); 
```

#### Return Value

Number of faces modified by a feature

Remarks

Call this method before calling [IFeature::IGetAffectedFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetAffectedFaces.md).

Example

[Get Faces Affected By Feature (VBA)](Get_Faces_Affected_by_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)  
[IFace2::GetAffectedFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetAffectedFaces.md)
