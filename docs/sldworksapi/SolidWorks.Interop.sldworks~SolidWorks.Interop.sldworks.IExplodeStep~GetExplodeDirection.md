# GetExplodeDirection Method (IExplodeStep)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetExplodeDirection`

Gets the explode direction (manipulator index and entity) for this explode step.
Gets the explode direction (manipulator index and entity) for this explode step.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetExplodeDirection( _
   ByRef ExplDirIndex As System.Integer _
) As System.Object
```

```

Dim instance As IExplodeStep
Dim ExplDirIndex As System.Integer
Dim value As System.Object
 
value = instance.GetExplodeDirection(ExplDirIndex)
```

```

System.object GetExplodeDirection( 
   out System.int ExplDirIndex
)
```

```

System.Object^ GetExplodeDirection( 
   [Out] System.int ExplDirIndex
) 
```

#### Parameters

*ExplDirIndex*
:   Explode direction manipulator index as defined in [swExplodeDirectionIndex\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swExplodeDirectionIndex_e.html); valid only for regular explode steps

#### Return Value

Explode direction entity; Nothing or null if an explode direction entity was not selected during creation of this explode step

Remarks

This method is not valid for subassembly explode steps.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IExplodeStep Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.md)  
[IExplodeStep Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep_members.md)  
[IExplodeStep::SetExplodeDirection Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~SetExplodeDirection.md)
