# IsPatternSeed Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IsPatternSeed`

Gets whether this body is the seed of a patterned body.
Gets whether this body is the seed of a patterned body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsPatternSeed( _
   ByVal BodyDispIn As System.Object _
) As System.Boolean
```

```

Dim instance As IBody2
Dim BodyDispIn As System.Object
Dim value As System.Boolean
 
value = instance.IsPatternSeed(BodyDispIn)
```

```

System.bool IsPatternSeed( 
   System.object BodyDispIn
)
```

```

System.bool IsPatternSeed( 
   System.Object^ BodyDispIn
) 
```

#### Parameters

*BodyDispIn*
:   Patterned body

#### Return Value

True if this body is the seed of the patterned body, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)
