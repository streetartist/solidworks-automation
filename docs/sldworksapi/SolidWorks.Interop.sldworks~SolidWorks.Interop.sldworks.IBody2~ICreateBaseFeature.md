# ICreateBaseFeature Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateBaseFeature`

Creates a base feature for the imported body.
Creates a base feature for the imported body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateBaseFeature( _
   ByVal BodyIn As Body2 _
) As System.Boolean
```

```

Dim instance As IBody2
Dim BodyIn As Body2
Dim value As System.Boolean
 
value = instance.ICreateBaseFeature(BodyIn)
```

```

System.bool ICreateBaseFeature( 
   Body2 BodyIn
)
```

```

System.bool ICreateBaseFeature( 
   Body2^ BodyIn
) 
```

#### Parameters

*BodyIn*
:   [Body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) on which to create base feature

#### Return Value

True if the base feature was created, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::CreateBaseFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateBaseFeature.md)
