# LockLightToModel Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~LockLightToModel`

Obsolete. Superseded by IModelDoc2::LockLightToModel.
Obsolete. Superseded by [IModelDoc2::LockLightToModel](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~LockLightToModel.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function LockLightToModel( _
   ByVal LightId As System.Integer, _
   ByVal Fix As System.Boolean _
) As System.Boolean
```

```

Dim instance As IModelDoc
Dim LightId As System.Integer
Dim Fix As System.Boolean
Dim value As System.Boolean
 
value = instance.LockLightToModel(LightId, Fix)
```

```

System.bool LockLightToModel( 
   System.int LightId,
   System.bool Fix
)
```

```

System.bool LockLightToModel( 
   System.int LightId,
   System.bool Fix
) 
```

#### Parameters

*LightId*

*Fix*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
