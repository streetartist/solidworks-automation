# ReverseEndPointTangent Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~ReverseEndPointTangent`

Reverses the end point tangent direction of splines and arcs.
Reverses the end point tangent direction of splines and arcs.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ReverseEndPointTangent( _
   ByVal ForceDeleteConstraints As System.Boolean _
) As System.Integer
```

```

Dim instance As ISketchManager
Dim ForceDeleteConstraints As System.Boolean
Dim value As System.Integer
 
value = instance.ReverseEndPointTangent(ForceDeleteConstraints)
```

```

System.int ReverseEndPointTangent( 
   System.bool ForceDeleteConstraints
)
```

```

System.int ReverseEndPointTangent( 
   System.bool ForceDeleteConstraints
) 
```

#### Parameters

*ForceDeleteConstraints*
:   True to force the deletion of constraints, false to not

#### Return Value

Result code as defined in [swReverseEndPointTangentResult\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swReverseEndPointTangentResult_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)
