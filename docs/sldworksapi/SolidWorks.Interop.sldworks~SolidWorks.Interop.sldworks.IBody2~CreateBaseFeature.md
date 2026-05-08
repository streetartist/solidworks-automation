# CreateBaseFeature Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateBaseFeature`

Creates a base feature for the imported body.
Creates a base feature for the imported body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateBaseFeature( _
   ByVal BodyIn As System.Object _
) As System.Boolean
```

```

Dim instance As IBody2
Dim BodyIn As System.Object
Dim value As System.Boolean
 
value = instance.CreateBaseFeature(BodyIn)
```

```

System.bool CreateBaseFeature( 
   System.object BodyIn
)
```

```

System.bool CreateBaseFeature( 
   System.Object^ BodyIn
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
[IBody2::ICreateBaseFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateBaseFeature.md)
