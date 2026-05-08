# IsRolledBack Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IsRolledBack`

Gets whether this feature is rolled back.
Gets whether this feature is rolled back.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsRolledBack() As System.Boolean
```

```

Dim instance As IFeature
Dim value As System.Boolean
 
value = instance.IsRolledBack()
```

```

System.bool IsRolledBack()
```

```

System.bool IsRolledBack(); 
```

#### Return Value

True if the feature is rolled back, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)  
[IFeatureManager::EditRollback Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~EditRollback.md)
