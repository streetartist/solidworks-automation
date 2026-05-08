# GetInferenceMode Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetInferenceMode`

Obsolete. Superseded by SketchManager::InferenceMode.
Obsolete. Superseded by [SketchManager::InferenceMode](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~InferenceMode.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetInferenceMode() As System.Boolean
```

```

Dim instance As IModelDoc2
Dim value As System.Boolean
 
value = instance.GetInferenceMode()
```

```

System.bool GetInferenceMode()
```

```

System.bool GetInferenceMode(); 
```

Remarks

This method affects sketch-entity snapping or inferring constraints to other geometry during creation.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::AutoInferToggle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AutoInferToggle.md)  
[IModelDoc2::SetInferenceMode Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetInferenceMode.md)
