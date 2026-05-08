# SetDynamicMirror Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SetDynamicMirror`

Enables or disables dynamic sketch mirroring, which is the automatic mirroring of newly created sketch entities about a selected centerline.
Enables or disables dynamic sketch mirroring, which is the automatic mirroring of newly created sketch entities about a selected centerline.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetDynamicMirror( _
   ByVal DynamicMirror As System.Boolean _
) As System.Boolean
```

```

Dim instance As ISketchManager
Dim DynamicMirror As System.Boolean
Dim value As System.Boolean
 
value = instance.SetDynamicMirror(DynamicMirror)
```

```

System.bool SetDynamicMirror( 
   System.bool DynamicMirror
)
```

```

System.bool SetDynamicMirror( 
   System.bool DynamicMirror
) 
```

#### Parameters

*DynamicMirror*
:   True to enable dynamic sketch mirroring, false to disable it

#### Return Value

True if setting this option to succeeds, false if fails

Remarks

If enabling dynamic sketch mirroring, then:

- a sketch must be in edit mode.
- a line segment or linear edge of a model must be selected before calling this method.

Example

[Dynamically Mirror Sketch Entities (VBA)](Dynamically_Mirror_Sketch_Entities_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)  
[ISketchManager::GetDynamicMirror Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~GetDynamicMirror.md)
