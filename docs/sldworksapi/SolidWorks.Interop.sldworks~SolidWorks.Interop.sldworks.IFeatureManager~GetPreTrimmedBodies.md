# GetPreTrimmedBodies Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~GetPreTrimmedBodies`

Gets the temporary trimmed bodies using the specified target sheet (surface) body according to the trim tools previously defined by IFeatureManager::PreTrimSurface.
Gets the temporary trimmed bodies using the specified target sheet (surface) body according to the trim tools previously defined by [IFeatureManager::PreTrimSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PreTrimSurface.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetPreTrimmedBodies( _
   ByVal TargetSurface As Body2 _
) As System.Object
```

```

Dim instance As IFeatureManager
Dim TargetSurface As Body2
Dim value As System.Object
 
value = instance.GetPreTrimmedBodies(TargetSurface)
```

```

System.object GetPreTrimmedBodies( 
   Body2 TargetSurface
)
```

```

System.Object^ GetPreTrimmedBodies( 
   Body2^ TargetSurface
) 
```

#### Parameters

*TargetSurface*
:   Target sheet [body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

#### Return Value

Array of temporary trimmed bodies

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IFeatureManager::PostTrimSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PostTrimSurface.md)
