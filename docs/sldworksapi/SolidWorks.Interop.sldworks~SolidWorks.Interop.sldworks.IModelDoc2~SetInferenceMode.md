# SetInferenceMode Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetInferenceMode`

Obsolete. Superseded by SketchManager::InferenceMode.
Obsolete. Superseded by [SketchManager::InferenceMode](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~InferenceMode.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetInferenceMode( _
   ByVal InferenceMode As System.Boolean _
) 
```

```

Dim instance As IModelDoc2
Dim InferenceMode As System.Boolean
 
instance.SetInferenceMode(InferenceMode)
```

```

void SetInferenceMode( 
   System.bool InferenceMode
)
```

```

void SetInferenceMode( 
   System.bool InferenceMode
) 
```

#### Parameters

*InferenceMode*
:   True to enable sketch inference mode, false to disable it

Remarks

|  |  |
| --- | --- |
| **Setting inference mode to...** | **Allows...** |
| True | Inferencing during sketch operations, subject to other settings that may disable inferencing such as [IModelDoc2::AutoInferToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AutoInferToggle.md), [IModelDoc2::SetAddToDB](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetAddToDB.md), and [IDrawingDoc::StartDrawing](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~StartDrawing.md). |
| false | Faster sketching without inferencing, similar to [IModelDoc2::SetAddToDB](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetAddToDB.md), except that using this method does not disable undo operations. |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::GetInferenceMode Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetInferenceMode.md)
