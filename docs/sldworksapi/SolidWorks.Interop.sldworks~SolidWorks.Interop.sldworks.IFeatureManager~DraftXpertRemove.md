# DraftXpertRemove Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~DraftXpertRemove`

Deletes the draft on the selected faces. If all the faces of a draft are selected, then this method deletes the draft feature; if not, then this method edits the draft feature and removes the selected face references from it.
Deletes the draft on the selected faces. If all the faces of a draft are selected, then this method deletes the draft feature; if not, then this method edits the draft feature and removes the selected face references from it.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function DraftXpertRemove() As Feature
```

```

Dim instance As IFeatureManager
Dim value As Feature
 
value = instance.DraftXpertRemove()
```

```

Feature DraftXpertRemove()
```

```

Feature^ DraftXpertRemove(); 
```

#### Return Value

Pointer to the [feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IFeatureManager::DraftXpertChange Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~DraftXpertChange.md)
