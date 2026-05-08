# IGetLayer Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~IGetLayer`

Gets the specified layer in this drawing document.
Gets the specified layer in this drawing document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetLayer( _
   ByVal NameIn As System.String _
) As Layer
```

```

Dim instance As ILayerMgr
Dim NameIn As System.String
Dim value As Layer
 
value = instance.IGetLayer(NameIn)
```

```

Layer IGetLayer( 
   System.string NameIn
)
```

```

Layer^ IGetLayer( 
   System.String^ NameIn
) 
```

#### Parameters

*NameIn*
:   Layer name

#### Return Value

[ILayer](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer.md) object

Remarks

You can get the layer name by calling [ILayerMgr::GetCurrentLayer](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~GetCurrentLayer.md), create a new layer calling [ILayerMgr::AddLayer](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~AddLayer.md), or obtain a list of layer names by calling [ILayerMgr::IGetLayerList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~IGetLayerList.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILayerMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr.md)  
[ILayerMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr_members.md)  
[ILayerMgr::GetLayer Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~GetLayer.md)
