# InsertMirrorAll Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~InsertMirrorAll`

Mirrors the part about a selected planar face.
Mirrors the part about a selected planar face.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertMirrorAll() As System.Boolean
```

```

Dim instance As IPartDoc
Dim value As System.Boolean
 
value = instance.InsertMirrorAll()
```

```

System.bool InsertMirrorAll()
```

```

System.bool InsertMirrorAll(); 
```

#### Return Value

True if the feature is successfully created, false if not

Remarks

This method returns a True or false to indicate whether or not the mirror-all feature was created. If it is successful, the newly created feature remains selected after the method runs. You can use [ISelectionMgr::GetSelectedObject6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject6.md) to retrieve this object.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)  
[IPartDoc::MirrorPart Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~MirrorPart.md)  
[IFeatureManager::InsertMirrorFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMirrorFeature.md)  
[IPartDoc::MirrorFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~MirrorFeature.md)
