# Activate Method (IView3D)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D~Activate`

Activates this 3D View.
Activates this 3D View.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Activate( _
   ByVal SaveLastState As System.Boolean _
) 
```

```

Dim instance As IView3D
Dim SaveLastState As System.Boolean
 
instance.Activate(SaveLastState)
```

```

void Activate( 
   System.bool SaveLastState
)
```

```

void Activate( 
   System.bool SaveLastState
) 
```

#### Parameters

*SaveLastState*
:   True to back up the previous model state prior to activating this 3D View, false to not back up the previous model state prior to activating this 3D view

Remarks

The model state includes the model's:

- active configuration
- display state
- explode, section, or Model Break view state
- view orientation, including pan and zoom

Example

See the [IView3D](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView3D Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D.md)  
[IView3D Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D_members.md)  
[IView3D::Deactivate Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D~Deactivate.md)
