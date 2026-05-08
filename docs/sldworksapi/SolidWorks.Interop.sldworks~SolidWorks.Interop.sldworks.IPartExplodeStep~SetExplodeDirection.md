# SetExplodeDirection Method (IPartExplodeStep)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep~SetExplodeDirection`

Sets the explode direction (manipulator index and entity) for this explode step.
Sets the explode direction (manipulator index and entity) for this explode step.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetExplodeDirection( _
   ByVal ExplodeDirection As System.Object, _
   ByVal ExplDirIndex As System.Integer _
) 
```

```

Dim instance As IPartExplodeStep
Dim ExplodeDirection As System.Object
Dim ExplDirIndex As System.Integer
 
instance.SetExplodeDirection(ExplodeDirection, ExplDirIndex)
```

```

void SetExplodeDirection( 
   System.object ExplodeDirection,
   System.int ExplDirIndex
)
```

```

void SetExplodeDirection( 
   System.Object^ ExplodeDirection,
   System.int ExplDirIndex
) 
```

#### Parameters

*ExplodeDirection*
:   Explode direction entity (e.g., [IEdge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md), [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md), [IRefAxis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.md))

*ExplDirIndex*
:   Explode direction manipulator index as defined in [swExplodeDirectionIndex\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swExplodeDirectionIndex_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartExplodeStep Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep.md)  
[IPartExplodeStep Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep_members.md)  
[IPartExplodeStep::GetExplodeDirection Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep~GetExplodeDirection.md)
