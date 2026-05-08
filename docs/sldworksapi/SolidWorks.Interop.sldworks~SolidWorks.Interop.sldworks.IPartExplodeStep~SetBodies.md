# SetBodies Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep~SetBodies`

Sets the bodies of this explode step.
Sets the bodies of this explode step.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetBodies( _
   ByVal Bodies As System.Object _
) 
```

```

Dim instance As IPartExplodeStep
Dim Bodies As System.Object
 
instance.SetBodies(Bodies)
```

```

void SetBodies( 
   System.object Bodies
)
```

```

void SetBodies( 
   System.Object^ Bodies
) 
```

#### Parameters

*Bodies*
:   Array of solid [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartExplodeStep Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep.md)  
[IPartExplodeStep Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep_members.md)  
[IPartExplodeStep::GetBodies Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep~GetBodies.md)
