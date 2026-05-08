# IGet3rdPartyStorage Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~IGet3rdPartyStorage`

Obsolete. Superseded by IModelDoc2::IGet3rdPartyStorage.
Obsolete. Superseded by [IModelDoc2::IGet3rdPartyStorage](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGet3rdPartyStorage.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGet3rdPartyStorage( _
   ByVal StringIn As System.String, _
   ByVal IsStoring As System.Boolean _
) As System.Object
```

```

Dim instance As IModelDoc
Dim StringIn As System.String
Dim IsStoring As System.Boolean
Dim value As System.Object
 
value = instance.IGet3rdPartyStorage(StringIn, IsStoring)
```

```

System.object IGet3rdPartyStorage( 
   System.string StringIn,
   System.bool IsStoring
)
```

```

System.Object^ IGet3rdPartyStorage( 
   System.String^ StringIn,
   System.bool IsStoring
) 
```

#### Parameters

*StringIn*

*IsStoring*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
