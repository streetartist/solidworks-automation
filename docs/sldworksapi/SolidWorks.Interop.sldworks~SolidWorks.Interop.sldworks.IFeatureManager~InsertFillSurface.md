# InsertFillSurface Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertFillSurface`

Obsolete. Superseded by IFeatureManager::InsertFillSurface2.
Obsolete. Superseded by [IFeatureManager::InsertFillSurface2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertFillSurface2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertFillSurface( _
   ByVal Resolution As System.Integer _
) As Feature
```

```

Dim instance As IFeatureManager
Dim Resolution As System.Integer
Dim value As Feature
 
value = instance.InsertFillSurface(Resolution)
```

```

Feature InsertFillSurface( 
   System.int Resolution
)
```

```

Feature^ InsertFillSurface( 
   System.int Resolution
) 
```

#### Parameters

*Resolution*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)
