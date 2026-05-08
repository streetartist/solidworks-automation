# IRestore2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IRestore2`

Restores a temporary body object from the specified stream.
Restores a temporary body object from the specified stream.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IRestore2( _
   ByVal StreamIn As System.Object _
) As Body2
```

```

Dim instance As IModeler
Dim StreamIn As System.Object
Dim value As Body2
 
value = instance.IRestore2(StreamIn)
```

```

Body2 IRestore2( 
   System.object StreamIn
)
```

```

Body2^ IRestore2( 
   System.Object^ StreamIn
) 
```

#### Parameters

*StreamIn*
:   IStream interface for storage inside the SOLIDWORKS document

#### Return Value

Temporary [body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

Remarks

You can use a temporary body object for display purposes. You can generate temporary bodies using such methods as [IModeler::CreateBodyFromFaces2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromFaces2.md) or [IModeler::ICreateBodyFromFaces3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromFaces3.md). Temporary bodies are not saved with the document unless you explicitly save them using [IBody2::Save](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Save.md) or [IBody2::ISave](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ISave.md).

You can obtain the StreamIn object by calling [IModelDoc2::IGet3rdPartyStorage](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGet3rdPartyStorage.md) and by specifying the stream name that was used during the body save operation.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)  
[IModeler::Restore Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~Restore.md)
