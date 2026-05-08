# GetAffectedFaces Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetAffectedFaces`

Gets the faces modified by a feature, such as a draft feature.
Gets the faces modified by a feature, such as a draft feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetAffectedFaces() As System.Object
```

```

Dim instance As IFeature
Dim value As System.Object
 
value = instance.GetAffectedFaces()
```

```

System.object GetAffectedFaces()
```

```

System.Object^ GetAffectedFaces(); 
```

#### Return Value

Array of the [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) modified by a feature

Example

[Get Faces Affected By Feature (VBA)](Get_Faces_Affected_by_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)  
[IFeature::GetAffectedFaceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetAffectedFaceCount.md)  
[IFeature::IGetAffectedFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetAffectedFaces.md)
