# Deactivate Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D~Deactivate`

Restores the previously backed-up model state of a 3D View.
Restores the previously backed-up model state of a 3D View.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Deactivate() 
```

```

Dim instance As IView3D
 
instance.Deactivate()
```

```

void Deactivate()
```

```

void Deactivate(); 
```

Remarks

The model state includes the model's:

- active configuration
- display state
- explode, section, or Model Break view state
- view orientation, including pan and zoom

Restoring the previously backed-up model state of a 3D View might not be this 3D View.

For example:

1. Call [IView3D::Activate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D~Activate.md) and set the SaveLastState parameter to true (i.e., previous model state backed up) for 3DView1.
2. Call IView3D::Activate and set the SaveLastState parameter to false (i.e., previous model state not backed up) for 3DView2.
3. Call IView3D::Deactivate for 3DView1 or 3DView2, then the model state prior to activating 3DView1 is restored.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView3D Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D.md)  
[IView3D Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D_members.md)
