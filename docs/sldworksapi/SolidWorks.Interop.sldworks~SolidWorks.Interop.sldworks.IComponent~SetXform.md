# SetXform Method (IComponent)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent~SetXform`

Obsolete. Superseded by IComponent2::Transform2.
Obsolete. Superseded by [IComponent2::Transform2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Transform2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetXform( _
   ByVal XformIn As System.Object _
) As System.Boolean
```

```

Dim instance As IComponent
Dim XformIn As System.Object
Dim value As System.Boolean
 
value = instance.SetXform(XformIn)
```

```

System.bool SetXform( 
   System.object XformIn
)
```

```

System.bool SetXform( 
   System.Object^ XformIn
) 
```

#### Parameters

*XformIn*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent.md)  
[IComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent_members.md)
