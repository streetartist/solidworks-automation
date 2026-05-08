# InsertSaveOutBodies Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSaveOutBodies`

Saves the selected surface bodies or solid bodies or sub-weldments to a file.
Saves the selected surface bodies or solid bodies or sub-weldments to a file.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertSaveOutBodies() As System.Boolean
```

```

Dim instance As IFeatureManager
Dim value As System.Boolean
 
value = instance.InsertSaveOutBodies()
```

```

System.bool InsertSaveOutBodies()
```

```

System.bool InsertSaveOutBodies(); 
```

#### Return Value

True if the selected surface bodies or solid bodies or sub-weldments are saved to a file, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)
