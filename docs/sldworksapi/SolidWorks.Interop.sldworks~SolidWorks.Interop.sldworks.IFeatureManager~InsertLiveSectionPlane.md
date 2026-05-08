# InsertLiveSectionPlane Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertLiveSectionPlane`

Inserts a Live Section Plane using the selected plane or planar face.
Inserts a Live Section Plane using the selected plane or planar face.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertLiveSectionPlane( _
   ByVal Type As System.Short _
) As Feature
```

```

Dim instance As IFeatureManager
Dim Type As System.Short
Dim value As Feature
 
value = instance.InsertLiveSectionPlane(Type)
```

```

Feature InsertLiveSectionPlane( 
   System.short Type
)
```

```

Feature^ InsertLiveSectionPlane( 
   System.short Type
) 
```

#### Parameters

*Type*
:   Not used. Specify any integer value.

#### Return Value

[Feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IFeatureManager::MoveRotateLiveSectionPlane Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~MoveRotateLiveSectionPlane.md)
