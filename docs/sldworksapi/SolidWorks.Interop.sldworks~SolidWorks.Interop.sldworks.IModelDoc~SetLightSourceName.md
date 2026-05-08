# SetLightSourceName Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SetLightSourceName`

Obsolete. Superseded by IModelDoc2::SetLightSourceName.
Obsolete. Superseded by [IModelDoc2::SetLightSourceName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetLightSourceName.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetLightSourceName( _
   ByVal ID As System.Integer, _
   ByVal NewName As System.String _
) As System.Boolean
```

```

Dim instance As IModelDoc
Dim ID As System.Integer
Dim NewName As System.String
Dim value As System.Boolean
 
value = instance.SetLightSourceName(ID, NewName)
```

```

System.bool SetLightSourceName( 
   System.int ID,
   System.string NewName
)
```

```

System.bool SetLightSourceName( 
   System.int ID,
   System.String^ NewName
) 
```

#### Parameters

*ID*

*NewName*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
