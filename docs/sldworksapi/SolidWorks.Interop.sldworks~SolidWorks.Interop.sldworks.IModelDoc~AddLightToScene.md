# AddLightToScene Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~AddLightToScene`

Obsolete. Superseded by IModelDoc2::AddLightToScene.
Obsolete. Superseded by [IModelDoc2::AddLightToScene](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddLightToScene.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddLightToScene( _
   ByVal LpszNewValue As System.String _
) As System.Integer
```

```

Dim instance As IModelDoc
Dim LpszNewValue As System.String
Dim value As System.Integer
 
value = instance.AddLightToScene(LpszNewValue)
```

```

System.int AddLightToScene( 
   System.string LpszNewValue
)
```

```

System.int AddLightToScene( 
   System.String^ LpszNewValue
) 
```

#### Parameters

*LpszNewValue*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
