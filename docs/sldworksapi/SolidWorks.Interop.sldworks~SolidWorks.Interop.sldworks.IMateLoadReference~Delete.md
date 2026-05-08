# Delete Method (IMateLoadReference)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateLoadReference~Delete`

Deletes this mate load reference.
Deletes this mate load reference.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Delete() As System.Boolean
```

```

Dim instance As IMateLoadReference
Dim value As System.Boolean
 
value = instance.Delete()
```

```

System.bool Delete()
```

```

System.bool Delete(); 
```

#### Return Value

True if the mate load reference is deleted, false if not

Remarks

This method rebuilds the FeatureManager design tree, which can be a time-consuming operation if it is large. If using this method to delete many load references at once, use [IFeatureManager::EnableFeatureTree](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~EnableFeatureTree.md) before and after using IAssemblyDoc::InsertLoadReference to disable and then re-enable rebuilding the FeatureManager design tree.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMateLoadReference Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateLoadReference.md)  
[IMateLoadReference Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateLoadReference_members.md)
