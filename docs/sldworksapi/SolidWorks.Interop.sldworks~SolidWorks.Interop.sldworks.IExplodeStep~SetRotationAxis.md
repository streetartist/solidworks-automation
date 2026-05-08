# SetRotationAxis Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~SetRotationAxis`

Sets the rotation axis (manipulator index and entity) for this regular explode step.
Sets the rotation axis (manipulator index and entity) for this regular explode step.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetRotationAxis( _
   ByVal RotationAxis As System.Object, _
   ByVal RotAxisIndex As System.Integer _
) 
```

```

Dim instance As IExplodeStep
Dim RotationAxis As System.Object
Dim RotAxisIndex As System.Integer
 
instance.SetRotationAxis(RotationAxis, RotAxisIndex)
```

```

void SetRotationAxis( 
   System.object RotationAxis,
   System.int RotAxisIndex
)
```

```

void SetRotationAxis( 
   System.Object^ RotationAxis,
   System.int RotAxisIndex
) 
```

#### Parameters

*RotationAxis*
:   Rotation axis entity

*RotAxisIndex*
:   Rotation manipulator index as defined in [swRotationAxisIndex\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swRotationAxisIndex_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IExplodeStep Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.md)  
[IExplodeStep Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep_members.md)  
[IExplodeStep::GetRotationAxis Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetRotationAxis.md)
