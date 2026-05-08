# InferenceMode Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~InferenceMode`

Obsolete. Superseded by ISldWorks::GetUserPreferenceToggle or ISldWorks::SetUserPreferenceToggle and swUserPreferenceToggle_e.swSketchInference.
Obsolete. Superseded by [ISldWorks::GetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserPreferenceToggle.md) or [ISldWorks::SetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceToggle.md) and [swUserPreferenceToggle\_e.swSketchInference.](ms-help://SolidWorks.Interop.swconst/SolidWorks/SO_SketchRelationsSnaps.htm)

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property InferenceMode As System.Boolean
```

```

Dim instance As ISketchManager
Dim value As System.Boolean
 
instance.InferenceMode = value
 
value = instance.InferenceMode
```

```

System.bool InferenceMode {get; set;}
```

```

property System.bool InferenceMode {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if sketch inference mode is on, false if off

Remarks

This property affects sketch entity snapping and inferring constraints to other geometry during creation.

|  |  |
| --- | --- |
| **Setting inference mode to...** | **Allows...** |
| True | Inferencing during sketch operations, subject to other settings that may disable inferencing such as [ISketchManager::AutoInference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~AutoInference.md), [ISketchManager::AddToDB](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~AddToDB.md), and [IDrawingDoc::StartDrawing](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~StartDrawing.md). |
| False | Faster sketching without inferencing, similar to SketchManager::AddToDB, except that using this method does not disable undo operations. |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)
