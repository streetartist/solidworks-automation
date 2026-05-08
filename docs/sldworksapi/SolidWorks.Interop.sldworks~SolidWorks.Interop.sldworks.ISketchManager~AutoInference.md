# AutoInference Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~AutoInference`

Obsolete. Superseded by ISldWorks::GetUserPreferenceToggle or ISldWorks::SetUserPreferenceToggle and swUserPreferenceToggle_e.swSketchInference.
Obsolete. Superseded by [ISldWorks::GetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserPreferenceToggle.md) or [ISldWorks::SetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceToggle.md) and [swUserPreferenceToggle\_e.swSketchInference.](ms-help://SolidWorks.Interop.swconst/SolidWorks/SO_SketchRelationsSnaps.htm)

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property AutoInference As System.Boolean
```

```

Dim instance As ISketchManager
Dim value As System.Boolean
 
instance.AutoInference = value
 
value = instance.AutoInference
```

```

System.bool AutoInference {get; set;}
```

```

property System.bool AutoInference {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if automatic inteferencing is on, false if off

Remarks

Inferencing mode can be seen when creating a sketch segment and your cursor moves past another sketch enitity. If inferencing is turned on, you see a dashed line from your current cursor position to the inferenced position on the existing sketch entity.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)  
[ISketchManager::InferenceMode Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~InferenceMode.md)
