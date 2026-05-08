# HideBody Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~HideBody`

Hides or shows this body.
Hides or shows this body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub HideBody( _
   ByVal BHide As System.Boolean _
) 
```

```

Dim instance As IBody2
Dim BHide As System.Boolean
 
instance.HideBody(BHide)
```

```

void HideBody( 
   System.bool BHide
)
```

```

void HideBody( 
   System.bool BHide
) 
```

#### Parameters

*BHide*
:   True to hide the body, false to show the body

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IFeatureManager::ShowBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowBodies.md)
