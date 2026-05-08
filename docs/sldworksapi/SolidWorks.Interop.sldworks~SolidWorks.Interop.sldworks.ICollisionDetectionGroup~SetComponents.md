# SetComponents Method (ICollisionDetectionGroup)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionGroup~SetComponents`

Sets the specified components in this collision detection group.
Sets the specified components in this collision detection group.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetComponents( _
   ByVal Components As System.Object _
) As System.Integer
```

```

Dim instance As ICollisionDetectionGroup
Dim Components As System.Object
Dim value As System.Integer
 
value = instance.SetComponents(Components)
```

```

System.int SetComponents( 
   System.object Components
)
```

```

System.int SetComponents( 
   System.Object^ Components
) 
```

#### Parameters

*Components*
:   Array of [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)

#### Return Value

Return code as defined in [swCollisionGroupSetComponentsErrors\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCollisionGroupSetComponentsErrors_e.html)

Example

See the [ICollisionDetectionManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICollisionDetectionGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionGroup.md)  
[ICollisionDetectionGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionGroup_members.md)
