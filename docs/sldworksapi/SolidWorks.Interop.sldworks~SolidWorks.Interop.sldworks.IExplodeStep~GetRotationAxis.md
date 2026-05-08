# GetRotationAxis Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetRotationAxis`

Gets the rotation axis (manipulator index and entity) for this regular explode step.
Gets the rotation axis (manipulator index and entity) for this regular explode step.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetRotationAxis( _
   ByRef RotAxisIndex As System.Integer _
) As System.Object
```

```

Dim instance As IExplodeStep
Dim RotAxisIndex As System.Integer
Dim value As System.Object
 
value = instance.GetRotationAxis(RotAxisIndex)
```

```

System.object GetRotationAxis( 
   out System.int RotAxisIndex
)
```

```

System.Object^ GetRotationAxis( 
   [Out] System.int RotAxisIndex
) 
```

#### Parameters

*RotAxisIndex*
:   Rotation manipulator index as defined in [swRotationAxisIndex\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swRotationAxisIndex_e.html)

#### Return Value

Rotation axis entity; Nothing or null if a rotation axis entity was not selected during creation of this explode step

Remarks

This method is not valid for subassembly explode steps.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IExplodeStep Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.md)  
[IExplodeStep Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep_members.md)  
[IExplodeStep::SetRotationAxis Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~SetRotationAxis.md)
