# IHide Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IHide`

Hides a temporary body using the specified part's context.
Hides a temporary body using the specified part's context.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub IHide( _
   ByVal Part As PartDoc _
) 
```

```

Dim instance As IBody2
Dim Part As PartDoc
 
instance.IHide(Part)
```

```

void IHide( 
   PartDoc Part
)
```

```

void IHide( 
   PartDoc^ Part
) 
```

#### Parameters

*Part*
:   [IPartDoc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)

Remarks

While SOLIDWORKS is displaying your IBody2 object using [IBody2::Display3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Display3.md), you cannot release it explicitly or implicitly. Before releasing or allowing your IBody2 object to be released, you must call this method to prevent it from being displayed.

COM applications should avoid explicitly releasing the IBody2 object by calling IBody2->Release() while it is being displayed by SOLIDWORKS.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::Hide Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Hide.md)
