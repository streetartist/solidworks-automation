# ISetBody2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ISetBody2`

Obsolete. Superseded by IFeature::ISetBody3.
Obsolete. Superseded by [IFeature::ISetBody3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ISetBody3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ISetBody2( _
   ByVal BodyIn As Body, _
   ByVal ApplyUserIds As System.Boolean _
) As System.Boolean
```

```

Dim instance As IFeature
Dim BodyIn As Body
Dim ApplyUserIds As System.Boolean
Dim value As System.Boolean
 
value = instance.ISetBody2(BodyIn, ApplyUserIds)
```

```

System.bool ISetBody2( 
   Body BodyIn,
   System.bool ApplyUserIds
)
```

```

System.bool ISetBody2( 
   Body^ BodyIn,
   System.bool ApplyUserIds
) 
```

#### Parameters

*BodyIn*

*ApplyUserIds*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)
