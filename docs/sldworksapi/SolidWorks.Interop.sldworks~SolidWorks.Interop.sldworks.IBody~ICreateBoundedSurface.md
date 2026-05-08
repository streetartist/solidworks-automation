# ICreateBoundedSurface Method (IBody)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~ICreateBoundedSurface`

Obsolete. Superseded by IBody2::ICreateBoundedSurface.
Obsolete. Superseded by [IBody2::ICreateBoundedSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateBoundedSurface.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ICreateBoundedSurface( _
   ByVal UOpt As System.Boolean, _
   ByVal VOpt As System.Boolean, _
   ByRef UvParams As System.Double _
) 
```

```

Dim instance As IBody
Dim UOpt As System.Boolean
Dim VOpt As System.Boolean
Dim UvParams As System.Double
 
instance.ICreateBoundedSurface(UOpt, VOpt, UvParams)
```

```

void ICreateBoundedSurface( 
   System.bool UOpt,
   System.bool VOpt,
   ref System.double UvParams
)
```

```

void ICreateBoundedSurface( 
   System.bool UOpt,
   System.bool VOpt,
   System.double% UvParams
) 
```

#### Parameters

*UOpt*

*VOpt*

*UvParams*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.md)  
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.md)
