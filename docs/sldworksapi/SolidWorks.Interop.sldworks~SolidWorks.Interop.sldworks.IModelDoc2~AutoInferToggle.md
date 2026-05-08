# AutoInferToggle Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AutoInferToggle`

Obsolete. Superseded by ISketchManager::AutoInference.
Obsolete. Superseded by [ISketchManager::AutoInference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~AutoInference.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub AutoInferToggle() 
```

```

Dim instance As IModelDoc2
 
instance.AutoInferToggle()
```

```

void AutoInferToggle()
```

```

void AutoInferToggle(); 
```

Remarks

Inferencing mode can be seen when creating a sketch segment and you mouse moves past another sketch item. If inferencing is turned on, you see a dashed line from the current cursor position to the inferenced position on the existing sketch entity.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::SetInferenceMode Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetInferenceMode.md)  
[IModelDoc2::GetInferenceMode Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetInferenceMode.md)
