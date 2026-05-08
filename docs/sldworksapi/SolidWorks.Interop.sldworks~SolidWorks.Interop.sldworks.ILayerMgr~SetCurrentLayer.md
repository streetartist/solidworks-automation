# SetCurrentLayer Method (ILayerMgr)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~SetCurrentLayer`

Sets the current (or active) layer in this drawing document.
Sets the current (or active) layer in this drawing document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetCurrentLayer( _
   ByVal NameIn As System.String _
) As System.Integer
```

```

Dim instance As ILayerMgr
Dim NameIn As System.String
Dim value As System.Integer
 
value = instance.SetCurrentLayer(NameIn)
```

```

System.int SetCurrentLayer( 
   System.string NameIn
)
```

```

System.int SetCurrentLayer( 
   System.String^ NameIn
) 
```

#### Parameters

*NameIn*
:   Name of the layer to become the active layer

#### Return Value

1 if the active layer was changed to the specified layer, 0 if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILayerMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr.md)  
[ILayerMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr_members.md)  
[ILayerMgr::GetCurrentLayer Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~GetCurrentLayer.md)
